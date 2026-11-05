#!/usr/bin/env python3
"""Validate markdown links in the repo.

Default mode (used by CI, must stay fast and offline):
  1. relative file targets exist;
  2. #anchors resolve in the target file, using GitHub's rules:
     explicit <a id="..."> tags OR heading-derived slugs
     (lowercase, strip punctuation/emoji, spaces->hyphens, dedupe with -1, -2).
  Exit code 1 on any internal failure.

Optional external mode (network; report-only unless --strict-external):
  python3 tools/check_links.py --external [--paths curriculum coursepages ...]
                               [--report audit/external.md] [--strict-external]
  Checks http(s) URLs in supported Markdown links, HTML links/images and autolinks.
  Classification:
    OK    2xx/3xx after following redirects
    WARN  access blocked, rate-limited, transient HTTP or network error; unverified
    FAIL  the server reports 404 or 410 after a GET retry
  Redirects that land on a different host are listed so moved courses can be reviewed.
"""
import argparse
from datetime import datetime, timezone
import html
from html.parser import HTMLParser
import http.cookiejar
import concurrent.futures
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXCLUDED_DIRS = {".git", ".venv", "venv", "node_modules", ".pytest_cache",
                 "__pycache__", ".research"}
AUTOLINK = re.compile(r"<(https?://[^>\s]+)>")
HEADING = re.compile(r"^ {0,3}#{1,6}(?:[ \t]+(.*)|[ \t]*)$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
REFERENCE = re.compile(r"^ {0,3}\[([^\]]+)\]:[ \t]*(.*)$", re.M)


def markdown_files(root):
    """Find source Markdown without entering environment/cache directories."""
    found = []
    for directory, children, files in os.walk(root):
        children[:] = sorted(d for d in children if d not in EXCLUDED_DIRS
                             and not os.path.isfile(os.path.join(directory, d, "pyvenv.cfg")))
        found.extend(os.path.join(directory, name) for name in sorted(files)
                     if name.endswith(".md"))
    return found


def prose_blocks(text):
    """Hide fenced/indented code and HTML comments, preserving line boundaries.

    Supports ordinary top-level CommonMark backtick/tilde fences, including
    fences longer than three characters. This is not a full Markdown renderer.
    """
    text = re.sub(r"<!--.*?-->", lambda m: "\n" * m[0].count("\n"), text, flags=re.S)
    out, fence = [], None
    for line in text.splitlines(keepends=True):
        match = FENCE.match(line.rstrip("\r\n"))
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            out.append("\n")
        elif match and not (match[1][0] == "`" and "`" in match[2]):
            fence = match[1]
            out.append("\n")
        elif line.startswith(("    ", "\t")):
            out.append("\n")
        else:
            out.append(line)
    return "".join(out)


def without_inline_code(text):
    return re.sub(r"(`+)(?!`)(.*?)\1(?!`)", "", text, flags=re.S)


class HTMLTargets(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.targets, self.anchors = [], set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for name in ("id", "name" if tag == "a" else "id"):
            if attrs.get(name):
                self.anchors.add(attrs[name])
        for name in ("href" if tag == "a" else "src",):
            if tag in {"a", "img", "source", "video", "audio"} and attrs.get(name):
                self.targets.append(attrs[name])


def unescape_target(value):
    return html.unescape(re.sub(r"\\([!\"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~\\])", r"\1", value))


def destination(text, start):
    """Read a <destination> or a bare destination with balanced parentheses."""
    pos = start
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos < len(text) and text[pos] == "<":
        end = pos + 1
        while end < len(text):
            if text[end] == "\\":
                end += 2
                continue
            if text[end] == ">":
                return unescape_target(text[pos + 1:end]), end + 1
            if text[end] == "\n":
                return None
            end += 1
        return None
    begin, depth = pos, 0
    while pos < len(text):
        char = text[pos]
        if char == "\\" and pos + 1 < len(text):
            pos += 2
            continue
        if char.isspace() or (char == ")" and depth == 0):
            break
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        pos += 1
    if depth:
        return None
    return unescape_target(text[begin:pos]), pos


def label_key(label):
    return " ".join(label.split()).casefold()


def links_of(text):
    """Extract inline, full/collapsed/shortcut reference, HTML and autolinks.

    Reference definitions must put the destination on the definition line.
    Unknown shortcut labels are prose, not links. See tools/README.md for limits.
    """
    text = without_inline_code(prose_blocks(text))
    references = {}
    for match in REFERENCE.finditer(text):
        parsed = destination(match[2], 0)
        if parsed and parsed[0]:
            references.setdefault(label_key(match[1]), parsed[0])
    text = REFERENCE.sub("", text)
    markup = HTMLTargets()
    markup.feed(text)
    targets = markup.targets + [html.unescape(url) for url in AUTOLINK.findall(text)]
    pos = 0
    while pos < len(text):
        if text[pos] == "\\":
            pos += 2
            continue
        if text[pos] != "[":
            pos += 1
            continue
        begin, end, depth = pos + 1, pos + 1, 1
        while end < len(text) and depth:
            if text[end] == "\\":
                end += 2
                continue
            depth += (text[end] == "[") - (text[end] == "]")
            end += 1
        if depth:
            pos += 1
            continue
        label = text[begin:end - 1]
        if end < len(text) and text[end] == "(":
            parsed = destination(text, end + 1)
            if parsed:
                target, stop = parsed
                # Optional title must end before the enclosing closing parenthesis.
                tail = re.match(r'''\s*(?:"[^"\n]*"|'[^'\n]*'|\([^\n)]*\))?\s*\)''', text[stop:])
                if tail:
                    targets.append(target)
                    if "![" in label:
                        targets.extend(links_of(label))
                    pos = stop + tail.end()
                    continue
        elif end < len(text) and text[end] == "[":
            close = text.find("]", end + 1)
            if close != -1:
                key = label_key(text[end + 1:close] or label)
                if key in references:
                    targets.append(references[key])
                pos = close + 1
                continue
        elif label_key(label) in references:
            targets.append(references[label_key(label)])
        pos = end
    return targets


def github_slug(text):
    # strip markdown emphasis and links, keep link text
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = html.unescape(re.sub(r"<[^>]+>", "", text))
    text = text.replace("*", "").replace("`", "")
    out = []
    for ch in text.strip().lower():
        if ch.isalnum():
            out.append(ch)
        elif ch == " ":
            out.append("-")
        elif ch in ("-", "_"):
            out.append(ch)
        elif unicodedata.category(ch).startswith(("L", "N")):
            out.append(ch)
        # else drop (punctuation, emoji, symbols)
    return "".join(out)  # github keeps consecutive hyphens


def anchors_of(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text = prose_blocks(text)
    markup = HTMLTargets()
    markup.feed(without_inline_code(text))
    generated = set()
    lines = text.splitlines()
    for i, line in enumerate(lines):
        match = HEADING.match(line)
        if match:
            heading = re.sub(r"\s+#+\s*$", "", match[1] or "")
        elif i and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line) and lines[i - 1].strip():
            heading = lines[i - 1]
        else:
            continue
        base = github_slug(heading)
        candidate, suffix = base, 0
        while candidate in generated:
            suffix += 1
            candidate = "%s-%d" % (base, suffix)
        generated.add(candidate)
    return markup.anchors | generated


def check_internal(root=ROOT):
    files = markdown_files(root)
    anchors_cache = {p: anchors_of(p) for p in files}
    fails = 0
    checked = 0
    for p in files:
        with open(p, encoding="utf-8") as f:
            text = f.read()
        for t in links_of(text):
            parsed = urllib.parse.urlsplit(t)
            if parsed.scheme or parsed.netloc:
                continue
            if "…" in t:  # prose placeholder (e.g. `src="assets/…"` in audit docs)
                continue
            checked += 1
            anchor = urllib.parse.unquote(parsed.fragment) or None
            rel_file = urllib.parse.unquote(parsed.path)
            if not rel_file:
                fpath = p
            else:
                base = root if rel_file.startswith("/") else os.path.dirname(p)
                fpath = os.path.normpath(os.path.join(base, rel_file.lstrip("/")))
                if not os.path.exists(fpath):
                    print("MISSING FILE  %s -> %s" % (os.path.relpath(p, root), t))
                    fails += 1
                    continue
            if anchor is None or os.path.isdir(fpath) or not fpath.endswith(".md"):
                continue
            if fpath not in anchors_cache:
                anchors_cache[fpath] = anchors_of(fpath)
            if anchor not in anchors_cache[fpath]:
                print("BAD ANCHOR    %s -> %s (in %s)" % (os.path.relpath(p, root), t,
                                                          os.path.relpath(fpath, root)))
                fails += 1
    print("\nchecked %d internal links across %d md files; %d failures" %
          (checked, len(files), fails))
    return fails


# ----------------------------------------------------------------- external
UA = "Mozilla/5.0 (compatible; roadmap-link-checker/1.0)"


def collect_external(paths):
    files = []
    for rel in paths:
        full = os.path.join(ROOT, rel)
        if os.path.isfile(full):
            files.append(full)
        else:
            files.extend(markdown_files(full))
    urls = {}
    for p in sorted(set(files)):
        with open(p, encoding="utf-8") as f:
            text = f.read()
        for u in links_of(text):
            if not u.startswith(("http://", "https://")):
                continue
            urls.setdefault(u, set()).add(os.path.relpath(p, ROOT))
    return urls


def probe(url, timeout):
    """Return (status_label, http_code_or_error, final_url)."""
    last_err = None
    # cookie-aware opener: some sites (e.g. milvus.io) set a cookie then redirect
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={
                "User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
                "Accept-Language": "en"})
            with opener.open(req, timeout=timeout) as r:
                return "OK", r.status, r.geturl()
        except urllib.error.HTTPError as e:
            last_err = e.code
            if method == "HEAD":
                continue  # many servers mishandle HEAD; retry with GET
            break
        except Exception as e:  # DNS, TLS, timeout, connection reset
            last_err = type(e).__name__
            if method == "HEAD":
                continue
            break
    # No host exemption can turn a 404 into a verified resource. Conversely,
    # access failures, server outages and network failures do not prove link rot.
    return ("FAIL" if last_err in (404, 410) else "WARN"), last_err, url


def check_external(paths, report, workers, timeout):
    urls = collect_external(paths)
    print("checking %d unique external URLs in %s ..." % (len(urls), ", ".join(paths)))
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(probe, u, timeout): u for u in urls}
        for fut in concurrent.futures.as_completed(futs):
            results[futs[fut]] = fut.result()
    counts = {"OK": 0, "WARN": 0, "FAIL": 0}
    moved = []
    for u, (label, code, final) in results.items():
        counts[label] += 1
        if label == "OK" and urllib.parse.urlparse(final).netloc != urllib.parse.urlparse(u).netloc:
            moved.append((u, final))
    for label in ("FAIL", "WARN"):
        for u in sorted(k for k, v in results.items() if v[0] == label):
            print("%-5s %-6s %s   (%s)" % (label, results[u][1], u, ", ".join(sorted(urls[u]))))
    for u, final in sorted(moved):
        print("MOVED        %s -> %s" % (u, final))
    print("\nexternal: %d OK · %d WARN (unverified) · %d FAIL (404/410) · %d cross-host redirects" %
          (counts["OK"], counts["WARN"], counts["FAIL"], len(moved)))
    if report:
        with open(os.path.join(ROOT, report), "w", encoding="utf-8") as f:
            f.write("# External link report\n\n")
            f.write("Generated at %s by `python3 tools/check_links.py --external`. " %
                    datetime.now(timezone.utc).isoformat(timespec="seconds"))
            f.write("OK = reachable at check time; WARN = blocked, transient or unverified; "
                    "FAIL = server reports 404/410. HTTP reachability does not verify content, "
                    "price, course access or the truth of a claim.\n\n")
            f.write("**Totals:** %d OK · %d WARN · %d FAIL · %d cross-host redirects\n\n" %
                    (counts["OK"], counts["WARN"], counts["FAIL"], len(moved)))
            f.write("| Status | Code | URL | Found in |\n|---|---|---|---|\n")
            order = {"FAIL": 0, "WARN": 1, "OK": 2}
            for u in sorted(results, key=lambda k: (order[results[k][0]], k)):
                label, code, _ = results[u]
                f.write("| %s | %s | `%s` | %s |\n" % (label, code, u, ", ".join(sorted(urls[u]))))
            if moved:
                f.write("\n## Cross-host redirects (review: course may have moved)\n\n")
                f.write("| Original | Lands on |\n|---|---|\n")
                for u, final in sorted(moved):
                    f.write("| `%s` | `%s` |\n" % (u, final))
        print("report written to", report)
    return counts["FAIL"]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--external", action="store_true",
                    help="also HTTP-check external URLs (needs network)")
    ap.add_argument("--paths", nargs="+",
                    default=["README.md", "START-HERE.md", "FAQ.md", "CONTRIBUTING.md",
                             "CODE_OF_CONDUCT.md", "LICENSE.md", "curriculum", "coursepages",
                             "guides", "resources", "tools", "assets/README.md"],
                    help="files/dirs to scan in --external mode")
    ap.add_argument("--report", help="write a markdown report (repo-relative path)")
    ap.add_argument("--strict-external", action="store_true",
                    help="exit 1 if any external URL FAILs")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--timeout", type=float, default=20.0)
    args = ap.parse_args()
    if args.workers < 1 or args.timeout <= 0:
        ap.error("--workers and --timeout must be positive")

    internal_fails = check_internal()
    external_fails = 0
    if args.external:
        print()
        external_fails = check_external(args.paths, args.report, args.workers, args.timeout)
    if internal_fails or (args.strict_external and external_fails):
        sys.exit(1)


if __name__ == "__main__":
    main()
