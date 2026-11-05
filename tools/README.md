# Repository tooling

| Script | Status | Purpose |
| :--- | :--- | :--- |
| [`check_links.py`](check_links.py) | **Active** | Dependency-free internal file/anchor validation; see supported syntax below. External mode reports reachability separately from content verification. |
| [`check_curriculum.py`](check_curriculum.py) | **Active** | Standard-library validation of the canonical module manifest, prerequisite graph, ordered role routes and generated guide tables. |
| [`.github/workflows/check-links.yml`](../.github/workflows/check-links.yml) | **Active configuration** | Pushes/PRs touching Markdown, tools or the practice harness run internal checks, offline checker regressions and the NumPy reference suite. Monthly/manual runs upload an external-link report. Local checks do not establish that a remote workflow has run. |
| [`delete-empty-issues.workflow.yml`](delete-empty-issues.workflow.yml) | **Historical staged copy** | The corrected empty-body condition and roadmap-specific reply are now in the active [workflow](../.github/workflows/delete-empty-issues.yml). Retained because historical audit entries refer to this staged file. Edit the active file for future changes. |
| [`split_readme.py`](split_readme.py) | Historical (v2026.4 migration) — **do not re-run** | Split the former monolithic 2,236-line `README.md` into `curriculum/`, `guides/`, `resources/` and `CHANGELOG.md` by verbatim line ranges. It expects the pre-split README and a hard-coded `/home/user/webapp` root. |
| [`build_hub.py`](build_hub.py) | Historical (v2026.4 migration) — **do not re-run** | Assembled the v2026.4 hub `README.md` from a `README.md.orig` snapshot, which is **not** in the repository. Since v2026.5 the hub `README.md` is edited directly; re-running this script would fail (missing input) or overwrite the curated hub. |

<a id="install-ci"></a>
## Running the checks

Run the offline checks after curriculum or tooling changes:

```bash
python tools/check_links.py
python tools/check_curriculum.py --check
python -m unittest discover -s tools/tests -v
python -m unittest discover -s resources/local-labs/tests -v
python -m unittest discover -s resources/agent-lab/tests -v
# Bash; use the PowerShell equivalent below on Windows.
NPFS_IMPL=reference python -m pytest resources/numpy-from-scratch/tests -q
```

```powershell
$env:NPFS_IMPL = 'reference'
python -m pytest resources/numpy-from-scratch/tests -q
Remove-Item Env:NPFS_IMPL
```

Install the [practice dependencies](../resources/numpy-from-scratch/requirements.txt) if needed. The starter suite intentionally fails until the learner implements the algorithms; reference mode validates the supplied solutions.

## Curriculum manifest and generated tables

Edit [`curriculum/modules.json`](../curriculum/modules.json) to change a default course, principal book, declared prerequisite or role sequence. Run `python tools/check_curriculum.py --write`, review the generated table changes, then run the checks above. Only the `MODULE DEFAULTS`, `ROLE ROUTES` and `PREREQUISITES` marker bodies in the two guides are generated; surrounding prose stays handwritten. Missing or duplicate markers prevent writes. The default `--check` mode exits unsuccessfully if tables drift from the manifest.

The checker enforces the 27 canonical module IDs, the five named subsets, six role routes, known dependencies, acyclic strict prerequisites, existing module/subset anchors and HTTP(S) source URL syntax. Each route must provide a prerequisite before the dependent step. Full M18 supplies M18 application competence and full M25 supplies product-brief competence; completing a subset does not imply completing its full parent. Capstones must name a conditional research, systems or applied route. Recommendations can point forward and do not block routes. M24's evaluated-project prerequisite remains prose because it can come from any relevant project; its quality and other learning outcomes require human review. URL syntax validation does not check external availability.

## Supported Markdown and limitations

The internal checker recognizes inline links/images with balanced parentheses, angle-wrapped destinations, single-line reference definitions (full, collapsed and shortcut references), HTML `href`/`src`, explicit HTML IDs, ATX/Setext headings and deduplicated heading slugs. It decodes URL-escaped paths/anchors, ignores query strings for local file resolution, and excludes `.git`, virtual environments, caches and `node_modules` on Windows and Unix.

Fenced backtick/tilde code, indented code, inline code and HTML comments are excluded. The scanner is a maintained subset rather than a complete CommonMark renderer: complex nested list/blockquote markup, multiline reference destinations, embedded HTML blocks and renderer-specific heading extensions need manual review. Put navigation anchors explicitly in `<a id="stable-name"></a>` and keep curriculum links outside code examples. Tests in [`tests/test_check_links.py`](tests/test_check_links.py) cover the supported cases.

## External evidence

For an intentional source refresh, run:

```bash
python tools/check_links.py --external --report audit/external-links.md
```

Defaults cover the active root guides, curriculum, course pages, guides, resources, tooling and asset documentation. Historical audit URLs are not refreshed by default; include `--paths audit` to inspect that history separately. Use `--paths`, `--workers` and `--timeout` to narrow or bound a check.

- **OK:** the endpoint responded successfully at the recorded check time. Inspect the destination to verify subject, edition and access conditions.
- **WARN:** blocked/rate-limited, a server outage or a network failure. Accessibility remains unverified; retry or review manually. A warning is not proof that a link works in a browser.
- **FAIL:** the server returned 404/410 after retrying with GET. Review the result before replacing the resource; no host receives a blanket exemption.

External mode is report-only unless `--strict-external` is set. Cross-host redirects are listed for review. Neither an HTTP success nor passing code tests establish that every curriculum claim is true or that a course is free to complete.

**Verbatim-move guarantee.** During the v2026.4 restructure, each moved section was
diff-verified against its original line range after mechanically un-doing the link-path
rewrites — 13/13 sections matched byte-for-byte. No curriculum prose was altered.
