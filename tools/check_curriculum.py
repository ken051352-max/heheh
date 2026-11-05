#!/usr/bin/env python3
"""Validate the curriculum manifest and its generated guide tables, offline.

Run without flags (or with --check) in CI. After an intentional manifest edit,
run --write to replace only the three marked table bodies, then review the diff.
This validates declared prerequisites and URL syntax, not learning outcomes or
external resource availability. Unnumbered project prerequisites remain prose.
"""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import urlsplit

if __package__:
    from .check_links import anchors_of
else:
    from check_links import anchors_of

ROOT = Path(__file__).resolve().parents[1]
MODULE_IDS = ({f"M{i}" for i in range(19)} - {"M8"}) | {
    "M6h", "M8a", "M8b", *(f"M{i}" for i in range(21, 27))}
SUBSET_IDS = {"M18-app", "M25-brief", "M26-research", "M26-systems", "M26-applied"}
ROUTE_IDS = {"analyst", "applied-ds", "ml-engineer", "ai-application", "research", "data-engineer"}
SUBSET_LABELS = {"M18-app": "M18 application foundations", "M25-brief": "M25 product brief",
                 "M26-research": "M26 research", "M26-systems": "M26 systems",
                 "M26-applied": "M26 applied"}


def valid_url(value):
    """A well-formed public HTTP(S) destination; this makes no network request."""
    try:
        parsed = urlsplit(value)
        return (parsed.scheme in {"http", "https"} and bool(parsed.hostname)
                and not parsed.username and not parsed.password
                and not re.search(r"[\s<>|\\]", value) and parsed.port != 0)
    except ValueError:
        return False


def schema_errors(data):
    errors = []
    if not isinstance(data, dict):
        return ["manifest must be an object"]
    fields = {
        "modules": ("id", "title", "path", "anchor", "default_url", "book", "book_url"),
        "subsets": ("id", "parent", "anchor"), "routes": ("id", "title")}
    lists = {"modules": ("requires", "recommends"), "subsets": ("requires",), "routes": ("steps",)}
    for section in fields:
        if not isinstance(data.get(section), list):
            errors.append(f"{section} must be a list")
            continue
        for index, entry in enumerate(data[section]):
            label = f"{section}[{index}]"
            if not isinstance(entry, dict):
                errors.append(f"{label} must be an object")
                continue
            for field in fields[section]:
                value = entry.get(field)
                if not isinstance(value, str) or (not value.strip() and field not in {"default_url", "book_url"}):
                    errors.append(f"{label}.{field} must be a string" + ("" if field.endswith("url") else " with content"))
            for field in lists[section]:
                value = entry.get(field)
                if not isinstance(value, list) or any(not isinstance(v, str) or not v for v in value):
                    errors.append(f"{label}.{field} must be a list of IDs")
                elif len(value) != len(set(value)):
                    errors.append(f"{label}.{field} contains duplicate IDs")
    return errors


def validate(data, root=ROOT):
    """Return actionable errors for schema, targets, graph and ordered routes."""
    errors = schema_errors(data)
    if errors:
        return errors
    modules = {entry["id"]: entry for entry in data["modules"]}
    subsets = {entry["id"]: entry for entry in data["subsets"]}
    nodes = {**modules, **subsets}
    for section, expected in (("modules", MODULE_IDS), ("subsets", SUBSET_IDS), ("routes", ROUTE_IDS)):
        actual = [entry["id"] for entry in data[section]]
        if len(actual) != len(set(actual)):
            errors.append(f"{section}: duplicate IDs")
        if set(actual) != expected:
            errors.append(f"{section}: missing IDs {sorted(expected - set(actual))}; unexpected IDs {sorted(set(actual) - expected)}")
    if modules.keys() & subsets.keys():
        errors.append("module and subset IDs must be distinct")
    root = Path(root).resolve()
    anchor_cache = {}

    def check_target(identifier, path, anchor):
        relative = PurePosixPath(path)
        target = (root / path).resolve()
        if (relative.is_absolute() or ".." in relative.parts or "\\" in path or ":" in path
                or not target.is_relative_to(root) or target.suffix != ".md"):
            errors.append(f"{identifier}: path must be a repository-relative Markdown file")
            return
        if not target.is_file():
            errors.append(f"{identifier}: missing file {path}")
            return
        if target not in anchor_cache:
            anchor_cache[target] = anchors_of(target)
        if anchor not in anchor_cache[target]:
            errors.append(f"{identifier}: missing anchor {path}#{anchor}")

    for identifier, node in nodes.items():
        for field in ("requires", "recommends"):
            for dependency in node.get(field, []):
                if dependency not in nodes:
                    errors.append(f"{identifier}.{field}: unknown ID {dependency}")
        if identifier in modules:
            check_target(identifier, node["path"], node["anchor"])
            for field in ("default_url", "book_url"):
                value = node[field]
                if not (identifier == "M26" and value == "") and not valid_url(value):
                    errors.append(f"{identifier}.{field}: expected an http(s) URL")
        elif node["parent"] not in modules:
            errors.append(f"{identifier}: unknown parent module {node['parent']}")
        else:
            check_target(identifier, modules[node["parent"]]["path"], node["anchor"])

    # Only strict prerequisite edges must be acyclic. Recommended topics may
    # deliberately refer forward, and a subset does not require its full parent.
    visited, active = set(), []

    def visit(identifier):
        if identifier in active:
            errors.append("prerequisite cycle: " + " -> ".join(active[active.index(identifier):] + [identifier]))
            return
        if identifier in visited:
            return
        active.append(identifier)
        for dependency in nodes[identifier]["requires"]:
            if dependency in nodes:
                visit(dependency)
        active.pop()
        visited.add(identifier)

    for identifier in nodes:
        visit(identifier)
    for route in data["routes"]:
        available = set()
        for identifier in route["steps"]:
            if identifier not in nodes:
                errors.append(f"route {route['id']}: unknown step {identifier}")
                continue
            if identifier == "M26":
                errors.append(f"route {route['id']}: choose a conditional M26 subset, not the unqualified capstone")
            missing = set(nodes[identifier]["requires"]) - available
            if missing:
                errors.append(f"route {route['id']}: {identifier} requires earlier {', '.join(sorted(missing))}")
                # An invalid step cannot confer competence on later steps.
                continue
            available.add(identifier)
            if identifier in modules:
                available.update(subset_id for subset_id, subset in subsets.items()
                                 if subset["parent"] == identifier and identifier != "M26")
    return errors


def cell(text):
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("\n", " ").replace("\r", " ")


def render_tables(data):
    """Produce guide-relative Markdown, preserving the manifest's display order."""
    modules = {entry["id"]: entry for entry in data["modules"]}
    subsets = {entry["id"]: entry for entry in data["subsets"]}

    def link(identifier, titled=False):
        node = modules.get(identifier) or subsets[identifier]
        path = node.get("path") or modules[node["parent"]]["path"]
        label = "M6½" if identifier == "M6h" else SUBSET_LABELS.get(identifier, identifier)
        if titled:
            label += " — " + node["title"]
        return f"[{cell(label)}](../{path}#{node['anchor']})"

    # Stacked resource cards reflow on narrow screens. Marker names remain
    # unchanged so existing integrations and drift checks keep working.
    defaults = []
    prerequisites = ["| Module | Required modules | Recommended modules |", "| :--- | :--- | :--- |"]
    for node in data["modules"]:
        course = f"[Free course / lecture route]({node['default_url']})" if node["default_url"] else "Use your chosen capstone topic"
        book = f"[{cell(node['book'])}]({node['book_url']})" if node["book_url"] else cell(node["book"])
        defaults.extend([f'<a id="default-{node["id"].lower()}"></a>',
                         f"### {link(node['id'], titled=True)}", "",
                         f"- **Free teaching route:** {course}",
                         f"- **Principal book:** {book}", ""])
        required = ", ".join(link(dep) for dep in node["requires"]) or "None"
        if node["id"] == "M24":
            required = "An evaluated project (see module)"
        elif node["id"] == "M26":
            required = "Depends on the chosen capstone route (see below)"
        recommended = ", ".join(link(dep) for dep in node["recommends"]) or "None"
        prerequisites.append(f"| {link(node['id'])} | {required} | {recommended} |")
    for node in data["subsets"]:
        required = ", ".join(link(dep) for dep in node["requires"]) or "None"
        prerequisites.append(f"| {link(node['id'])} | {required} | None |")
    routes = []
    for route in data["routes"]:
        routes.extend([f'<a id="route-{route["id"]}"></a>',
                       f"### {cell(route['title'])}", "",
                       " → ".join(link(step) for step in route["steps"]), ""])
    return {"guides/how-to-read-a-module.md": {"MODULE DEFAULTS": "\n".join(defaults).rstrip()},
            "guides/practitioner-track.md": {"ROLE ROUTES": "\n".join(routes).rstrip(), "PREREQUISITES": "\n".join(prerequisites)}}


def sync_tables(data, root=ROOT, write=False):
    """Check or update exact marker bodies; refuse ambiguous/missing markers."""
    errors, pending = [], {}
    for relative, sections in render_tables(data).items():
        path = Path(root) / relative
        if not path.is_file():
            errors.append(f"missing generated guide: {relative}")
            continue
        with path.open(encoding="utf-8", newline="") as source:
            original = source.read()
        newline = "\r\n" if "\r\n" in original else "\n"
        updated = original
        for name, table in sections.items():
            begin, end = f"<!-- BEGIN {name} -->", f"<!-- END {name} -->"
            if updated.count(begin) != 1 or updated.count(end) != 1 or updated.index(begin) >= updated.index(end):
                errors.append(f"{relative}: expected exactly one ordered {name} marker pair")
                continue
            start = updated.index(begin) + len(begin)
            stop = updated.index(end)
            replacement = newline * 2 + table.replace("\n", newline) + newline * 2
            if updated[start:stop] != replacement and not write:
                errors.append(f"{relative}: generated {name} table drift; run python tools/check_curriculum.py --write")
            updated = updated[:start] + replacement + updated[stop:]
        if updated != original:
            pending[path] = updated
    # Never partially write if a guide lacks a required marker.
    if write and not errors:
        for path, updated in pending.items():
            path.write_text(updated, encoding="utf-8", newline="")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="validate and fail on generated-table drift (default)")
    mode.add_argument("--write", action="store_true", help="validate and regenerate only marked table bodies")
    args = parser.parse_args(argv)
    try:
        data = json.loads((ROOT / "curriculum/modules.json").read_text(encoding="utf-8-sig"))
        errors = validate(data)
        if not errors:
            errors = sync_tables(data, write=args.write)
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        errors = [str(error)]
    for error in errors:
        print("ERROR: " + error)
    if errors:
        print(f"Curriculum integrity: {len(errors)} failure(s)")
        return 1
    print("Curriculum integrity: 27 modules, 5 subsets, 6 ordered routes; targets and generated tables valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
