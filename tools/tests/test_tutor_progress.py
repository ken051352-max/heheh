"""Behavioral checks for the private, standard-library tutor progress CLI."""

import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "resources/tutor/roadmap-tutor/scripts/progress.py"
SPEC = importlib.util.spec_from_file_location("tutor_progress", SCRIPT)
progress = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(progress)


class TutorProgress(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.root = self.base / "roadmap"
        (self.root / "curriculum").mkdir(parents=True)
        manifest = {"modules": [{"id": "M1"}, {"id": "M8a"}, {"id": "M6h"}],
                    "subsets": [{"id": "M18-app"}], "routes": [{"id": "software"}]}
        (self.root / "curriculum/modules.json").write_text(json.dumps(manifest), encoding="utf-8")
        self.store = progress.Store(self.root)

    def plan(self, **changes):
        value = {"week_start": "2026-11-05", "available_minutes": 180, "buffer_minutes": 30,
                 "tasks": [{"id": "task-1", "module_id": "M1", "task": "Explain return vs print",
                            "minutes": 30, "reference": "guides/first-semester.md#week-1",
                            "readiness_check": "Predict and change an example"}]}
        value.update(changes)
        return value

    def record(self, **changes):
        value = {"id": "session-1", "date": "2026-11-05", "module_id": "M1",
                 "capability": "python-return-vs-print", "task": "Change a bill-share function",
                 "minutes": 25, "artifact": "study-private/example.py",
                 "evidence": "Predicted values and fixed a changed example",
                 "evidence_source": "learner-report", "assistance": "hints",
                 "understanding": "assisted", "next_action": "Retry a changed input without hints",
                 "review_after": "2026-11-07"}
        value.update(changes)
        return value

    def test_init_is_empty_idempotent_and_private(self):
        before = (self.root / "curriculum/modules.json").read_bytes()
        state = self.store.init()
        self.assertEqual(state["sessions"], [])
        self.assertIsNone(state["plan"])
        self.assertEqual(state["timezone"], "Asia/Kolkata")
        self.assertEqual(state["role_focus"], "undecided")
        first_bytes = self.store.path.read_bytes()
        self.assertEqual(self.store.init(), state)
        self.assertEqual(self.store.path.read_bytes(), first_bytes)
        self.assertFalse(self.store.backup.exists())
        self.assertEqual((self.root / "curriculum/modules.json").read_bytes(), before)
        self.assertEqual(self.store.path, self.root / "study-private/tutor/state.json")

    def test_empty_status_does_not_invent_progress(self):
        self.store.init()
        status = self.store.status("2026-11-05")
        self.assertEqual(status["session_count"], 0)
        self.assertEqual(status["known_minutes"], 0)
        self.assertEqual(status["unknown_minutes_sessions"], 0)
        self.assertIsNone(status["last_next_action"])
        self.assertEqual(status["due_reviews"], [])

    def test_plan_accounts_for_buffer_and_accepts_no_study_week(self):
        self.store.init()
        self.assertEqual(self.store.set_plan(self.plan())["plan"], self.plan())
        with self.assertRaisesRegex(progress.ProgressError, "exceed"):
            self.store.set_plan(self.plan(available_minutes=59))
        self.store.set_plan(self.plan(available_minutes=60))
        empty = self.plan(available_minutes=0, buffer_minutes=0, tasks=[])
        self.assertEqual(self.store.set_plan(empty)["plan"], empty)

    def test_invalid_plan_minutes_are_rejected(self):
        for value in (True, -1, 1.5, float("inf"), float("nan"), "30", None):
            for field in ("available_minutes", "buffer_minutes"):
                with self.subTest(value=value, field=field), self.assertRaises(progress.ProgressError):
                    progress.validate_plan(self.plan(**{field: value}), self.store.module_ids)
        with self.assertRaises(progress.ProgressError):
            progress.validate_plan(self.plan(available_minutes=10081), self.store.module_ids)
        for value in (0, True, -1, 1.5):
            plan = self.plan()
            plan["tasks"][0]["minutes"] = value
            with self.subTest(value=value), self.assertRaises(progress.ProgressError):
                progress.validate_plan(plan, self.store.module_ids)

    def test_duplicate_task_ids_rejected(self):
        plan = self.plan()
        plan["tasks"].append(copy.deepcopy(plan["tasks"][0]))
        with self.assertRaisesRegex(progress.ProgressError, "Duplicate task"):
            progress.validate_plan(plan, self.store.module_ids)

    def test_invalid_dates_and_reverse_review_date_rejected(self):
        for value in ("2026-02-30", "20261105", "2026-1-05", "tomorrow", 20261105):
            with self.subTest(value=value), self.assertRaises(progress.ProgressError):
                progress.validate_plan(self.plan(week_start=value), self.store.module_ids)
            with self.subTest(value=value), self.assertRaises(progress.ProgressError):
                progress.validate_record(self.record(date=value), self.store.module_ids)
        with self.assertRaisesRegex(progress.ProgressError, "precede"):
            progress.validate_record(self.record(review_after="2026-11-04"), self.store.module_ids)

    def test_unknown_and_zero_minutes_are_distinct(self):
        self.store.init()
        self.store.record(self.record(minutes=None))
        self.store.record(self.record(id="zero", minutes=0))
        self.store.record(self.record(id="known", minutes=12))
        status = self.store.status("2026-11-05")
        self.assertEqual(status["session_count"], 3)
        self.assertEqual(status["known_minutes"], 12)
        self.assertEqual(status["unknown_minutes_sessions"], 1)

    def test_invalid_record_minutes_rejected(self):
        for value in (True, False, -1, 2.5, float("nan"), float("inf"), "25"):
            with self.subTest(value=value), self.assertRaises(progress.ProgressError):
                progress.validate_record(self.record(minutes=value), self.store.module_ids)

    def test_idempotent_session_and_conflict_preserve_prior_bytes(self):
        self.store.init()
        self.store.record(self.record())
        before = self.store.path.read_bytes()
        self.assertEqual(len(self.store.record(self.record())["sessions"]), 1)
        self.assertEqual(self.store.path.read_bytes(), before)
        with self.assertRaisesRegex(progress.ProgressError, "different data"):
            self.store.record(self.record(minutes=80))
        self.assertEqual(self.store.path.read_bytes(), before)

    def test_manifest_subset_and_causal_ids_are_used(self):
        for module_id in ("M1", "M6h", "M18-app"):
            progress.validate_record(self.record(module_id=module_id), self.store.module_ids)
        for module_id in ("M19", "M6½", "unknown", [], None):
            with self.subTest(module_id=module_id), self.assertRaises(progress.ProgressError):
                progress.validate_record(self.record(module_id=module_id), self.store.module_ids)

    def test_independent_claim_needs_artifact_and_evidence(self):
        for change in ({"artifact": None}, {"artifact": " "}, {"evidence": ""}, {"evidence": " "}):
            with self.subTest(change=change), self.assertRaises(progress.ProgressError):
                progress.validate_record(self.record(understanding="independent", **change), self.store.module_ids)
        # Validating recorded evidence is not verifying a file or certifying mastery.
        progress.validate_record(self.record(understanding="independent", assistance="none"), self.store.module_ids)

    def test_wrong_shapes_and_enums_are_rejected(self):
        for field, value in (("understanding", "mastered"), ("evidence_source", "inferred"),
                             ("assistance", "unknown"), ("artifact", 2), ("evidence", None),
                             ("task", ""), ("id", []), ("next_action", " ")):
            with self.subTest(field=field), self.assertRaises(progress.ProgressError):
                progress.validate_record(self.record(**{field: value}), self.store.module_ids)
        with self.assertRaises(progress.ProgressError):
            progress.validate_plan(self.plan(tasks={}), self.store.module_ids)

    def test_backup_holds_immediate_previous_valid_state(self):
        self.store.init()
        initial = self.store.path.read_bytes()
        self.store.set_plan(self.plan())
        self.assertEqual(self.store.backup.read_bytes(), initial)
        planned = self.store.path.read_bytes()
        self.store.record(self.record())
        self.assertEqual(self.store.backup.read_bytes(), planned)

    def test_corrupt_state_is_never_silently_reset(self):
        self.store.init()
        for payload in (b"{broken", b"{}", b'{"schema_version":NaN}', b'{"a":1,"a":2}'):
            self.store.path.write_bytes(payload)
            for operation in (self.store.init, lambda: self.store.record(self.record()),
                              lambda: self.store.set_plan(self.plan()), lambda: self.store.status("2026-11-05")):
                with self.subTest(payload=payload), self.assertRaises(progress.ProgressError):
                    operation()
                self.assertEqual(self.store.path.read_bytes(), payload)
            self.assertFalse(self.store.lock_path.exists())

    def test_valid_json_with_corrupt_sessions_is_rejected(self):
        state = self.store.init()
        for change in ({"sessions": [self.record(), self.record()]}, {"schema_version": True},
                       {"schema_version": 9}, {"unexpected": "must not lose this"}):
            invalid = dict(state, **change)
            payload = json.dumps(invalid).encode()
            self.store.path.write_bytes(payload)
            with self.subTest(change=change), self.assertRaises(progress.ProgressError):
                self.store.init()
            self.assertEqual(self.store.path.read_bytes(), payload)

    def test_missing_state_with_backup_requires_manual_recovery(self):
        self.store.init()
        self.store.set_plan(self.plan())
        self.store.path.unlink()
        with self.assertRaisesRegex(progress.ProgressError, "backup exists"):
            self.store.init()

    def test_due_reviews_use_latest_date_per_capability_not_append_order(self):
        self.store.init()
        self.store.record(self.record(id="recent", date="2026-11-08", review_after="2026-11-12", next_action="Recent action"))
        self.store.record(self.record(id="older", date="2026-11-05", review_after="2026-11-07", next_action="Old action"))
        status = self.store.status("2026-11-09")
        self.assertEqual(status["due_reviews"], [])
        self.assertEqual(status["last_next_action"], "Recent action")
        self.assertEqual(len(self.store.status("2026-11-12")["due_reviews"]), 1)
        historical = self.store.status("2026-11-07")
        self.assertEqual(historical["session_count"], 1)
        self.assertEqual(historical["known_minutes"], 25)
        self.assertEqual(historical["due_reviews"][0]["next_action"], "Old action")

    def test_latest_same_day_record_wins_and_null_clears_review(self):
        self.store.init()
        self.store.record(self.record())
        self.store.record(self.record(id="second", review_after=None))
        self.assertEqual(self.store.status("2026-11-12")["due_reviews"], [])

    def test_same_capability_in_different_modules_keeps_separate_reviews(self):
        self.store.init()
        self.store.record(self.record())
        self.store.record(self.record(id="sql", module_id="M8a", review_after=None))
        due = self.store.status("2026-11-12")["due_reviews"]
        self.assertEqual(len(due), 1)
        self.assertEqual(due[0]["module_id"], "M1")

    def test_existing_lock_is_not_removed_or_ignored(self):
        self.store.init()
        self.store.lock_path.write_text("existing owner", encoding="utf-8")
        before = self.store.path.read_bytes()
        with self.assertRaisesRegex(progress.ProgressError, "locked"):
            self.store.record(self.record())
        self.assertEqual(self.store.lock_path.read_text(encoding="utf-8"), "existing owner")
        self.assertEqual(self.store.path.read_bytes(), before)

    def test_atomic_replace_failure_preserves_state_and_releases_lock(self):
        self.store.init()
        before = self.store.path.read_bytes()
        replace = os.replace

        def fail_state(source, destination):
            if Path(destination) == self.store.path:
                raise OSError("simulated replacement failure")
            return replace(source, destination)

        with mock.patch.object(progress.os, "replace", side_effect=fail_state):
            with self.assertRaises(OSError):
                self.store.record(self.record())
        self.assertEqual(self.store.path.read_bytes(), before)
        self.assertFalse(self.store.lock_path.exists())
        self.assertEqual(list(self.store.directory.glob("*.tmp")), [])

    def test_private_symlink_escape_is_rejected(self):
        outside = self.base / "outside"
        outside.mkdir()
        private = self.root / "study-private"
        try:
            private.symlink_to(outside, target_is_directory=True)
        except OSError as exc:
            self.skipTest(f"Symlink creation unavailable: {exc}")
        with self.assertRaisesRegex(progress.ProgressError, "redirected path"):
            self.store.init()
        self.assertEqual(list(outside.iterdir()), [])

    def test_private_file_symlink_is_rejected(self):
        self.store.init()
        outside = self.base / "outside.json"
        outside.write_bytes(self.store.path.read_bytes())
        self.store.path.unlink()
        try:
            self.store.path.symlink_to(outside)
        except OSError as exc:
            self.skipTest(f"Symlink creation unavailable: {exc}")
        before = outside.read_bytes()
        with self.assertRaises(progress.ProgressError):
            self.store.record(self.record())
        self.assertEqual(outside.read_bytes(), before)

    def test_hardlinked_state_is_rejected(self):
        self.store.init()
        outside = self.base / "outside.json"
        try:
            os.link(self.store.path, outside)
        except OSError as exc:
            self.skipTest(f"Hard links unavailable: {exc}")
        before = outside.read_bytes()
        with self.assertRaisesRegex(progress.ProgressError, "Hard-linked"):
            self.store.record(self.record())
        self.assertEqual(outside.read_bytes(), before)

    def test_state_reread_under_lock_preserves_other_writer(self):
        second = progress.Store(self.root)
        self.store.init()
        self.store.record(self.record(id="first"))
        second.record(self.record(id="second"))
        self.assertEqual(self.store.status("2026-11-05")["session_count"], 2)

    def test_cli_round_trip_and_invalid_input_exit_code(self):
        command = [sys.executable, str(SCRIPT), "--root", str(self.root)]
        initialized = subprocess.run(command + ["init"], capture_output=True, text=True, timeout=15)
        self.assertEqual(initialized.returncode, 0, initialized.stderr)
        payload = self.store.directory / "session-input.json"
        payload.write_text(json.dumps(self.record()), encoding="utf-8")
        recorded = subprocess.run(command + ["record", "--file", str(payload)], capture_output=True, text=True, timeout=15)
        self.assertEqual(recorded.returncode, 0, recorded.stderr)
        status = subprocess.run(command + ["status", "--as-of", "2026-11-07"], capture_output=True, text=True, timeout=15)
        self.assertEqual(status.returncode, 0, status.stderr)
        self.assertEqual(json.loads(status.stdout)["known_minutes"], 25)
        bad = subprocess.run(command + ["status", "--as-of", "2026-02-30"], capture_output=True, text=True, timeout=15)
        self.assertEqual(bad.returncode, 2)
        self.assertIn("Invalid as_of", bad.stderr)


if __name__ == "__main__":
    unittest.main()
