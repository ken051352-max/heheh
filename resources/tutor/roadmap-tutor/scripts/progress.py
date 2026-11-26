"""Private, offline study planning and evidence log; never certifies mastery.

Uses only Python's standard library. Run with --help for the CLI. State belongs
to the learner in study-private/tutor, not to the curriculum or its tracker.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import date, datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import sys
import tempfile


class ProgressError(ValueError):
    """Invalid input or unsafe state; leave existing learner records intact."""


def _object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ProgressError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _constant(value):
    raise ProgressError(f"Non-finite JSON number: {value}")


def read_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8-sig"),
                          object_pairs_hook=_object, parse_constant=_constant)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ProgressError(f"Cannot read valid JSON from {path}: {exc}") from exc


def _fields(value, required, optional=()):
    if not isinstance(value, dict):
        raise ProgressError("Expected a JSON object")
    missing = set(required) - value.keys()
    extra = value.keys() - set(required) - set(optional)
    if missing or extra:
        raise ProgressError(f"Invalid fields: missing {sorted(missing)}, unknown {sorted(extra)}")


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ProgressError(f"{label} must be a nonempty string")


def _date(value, label):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ProgressError(f"{label} must use YYYY-MM-DD")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ProgressError(f"Invalid {label}: {value}") from exc


def _minutes(value, label, minimum=0, maximum=None):
    if type(value) is not int or value < minimum or (maximum is not None and value > maximum):
        raise ProgressError(f"{label} must be an integer >= {minimum}" +
                            (f" and <= {maximum}" if maximum is not None else ""))


def _choice(value, label, choices):
    if not isinstance(value, str) or value not in choices:
        raise ProgressError(f"{label} must be one of {', '.join(sorted(choices))}")


def validate_plan(plan, module_ids):
    _fields(plan, ("week_start", "available_minutes", "buffer_minutes", "tasks"))
    _date(plan["week_start"], "week_start")
    _minutes(plan["available_minutes"], "available_minutes", maximum=10080)
    _minutes(plan["buffer_minutes"], "buffer_minutes")
    if not isinstance(plan["tasks"], list):
        raise ProgressError("tasks must be a list")
    seen = set()
    total = plan["buffer_minutes"]
    for task in plan["tasks"]:
        _fields(task, ("id", "module_id", "task", "minutes", "reference", "readiness_check"))
        for key in ("id", "task", "reference", "readiness_check"):
            _text(task[key], key)
        _choice(task["module_id"], "module_id", module_ids)
        _minutes(task["minutes"], "task minutes", minimum=1)
        if task["id"] in seen:
            raise ProgressError(f"Duplicate task ID: {task['id']}")
        seen.add(task["id"])
        total += task["minutes"]
    if total > plan["available_minutes"]:
        raise ProgressError("Tasks plus buffer exceed available_minutes; reduce scope")


def validate_record(record, module_ids):
    _fields(record, ("id", "date", "module_id", "capability", "task", "minutes",
                     "artifact", "evidence", "evidence_source", "assistance",
                     "understanding", "next_action"), ("review_after",))
    for key in ("id", "capability", "task", "next_action"):
        _text(record[key], key)
    _date(record["date"], "date")
    _choice(record["module_id"], "module_id", module_ids)
    if record["minutes"] is not None:
        _minutes(record["minutes"], "minutes")
    if record["artifact"] is not None:
        _text(record["artifact"], "artifact")
    if not isinstance(record["evidence"], str):
        raise ProgressError("evidence must be a string (empty is allowed before assessment)")
    _choice(record["evidence_source"], "evidence_source", {"learner-report", "tutor-observed"})
    _choice(record["assistance"], "assistance", {"none", "hints", "solution", "mixed"})
    _choice(record["understanding"], "understanding",
            {"not-attempted", "assisted", "independent", "needs-review"})
    if record["understanding"] == "independent":
        _text(record["evidence"], "independent evidence")
        _text(record["artifact"], "independent artifact")
    if record.get("review_after") is not None:
        _date(record["review_after"], "review_after")
        if record["review_after"] < record["date"]:
            raise ProgressError("review_after cannot precede the session date")


def _safe_path(path, boundary):
    """Reject symlinks/junctions in every component beneath the trusted root."""
    try:
        relative = path.relative_to(boundary)
    except ValueError as exc:
        raise ProgressError(f"Path leaves private storage: {path}") from exc
    current = boundary
    for component in relative.parts:
        current = current / component
        if current.is_symlink() or current.resolve() != current:
            raise ProgressError(f"Symlink or redirected path is not allowed: {current}")
    return path


class Store:
    def __init__(self, root):
        self.root = Path(root).resolve(strict=True)
        manifest_path = _safe_path(self.root / "curriculum/modules.json", self.root)
        manifest = read_json(manifest_path)
        try:
            self.module_ids = {item["id"] for group in ("modules", "subsets") for item in manifest[group]}
            self.route_ids = {item["id"] for item in manifest["routes"]}
        except (KeyError, TypeError) as exc:
            raise ProgressError("Expected curriculum/modules.json with modules, subsets and routes") from exc
        if not self.module_ids or any(not isinstance(item, str) for item in self.module_ids | self.route_ids):
            raise ProgressError("Manifest IDs must be nonempty strings")
        self.directory = self.root / "study-private/tutor"
        self.path = self.directory / "state.json"
        self.backup = self.directory / "state.previous.json"
        self.lock_path = self.directory / "state.lock"

    @contextmanager
    def _locked(self):
        for path in (self.root / "study-private", self.directory):
            _safe_path(path, self.root)
            path.mkdir(exist_ok=True)
        for path in (self.path, self.backup, self.lock_path):
            _safe_path(path, self.root)
            if path.exists() and not path.is_file():
                raise ProgressError(f"Expected a regular file: {path}")
            if path.exists() and path.stat().st_nlink > 1:
                raise ProgressError(f"Hard-linked private state is not allowed: {path}")
        try:
            descriptor = os.open(self.lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY,
                                 0o600)
        except FileExistsError as exc:
            raise ProgressError("Progress store is locked. Do not remove state.lock until you have "
                                "confirmed no writer is running; a stale lock needs manual review.") from exc
        try:
            os.write(descriptor, f"pid={os.getpid()}\n".encode("ascii"))
            yield
        finally:
            identity = os.fstat(descriptor)
            os.close(descriptor)
            _safe_path(self.lock_path, self.root)
            if self.lock_path.exists():
                current = self.lock_path.stat()
                if (current.st_dev, current.st_ino) == (identity.st_dev, identity.st_ino):
                    self.lock_path.unlink()

    def _validate_state(self, state):
        _fields(state, ("schema_version", "timezone", "role_focus", "sessions", "plan"))
        if type(state["schema_version"]) is not int or state["schema_version"] != 1:
            raise ProgressError("Unsupported schema_version; do not reset existing data")
        _choice(state["timezone"], "timezone", {"Asia/Kolkata"})
        _choice(state["role_focus"], "role_focus", self.route_ids | {"undecided"})
        if state["plan"] is not None:
            validate_plan(state["plan"], self.module_ids)
        if not isinstance(state["sessions"], list):
            raise ProgressError("sessions must be a list")
        seen = set()
        for record in state["sessions"]:
            validate_record(record, self.module_ids)
            if record["id"] in seen:
                raise ProgressError(f"Duplicate stored session ID: {record['id']}")
            seen.add(record["id"])

    def _read(self):
        if not self.path.exists():
            raise ProgressError("No progress state exists; run init first")
        state = read_json(self.path)
        self._validate_state(state)
        return state

    def _atomic_write(self, path, payload):
        descriptor, temporary = tempfile.mkstemp(prefix=".state-", suffix=".tmp", dir=self.directory)
        temporary_path = Path(temporary)
        try:
            with os.fdopen(descriptor, "wb") as stream:
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            _safe_path(path, self.root)
            os.replace(temporary_path, path)
        finally:
            if temporary_path.exists():
                temporary_path.unlink()

    def _write(self, state):
        self._validate_state(state)
        if self.path.exists():
            self._atomic_write(self.backup, self.path.read_bytes())
        payload = (json.dumps(state, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")
        self._atomic_write(self.path, payload)

    def init(self):
        with self._locked():
            if self.path.exists():
                return self._read()
            if self.backup.exists():
                raise ProgressError("State missing but a backup exists; inspect and recover manually before init")
            state = {"schema_version": 1, "timezone": "Asia/Kolkata", "role_focus": "undecided",
                     "sessions": [], "plan": None}
            self._write(state)
            return state

    def set_plan(self, plan):
        validate_plan(plan, self.module_ids)
        with self._locked():
            state = self._read()
            if state["plan"] != plan:
                state["plan"] = plan
                self._write(state)
            return state

    def record(self, record):
        validate_record(record, self.module_ids)
        with self._locked():
            state = self._read()
            existing = next((item for item in state["sessions"] if item["id"] == record["id"]), None)
            if existing is not None:
                if existing != record:
                    raise ProgressError("Session ID already exists with different data; use a new ID for new evidence")
                return state
            state["sessions"].append(record)
            self._write(state)
            return state

    def status(self, as_of=None):
        if as_of is None:
            as_of = datetime.now(timezone(timedelta(hours=5, minutes=30))).date().isoformat()
        _date(as_of, "as_of")
        with self._locked():
            state = self._read()
        eligible = [item for item in state["sessions"] if item["date"] <= as_of]
        ordered = sorted(eligible, key=lambda item: item["date"])
        latest = {}
        for item in ordered:
            latest[(item["module_id"], item["capability"])] = item
        due = [item for item in latest.values()
               if item.get("review_after") is not None and item["review_after"] <= as_of]
        return {
            "as_of": as_of,
            "timezone": state["timezone"],
            "role_focus": state["role_focus"],
            "session_count": len(eligible),
            "known_minutes": sum(item["minutes"] for item in eligible if item["minutes"] is not None),
            "unknown_minutes_sessions": sum(item["minutes"] is None for item in eligible),
            "last_next_action": ordered[-1]["next_action"] if ordered else None,
            "due_reviews": [{key: item[key] for key in ("module_id", "capability", "review_after", "next_action")}
                            for item in sorted(due, key=lambda item: (item["review_after"], item["module_id"], item["capability"]))],
            "plan": state["plan"],
            "note": "Evidence log only, not mastery certification. Plan is the current plan, not historical. "
                    "Review prompts appear only when status runs; no notifications are scheduled.",
        }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path, help="Roadmap checkout containing curriculum/modules.json")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="Create empty private state, or validate existing state")
    status = commands.add_parser("status", help="Show recorded evidence and due review prompts")
    status.add_argument("--as-of", help="YYYY-MM-DD; defaults to today's date in India")
    for name in ("plan", "record"):
        command = commands.add_parser(name)
        command.add_argument("--file", required=True, type=Path, help="Input JSON file; keep personal inputs private")
    args = parser.parse_args(argv)
    try:
        store = Store(args.root)
        if args.command == "init":
            result = store.init()
        elif args.command == "status":
            result = store.status(args.as_of)
        elif args.command == "plan":
            result = store.set_plan(read_json(args.file))
        else:
            result = store.record(read_json(args.file))
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
        return 0
    except (ProgressError, OSError, RuntimeError) as exc:
        print(f"progress: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
