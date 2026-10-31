# Repository tooling

| Script | Status | Purpose |
| :--- | :--- | :--- |
| [`check_links.py`](check_links.py) | **Active** | Default mode validates every internal markdown link and `#anchor` in the repo (GitHub slug rules + explicit `<a id>` tags). Run `python3 tools/check_links.py`; it must report **0 failures** before any merge. `--external` (v2026.7) also HTTP-checks external URLs in `curriculum/`, `coursepages/`, `guides/` and `resources/`. It classifies each as OK / WARN (bot-gated 401/403/429) / FAIL, lists cross-host redirects, writes a table with `--report <path>`, and exits non-zero on FAIL only with `--strict-external`. Options: `--paths`, `--workers`, `--timeout`. |
| [`check-links.workflow.yml`](check-links.workflow.yml) | **Ready to install** | GitHub Actions workflow (upgraded in v2026.7). On every push/PR touching markdown or the harness: (1) the internal link check (blocking); (2) the [NumPy-from-scratch](../resources/numpy-from-scratch/README.md) tests run against the `reference/` solutions (`NPFS_IMPL=reference`). Monthly and on demand, it also uploads an external-link report as an artefact (report-only). |
| [`delete-empty-issues.workflow.yml`](delete-empty-issues.workflow.yml) | **Ready to install** | Corrected replacement for `.github/workflows/delete-empty-issues.yml`. The live version's `if:` condition matches a sentence from the deleted OSSU-era RFC template, and its auto-reply is OSSU-branded. This version fires only on genuinely empty issue bodies and replies with links to the four issue forms, `START-HERE.md`, the FAQ and the module guide. |
| [`split_readme.py`](split_readme.py) | Historical (v2026.4 migration) — **do not re-run** | Split the former monolithic 2,236-line `README.md` into `curriculum/`, `guides/`, `resources/` and `CHANGELOG.md` by verbatim line ranges. It expects the pre-split README and a hard-coded `/home/user/webapp` root. |
| [`build_hub.py`](build_hub.py) | Historical (v2026.4 migration) — **do not re-run** | Assembled the v2026.4 hub `README.md` from a `README.md.orig` snapshot, which is **not** in the repository. Since v2026.5 the hub `README.md` is edited directly; re-running this script would fail (missing input) or overwrite the curated hub. |

<a id="install-ci"></a>
## Installing the two workflows (owner, one commit)

The automation token that opens these pull requests is a GitHub App without the `workflows` permission. GitHub refuses any push from it that creates or edits files under `.github/workflows/` (re-confirmed in v2026.7). Install them from your own account:

```bash
git mv -f tools/check-links.workflow.yml .github/workflows/check-links.yml
git mv -f tools/delete-empty-issues.workflow.yml .github/workflows/delete-empty-issues.yml
git commit -m "ci: install link-check + harness workflow and corrected empty-issue workflow"
git push
```

Or do the same in the GitHub web editor: create `.github/workflows/check-links.yml` and paste in the contents of `tools/check-links.workflow.yml`, then overwrite `.github/workflows/delete-empty-issues.yml` the same way. Afterwards, delete the two staged copies and change their rows above to **Active**.

**Verbatim-move guarantee.** During the v2026.4 restructure, each moved section was
diff-verified against its original line range after mechanically un-doing the link-path
rewrites — 13/13 sections matched byte-for-byte. No curriculum prose was altered.
