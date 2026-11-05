"""Offline regressions for the Markdown subset this repository uses."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

SPEC = importlib.util.spec_from_file_location(
    "check_links", Path(__file__).parents[1] / "check_links.py")
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class MarkdownTargets(unittest.TestCase):
    def test_code_comments_and_fences_are_not_links(self):
        text = '''[real](README.md)
`[inline](missing.md)`
````python
[expression](missing.md)
```
<a id="not-an-anchor" href="missing.md">
````
~~~
[tilde](missing.md)
~~~
    [indented](missing.md)
<!-- [comment](missing.md) -->
'''
        self.assertEqual(checker.links_of(text), ["README.md"])

    def test_balanced_parentheses_escaped_destination_and_title(self):
        text = r'''[a](notes_(draft).md "a title") [b](notes_\(draft\).md)'''
        self.assertEqual(checker.links_of(text), ["notes_(draft).md"] * 2)

    def test_angle_destination_and_single_quoted_title(self):
        self.assertEqual(checker.links_of("[a](<My Notes.md#read-me> 'title')"),
                         ["My Notes.md#read-me"])

    def test_reference_full_collapsed_and_shortcut_are_case_insensitive(self):
        text = '''[first][Course Notes] [course notes][] [Course Notes]
[course notes]: <My Notes.md> "notes"
[unused]: missing.md
[ordinary prose]
'''
        self.assertEqual(checker.links_of(text), ["My Notes.md"] * 3)

    def test_html_autolinks_and_nested_image(self):
        text = '''<a href='docs.md'>docs</a><img src="pic.png">
<https://example.com/x?q=1&amp;r=2>
[![logo](logo.png)](README.md)
'''
        self.assertCountEqual(checker.links_of(text), ["docs.md", "pic.png",
                              "https://example.com/x?q=1&r=2", "README.md", "logo.png"])

    def test_escaped_link_opener_is_prose(self):
        self.assertEqual(checker.links_of(r"\[not a link](missing.md)"), [])

    def test_unclosed_fence_hides_remainder(self):
        self.assertEqual(checker.links_of("~~~\n[example](missing.md)\n"), [])


class InternalValidation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def check(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return checker.check_internal(str(self.root))

    def test_encoded_paths_fragments_queries_and_reference_links(self):
        self.write("My Notes.md", "# Section one\n")
        self.write("README.md", '''[notes](My%20Notes.md?view=1#section%2Done)
[again][notes]
[notes]: <My Notes.md#section-one>
''')
        self.assertEqual(self.check(), 0)

    def test_missing_file_and_anchor_are_independent_failures(self):
        self.write("README.md", "# Here\n[a](absent.md) [b](#absent)\n")
        self.assertEqual(self.check(), 2)

    def test_ids_inside_code_do_not_create_anchors(self):
        path = self.write("README.md", '''# Visible
```
<a id="fictional"></a>
# Fictional heading
```
`<a id="also-fictional"></a>`
<span id='real'></span>
''')
        self.assertEqual(checker.anchors_of(path), {"visible", "real"})

    def test_heading_suffixes_do_not_collide(self):
        path = self.write("README.md", "# Foo\n# Foo\n# Foo-1\n# Foo\n")
        self.assertEqual(checker.anchors_of(path), {"foo", "foo-1", "foo-1-1", "foo-2"})

    def test_inline_code_underscores_atx_closer_and_setext(self):
        path = self.write("README.md", "## `some_name` ###\nSecond title\n============\n")
        self.assertEqual(checker.anchors_of(path), {"some_name", "second-title"})

    def test_venv_and_cache_markdown_are_excluded_on_all_platforms(self):
        self.write("README.md", "# Valid\n")
        for directory in ("node_modules", ".venv", ".pytest_cache", ".git"):
            self.write(directory + "/README.md", "[bad](missing.md)\n")
        self.write("custom-python-env/pyvenv.cfg", "home = /some/python\n")
        self.write("custom-python-env/README.md", "[bad](missing.md)\n")
        self.assertEqual(len(checker.markdown_files(str(self.root))), 1)
        self.assertEqual(self.check(), 0)

    def test_empty_fragment_current_page_and_external_schemes(self):
        self.write("README.md", "[top](#) [self]() [mail](mailto:a@example.org) [web](//example.org)\n")
        self.assertEqual(self.check(), 0)


class HTTPClassification(unittest.TestCase):
    def probe_error(self, code, host="example.com"):
        url = "https://" + host + "/resource"
        error = urllib.error.HTTPError(url, code, "test", {}, None)
        with patch.object(checker.urllib.request, "build_opener") as factory:
            factory.return_value.open.side_effect = error
            result = checker.probe(url, timeout=1)
            self.assertEqual(factory.return_value.open.call_count, 2)
            return result[0]

    def test_404_and_410_remain_failures_even_on_bot_gated_hosts(self):
        for code in (404, 410):
            for host in ("example.com", "openai.com", "fakeopenai.com", "www.coursera.org"):
                with self.subTest(code=code, host=host):
                    self.assertEqual(self.probe_error(code, host), "FAIL")

    def test_blocked_rate_limited_and_server_errors_are_unverified(self):
        for code in (401, 403, 405, 429, 500, 502, 503, 999):
            with self.subTest(code=code):
                self.assertEqual(self.probe_error(code), "WARN")

    def test_network_error_is_not_dead_link_evidence(self):
        with patch.object(checker.urllib.request, "build_opener") as factory:
            factory.return_value.open.side_effect = urllib.error.URLError("offline")
            self.assertEqual(checker.probe("https://example.com", 1)[0], "WARN")

    def test_head_rejected_get_succeeds(self):
        url = "https://example.com/resource"
        with patch.object(checker.urllib.request, "build_opener") as factory:
            response = factory.return_value.open.return_value.__enter__.return_value
            response.status, response.geturl.return_value = 200, url
            factory.return_value.open.side_effect = [
                urllib.error.HTTPError(url, 405, "test", {}, None),
                factory.return_value.open.return_value]
            self.assertEqual(checker.probe(url, 1), ("OK", 200, url))


if __name__ == "__main__":
    unittest.main()
