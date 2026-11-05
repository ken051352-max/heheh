[Home](README.md) · [Start here](START-HERE.md) · [FAQ](FAQ.md)

<a id="contributing"></a>
# Contributing

Help readers find a clear route, trustworthy resources and projects they can reproduce. A precise report about one inaccessible lecture or confusing prerequisite is useful.

<a id="tldr"></a>
## Choose a contribution

| Change | How to proceed |
|---|---|
| Dead/moved link or confusing instruction | Use the [issue chooser](https://github.com/ken051352-max/heheh/issues/new/choose); include the file, URL and observed problem. |
| Typo or concrete factual correction | Open a focused pull request with the evidence. |
| Course/book replacement | Apply the [resource bar](#resource-bar), identify what it replaces and update the canonical default when appropriate. |
| Module structure or prerequisite change | Describe affected learners and migration in an [RFC](#rfc), unless the maintainer has already authorized the work. |

<a id="no-setup"></a>
## Reading needs no setup; checks and labs use Python

The roadmap is Markdown with images, Python integrity tools and optional practice labs. Reading requires no installation. Most integrity/contract tests use the standard library; the NumPy harness and optional DuckDB backend have explicit dependencies.

From the repository root:

```text
python tools/check_links.py
python tools/check_curriculum.py --check
python -m unittest discover -s tools/tests -v
python -m unittest discover -s resources/agent-lab/tests -v
python -m unittest discover -s resources/local-labs/tests -v
```

For the numerical suite, install the listed dependencies in an isolated environment and select the reference implementation:

```powershell
python -m pip install -r resources/numpy-from-scratch/requirements.txt -r resources/local-labs/requirements.txt
$env:NPFS_IMPL = 'reference'
python -m pytest resources/numpy-from-scratch/tests -q
Remove-Item Env:NPFS_IMPL
```

In Bash, use `NPFS_IMPL=reference python -m pytest resources/numpy-from-scratch/tests -q`. The learner starter suite intentionally fails until its algorithms are implemented. Report skipped dependencies explicitly. See [tooling](tools/README.md) for supported Markdown syntax, limits and optional HTTP checks.

The [workflow](.github/workflows/check-links.yml) configures push/PR checks and monthly/manual external reports. Passing locally does not demonstrate that a remote workflow has run.

For beginner practice changes, install [the small test dependency](resources/beginner-projects/requirements.txt), then run `BEGINNER_IMPL=reference python -m pytest resources/beginner-projects/tests -q` in Bash, or set `$env:BEGINNER_IMPL = 'reference'` first in PowerShell. Default starter failures are intentional; reference mode must pass. See [project verification](resources/beginner-projects/README.md#tests).

<a id="dead-links"></a>
## Report observed access

Provide the URL, file/module, date and result: missing page, wrong subject, unavailable recording, account/paywall requirement, or technical error. Include a replacement if you inspected it. Do not classify an entire domain as dead from a timeout or assume a 403 means it works in a browser.

<a id="verification-legend"></a>
### Verification legend

| Status | What it establishes |
|---|---|
| OK / ✅ reachable | The endpoint responded successfully at the recorded time. Content, lecture access and edition still need inspection. |
| WARN / ⚠️ unverified | Authentication, blocking/rate limits, server failure or network failure prevented verification. Explain any separate manual result. |
| FAIL / ❌ missing | The endpoint returned 404/410 after the checker's GET retry. Review before replacing. |
| Replaced / 🔁 | A changed destination with documented evidence of subject/access fit. |

Historical audit legends may differ. They describe earlier checks, not current availability. Curriculum symbols are explained in the [FAQ](FAQ.md#symbols).

<a id="resource-bar"></a>
## Resource bar

| Criterion | Required evidence |
|---|---|
| **Free lecture route** | Actual publicly accessible teaching, not a degree page, enrollment-only recording, time-limited trial or paid certificate. Label notes, labs and documentation separately from lectures. |
| **Books chosen on quality, whether free or paid** | Principal books may be paid. Verify title/authors/edition, relevant reading and legal access. Free samples/code are not a free full book. A purchase is not a completion gate; retain a workable free learning route. |
| **Named, checkable source** | Author/publisher, university course, official technical docs or original research. Record the inspected page and date. |
| **Outcome and prerequisite fit** | Explain what the learner should do with it and what background it assumes. A stronger advanced course may be a poor beginner default. |
| **Independent corroboration** | For major recommendations, inspect syllabus use, a substantive specialist review or independent comparison. Separate individual opinions from consensus. |
| **Bounded technical claims** | Use released specifications and qualified benchmarks. Do not turn vendor metrics, repository stars or convenience surveys into universal rules. |

Use the [evidence policy](guides/sources.md#evidence-policy) and [research record](audit/research-2026-11-05.md) as examples. Verify links through both content and access where possible; disclose what remains unverified.

<a id="no-piling-on"></a>
### Keep one clear default

Prefer replacing weaker or inaccessible entries. For a new alternative, explain the audience or gap it serves. Keep targeted reading/project instructions instead of an unranked link collection.

Defaults, principal books, strict/recommended prerequisites and role routes live in [curriculum/modules.json](curriculum/modules.json). Edit that manifest, run `python tools/check_curriculum.py --write`, and review the generated tables. Also update the module/coursepage prose, catalogue and affected guides; the checker cannot verify pedagogical meaning.

<a id="citations"></a>
### Cite what supports the claim

Link primary sources beside technical requirements. Record a source's revision and scope for fast-changing systems. The [historical practitioner key](guides/sources.md#citation-key) preserves old video references; it does not certify that every timestamp has been rechecked. Do not add a precise lecture/topic or benchmark attribution without inspecting it.

<a id="pull-requests"></a>
## Pull requests

1. Work on a branch and preserve unrelated changes.
2. Explain the learner-facing problem, resulting behavior and evidence.
3. Run link/manifest checks. Run the relevant existing tests for changed code; include results and skips.
4. Describe any changed prerequisites, access conditions, local alternatives and migration needs. Add a changelog entry for substantive changes.

<a id="anchors-warning"></a>
### Preserve module IDs and explicit anchors

Do not delete or rename existing `<a id="...">` anchors. Preserve compatibility aliases when moving content. The 27 active module IDs include M6½ and M8a/M8b; 19 and 20 remain vacant because their former content moved to M24/M26. See the [structure explanation](FAQ.md#structure). Review explicit-anchor preservation in addition to the checker, which cannot see external inbound links.

<a id="prose"></a>
### Editing prose

Use concrete outcomes, prerequisites and reviewable evidence. Clearly separate core work from later depth. Artifacts can be private, selectively shared or sanitized public. Avoid compulsory hosting, arbitrary metric gates and promised employment timelines. Historic verbatim migration guarantees apply to those earlier migrations; this release deliberately improves curriculum content.

Keep the [first-semester plan](guides/first-semester.md#semester-plan) as the single early schedule. Preserve existing week anchors, connect project stages to [readiness and remediation](guides/readiness-checks.md#how-to-check), and check beginner, experienced and returning entry paths. Generated resource cards and role sequences come from the existing manifest/checker; do not maintain separate hand-edited copies. Inspect narrow-screen rendering when possible and distinguish a proxy walkthrough from real student feedback.

<a id="changelog"></a>
### Changelog and audits

Record substantive changes in [CHANGELOG.md](CHANGELOG.md). Keep earlier audit bodies as historical evidence and create a dated current report. Distinguish source inspection, HTTP reachability, tests actually executed, mocks and untested integrations.

<a id="rfc"></a>
## Structural proposals

An RFC explains the problem, proposed routes/prerequisites, affected files, alternatives and migration for learners already in progress. Seek maintainer direction before unrequested structural work; existing authorization can cover the implementation. Preserve stable links and avoid requiring learners to restart completed work.

<a id="conduct"></a>
## Conduct

Critique resources and reasoning respectfully. Follow the [Contributor Covenant](CODE_OF_CONDUCT.md). Report concerns through its documented channels.

<a id="licence"></a>
## License

Contributions follow this repository's [CC BY-SA 4.0 license](LICENSE.md). Linked courses, books, datasets, models and third-party code retain their own terms; linking or accessing a resource does not transfer redistribution rights. Do not upload copyrighted book PDFs without authorization.
