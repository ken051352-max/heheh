"""Offline curriculum regressions using isolated Markdown fixtures."""
import json
from pathlib import Path
import tempfile
import unittest

from tools import check_curriculum as checker


class CurriculumIntegrity(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((checker.ROOT / "curriculum/modules.json").read_text(encoding="utf-8-sig"))
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.modules = {node["id"]: node for node in self.data["modules"]}
        self.subsets = {node["id"]: node for node in self.data["subsets"]}
        self.routes = {route["id"]: route for route in self.data["routes"]}
        targets = {}
        for node in self.data["modules"]:
            targets.setdefault(node["path"], set()).add(node["anchor"])
        for node in self.data["subsets"]:
            targets[self.modules[node["parent"]]["path"]].add(node["anchor"])
        for path, anchors in targets.items():
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("\n".join(f'<a id="{anchor}"></a>' for anchor in sorted(anchors)), encoding="utf-8")
        for relative, sections in checker.render_tables(self.data).items():
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            body = "\n".join(f"<!-- BEGIN {name} -->\nold table\n<!-- END {name} -->" for name in sections)
            target.write_text("# Handwritten introduction\n\n" + body + "\n\nHandwritten closing.\n", encoding="utf-8")

    def errors(self):
        return checker.validate(self.data, self.root)

    def assert_error(self, fragment):
        self.assertTrue(any(fragment in error for error in self.errors()), self.errors())

    def test_complete_manifest_has_valid_ordered_routes(self):
        self.assertEqual(self.errors(), [])

    def test_missing_canonical_module_and_reserved_ids_are_rejected(self):
        self.modules["M0"]["id"] = "M19"
        self.assert_error("missing IDs ['M0']; unexpected IDs ['M19']")

    def test_duplicate_nodes_are_not_silently_overwritten(self):
        self.data["modules"].append(dict(self.modules["M1"]))
        self.assert_error("modules: duplicate IDs")

    def test_malformed_schema_returns_errors_without_traceback(self):
        for invalid in (None, [], {"modules": "wrong", "subsets": [], "routes": []}):
            with self.subTest(invalid=invalid):
                self.assertTrue(checker.validate(invalid, self.root))
        self.modules["M1"]["requires"] = "M0"
        self.assert_error("requires must be a list of IDs")

    def test_unknown_dependencies_recommendations_and_route_steps(self):
        self.modules["M1"]["requires"].append("absent-required")
        self.modules["M1"]["recommends"].append("absent-recommended")
        self.routes["analyst"]["steps"].append("absent-step")
        self.assert_error("unknown ID absent-required")
        self.assert_error("unknown ID absent-recommended")
        self.assert_error("unknown step absent-step")

    def test_prerequisite_cycle_reports_the_path(self):
        self.modules["M1"]["requires"] = ["M2"]
        self.assert_error("prerequisite cycle: M1 -> M2 -> M1")

    def test_recommendations_can_point_forward_and_form_a_cycle(self):
        self.modules["M1"]["recommends"] = ["M2"]
        self.modules["M2"]["recommends"] = ["M1"]
        self.assertEqual(self.errors(), [])

    def test_route_prerequisites_must_precede_the_dependent_step(self):
        steps = self.routes["ai-application"]["steps"]
        steps[0], steps[1] = steps[1], steps[0]
        self.assert_error("route ai-application: M8a requires earlier M1")
        self.assert_error("route ai-application: M21 requires earlier M8a")

    def test_missing_transitive_prerequisite_invalidates_later_steps(self):
        self.routes["analyst"]["steps"].remove("M2")
        self.assert_error("route analyst: M5 requires earlier M2")
        self.assert_error("route analyst: M6 requires earlier M5")

    def test_full_parent_supplies_application_and_brief_competence(self):
        steps = self.routes["research"]["steps"]
        steps.insert(steps.index("M18") + 1, "M21")
        steps[steps.index("M25-brief")] = "M25"
        self.assertEqual(self.errors(), [])

    def test_application_subset_does_not_supply_full_parent_competence(self):
        self.modules["M21"]["requires"] = ["M18"]
        self.assert_error("route ai-application: M21 requires earlier M18")

    def test_capstone_requires_an_explicit_conditional_route(self):
        steps = self.routes["ai-application"]["steps"]
        steps[-1] = "M26"
        self.assert_error("choose a conditional M26 subset")

    def test_capstone_subset_prerequisites_are_enforced(self):
        self.routes["ai-application"]["steps"][-1] = "M26-research"
        self.assert_error("M26-research requires earlier M6")

    def test_research_capstone_does_not_impose_deep_learning_on_every_question(self):
        self.routes["research"]["steps"] = ["M1", "M2", "M5", "M6", "M25-brief", "M26-research"]
        self.assertEqual(self.errors(), [])

    def test_subset_parent_must_be_a_known_full_module(self):
        self.subsets["M18-app"]["parent"] = "M18-missing"
        self.assert_error("unknown parent module M18-missing")

    def test_missing_file_and_subset_anchor_are_reported(self):
        self.modules["M1"]["path"] = "curriculum/absent.md"
        self.subsets["M18-app"]["anchor"] = "absent-anchor"
        self.assert_error("missing file curriculum/absent.md")
        self.assert_error("missing anchor curriculum/6-frontier-production.md#absent-anchor")

    def test_repository_escape_is_rejected(self):
        self.modules["M1"]["path"] = "../outside.md"
        self.assert_error("path must be a repository-relative Markdown file")

    def test_source_urls_must_be_http_and_only_capstone_may_be_empty(self):
        for value in ("", "javascript:alert(1)", "https:///missing-host", "https://example.org/a b", "https://example.org:bad"):
            with self.subTest(value=value):
                self.modules["M1"]["default_url"] = value
                self.assert_error("M1.default_url: expected an http(s) URL")
        self.modules["M1"]["default_url"] = "https://example.org/course?session=1#topic"
        self.modules["M1"]["book_url"] = "file:///book.pdf"
        self.assert_error("M1.book_url: expected an http(s) URL")

    def test_generated_drift_fails_and_write_preserves_surrounding_prose(self):
        self.assertEqual(len(checker.sync_tables(self.data, self.root)), 3)
        self.assertEqual(checker.sync_tables(self.data, self.root, write=True), [])
        self.assertEqual(checker.sync_tables(self.data, self.root), [])
        guide = self.root / "guides/practitioner-track.md"
        text = guide.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# Handwritten introduction\n\n"))
        self.assertTrue(text.endswith("\n\nHandwritten closing.\n"))
        self.assertIn("[M6½](../curriculum/2-statistics-and-data.md#module-6-half)", text)
        self.assertIn("[M18 application foundations](../curriculum/6-frontier-production.md#application-foundations)", text)
        before = guide.read_bytes()
        self.assertEqual(checker.sync_tables(self.data, self.root, write=True), [])
        self.assertEqual(guide.read_bytes(), before)
        self.modules["M1"]["book"] = "A changed recommendation"
        self.assertTrue(any("MODULE DEFAULTS table drift" in error for error in checker.sync_tables(self.data, self.root)))

    def test_missing_or_duplicate_markers_prevent_all_writes(self):
        guide = self.root / "guides/practitioner-track.md"
        original = guide.read_text(encoding="utf-8")
        other = self.root / "guides/how-to-read-a-module.md"
        before = other.read_bytes()
        for modified in (original.replace("<!-- END ROLE ROUTES -->", ""), original + "<!-- BEGIN ROLE ROUTES -->"):
            with self.subTest(modified=modified):
                guide.write_text(modified, encoding="utf-8")
                errors = checker.sync_tables(self.data, self.root, write=True)
                self.assertTrue(any("exactly one ordered ROLE ROUTES marker pair" in error for error in errors))
                self.assertEqual(other.read_bytes(), before)
                self.assertEqual(guide.read_text(encoding="utf-8"), modified)

    def test_write_preserves_windows_newlines_outside_generated_bodies(self):
        guide = self.root / "guides/practitioner-track.md"
        guide.write_bytes(guide.read_text(encoding="utf-8").replace("\n", "\r\n").encode("utf-8"))
        self.assertEqual(checker.sync_tables(self.data, self.root, write=True), [])
        actual = guide.read_bytes()
        self.assertTrue(actual.startswith(b"# Handwritten introduction\r\n\r\n"))
        self.assertTrue(actual.endswith(b"\r\n\r\nHandwritten closing.\r\n"))
        self.assertEqual(checker.sync_tables(self.data, self.root), [])

    def test_book_labels_escape_markdown_table_syntax(self):
        self.modules["M1"]["book"] = "Book [edition] | reference"
        table = checker.render_tables(self.data)["guides/how-to-read-a-module.md"]["MODULE DEFAULTS"]
        self.assertIn(r"Book \[edition\] \| reference", table)


if __name__ == "__main__":
    unittest.main()
