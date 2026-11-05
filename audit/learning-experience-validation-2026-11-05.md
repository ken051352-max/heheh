# Learning-experience validation — 2026-11-05

**Preparation record:** the work was subsequently applied to the original project. See [the current project integration and validation](project-integration-2026-11-05.md) for later corrections, source follow-up and fresh execution there. The results below describe the earlier checkout inspection.

## Delivered work and location

Implemented in the fresh clone `C:\roadmap-sandbox-2026-11-05`, branch `codex/learning-experience-2026-11-05`, based on `6b682e58521b5d6bba8c76e626f218441c455bad`. The prior overhaul was already merged into the default branch. This pass leaves local working-tree changes for review; it did not push, open a PR, merge or deploy.

- One [semester sequence](../guides/first-semester.md#semester-plan) integrates existing onboarding, selected edition-checked reading, movable exam buffers and evidence before dependent work.
- The [beginner kit](../resources/beginner-projects/README.md) supplies calculator/Weather/SQL starters, fixtures, tests and reviewer guidance. Its [SQL query workspace](../resources/beginner-projects/sql/README.md#query-preview) runs before the later ingestion exercises.
- [Readiness and targeted repair](../guides/readiness-checks.md), the [resume tracker](../guides/progress-tracker.md#resume) and a [private six-week pilot](../guides/study-pilot.md#start) connect learning evidence to the next action.
- Entry pages, generated resource/role sections, modules and coursepages now distinguish immediate work from optional breadth. Existing module IDs, prerequisite routes and historical audit bodies are preserved.

See the [complete inventory](learning-experience-inventory-2026-11-05.md), [decision worklog](learning-experience-worklog-2026-11-05.md), [research](learning-experience-research-2026-11-05.md) and [semester source checks](semester-research-2026-11-05.md). These are different forms of evidence, not interchangeable assertions of verification.

## Executed code and integrity checks

The isolated environment uses CPython 3.12.10, pytest 9.2.0, NumPy 2.5.4, scikit-learn 1.9.1, DuckDB 1.5.6 and SQLite 3.49.1 on Windows. Dependencies were installed only in the checkout's ignored environment.

| Check | Actual result |
|---|---|
| Tooling regressions | 40 passed, including generated drift, graph ordering, escaping, atomic marker writes and Markdown/HTTP classification |
| NumPy supplied references | 33 passed with `NPFS_IMPL=reference` |
| Agent contract lab | 21 passed; no model/provider required |
| Causal and event replay labs | 18 passed, including all six DuckDB cases; no skips |
| Beginner supplied references/scaffolds | 70 passed with `BEGINNER_IMPL=reference` after query-preview integration |
| Beginner starter contract | 65 intentional `NotImplementedError` failures, 5 supplied-scaffold checks passed; JUnit inspected, zero setup/import errors |
| Demonstrations | Causal simulation, SQLite and DuckDB replay, calculator, offline Weather and expanded SQL references executed; added SQL preview executed without filling TODOs |
| Failure demonstrations | Calculator division by zero, unsupported Weather city and malformed weather fixture returned the expected failure status |

**182 unique tests passed, zero skipped.** The [execution transcript](learning-experience-tests-2026-11-05.txt) records commands, versions, output, expected exits and the separate integration follow-up. An initial 179-test pass preceded the new three-case preview module; the final beginner suite was rerun after that addition. Unchanged non-beginner suites were not needlessly repeated.

<!-- FINAL INTEGRITY -->
- **1,620 internal links across 70 Markdown files:** zero failures.
- **Manifest:** 27 modules, five subsets and six ordered routes; targets and generated content valid. Manifest contents unchanged.
- **Anchor compatibility:** all 242 original explicit prose anchors preserved; code/comment examples excluded from this count.
- **Review coverage:** 100 original files plus 41 new deliverables, 141 total; no missing disposition. All 17 prior audit files remain unchanged.
- **Diff:** 41 tracked files modified and 41 files added; tracked and new-file whitespace checks pass. Final diff reviewed, including generated sections and reference/starter separation.
<!-- END FINAL INTEGRITY -->

The starter is intentionally incomplete. A reference passing its own assessment does not establish learner mastery; each project requires an independently explained changed example. Existing CI now includes the new project paths/tests, but remote CI was not run for these unpushed changes. Historical migration scripts were read and retained, not executed.

## External sources and access

The [bounded active-resource sweep](learning-experience-external-2026-11-05.md) checked **362 unique URLs: 323 OK, 39 WARN/unverified, zero confirmed 404/410 failures, 13 cross-host redirects**. It used the existing checker with 12 workers and an eight-second request timeout, HEAD followed by GET on failures. Prior audit URLs were excluded from this active refresh. Warnings include TLS/network/disconnection/rate-limit/access failures and remain visible; they were not converted into verified browser access.

A subsequent targeted native-curl follow-up retrieved **33 of those 39 URLs** with certificate validation enabled. It also revealed an empty CS145 directory despite HTTP 200; the curriculum now links a dated course archive with retrieved public slide exports and explicitly restricted/unverified recordings. Nielsen's failing HTTPS book URL was replaced with its retrieved HTTP address. Five resources remain unresolved; the original scan and follow-up observations stay separate in the external report. This is HTTP/content evidence, not a claim of regional video playback.

Research independently inspected consequential lecture access, book title/authors/edition/contents, divergent specialist reviews, learning-design sources, Markdown behavior and SQLite contracts. When extraction failed or omitted needed detail, alternatives included direct official HTML/media requests, author pages, licensed book catalogues and Context7 documentation. SQL lecture MP4 byte sampling proves a retrievable media artifact, not uninterrupted playback. Scrimba's direct metadata/official launch pages declare free access; its interactive account flow was not exercised. The single CS50P default is a sequencing choice, not an inferred claim that Scrimba became paid.

One separately labeled optional live Weather reference request succeeded during project verification. This is a dated provider response, not an uptime measurement; automated tests remain offline. Free provider quotas/terms, regional lecture access and future availability can change.

## Rendering and navigation inspection

Rendered the actual Markdown with GitHub's public Markdown API and inspected a local page wrapper using `github-markdown-css` and headless Microsoft Edge 156.0.4314.58. Thirteen pages were checked at **320, 390 and 1280 CSS pixels**: README, Start Here, semester, Week 0, first month, readiness, tracker, resource defaults, role paths, foundations, classical ML, beginner kit and SQL brief.

- All 39 page/width combinations had no document-wide horizontal overflow and no image missing an alt attribute. Tables and code blocks may scroll inside their own regions; this is not a full accessibility conformance audit.
- Native disclosure keyboard opening/closing worked wherever a disclosure was present. Required first tasks remain outside optional reference disclosures.
- Desktop and narrow screenshots of README, semester and classical ML were visually inspected. Entry actions, heading hierarchy, wrapping and local contents were checked; remaining reference tables are explicitly secondary.
- Nine local browser clicks reached their expected page/anchor, covering the first task, milestone list, week 16, SQL preview, readiness repair, recovery, a single role route, experienced entry and M9.

After the final game-equivalence and resource-access corrections, the four changed reading pages (semester, readiness, statistics/data and books) were rendered again through the same API/wrapper and checked at all three widths: **12 follow-up combinations**, with no document-wide overflow, missing alt attributes or failed tested disclosure interactions. The refreshed 320-pixel semester screenshot was visually inspected. Unchanged code suites were not rerun for these prose/link changes; the internal-link, curriculum and anchor/whitespace checks passed again.

The API returns sanitized HTML with prefixed explicit IDs and without the full GitHub application's heading permalinks. The local wrapper adds navigation aliases and rewrites relative `.md` links for the proxy; original source anchors were separately compared and checked. Local screenshots, raw API HTML and browser measurements are retained in ignored `.research/`, not shipped as a website. External images/media were blocked during this local layout check, so it verifies text/alt fallback and local images rather than third-party badge rendering. A full logged-in GitHub/mobile-device session and screen-reader audit remain unperformed.

## Learner scenarios actually inspected

1. **Complete beginner:** README → Week 0 → public CS50P Lecture 0 link and the concrete greeting edit. No placement, purchase or role selection blocks the first task.
2. **Current student:** semester's early milestone link → current week → specific lecture/practice/check/next. Reading and advanced depth are labeled; the canonical schedule controls pacing.
3. **Project learner:** kit → one project brief → setup/stages → fixture/test paths → assessment/memo. References and learner TODOs remain separate; the SQL preview is runnable before ingestion.
4. **Failed readiness:** relevant check → reviewer notes → named repair lesson/example → changed-case retry. No global belonging/ability score is used.
5. **Returning learner:** tracker → last evidence → short reproduction → a targeted recovery task, preserving unrelated completed work.
6. **Undecided undergraduate:** shared foundations → prerequisite-aware role experiments → one provisional route. Six paths are alternatives; India employment, remote-from-India and relocation remain distinct.
7. **Mobile reader:** entry, semester and representative module inspected at narrow widths; local contents and native disclosure tested. Structural walkthroughs were also independently performed by the verifier.

These are agent proxy inspections, not trials with students. The walkthrough exposed and corrected the SQL scope mismatch, redundant calculator-refactor instruction, overly narrow prior-project waiver and incorrect M7 credit for the SQL preview.

A final independent challenge found one further contradiction: the accepted guessing-game alternative led back to calculator-only Week 5–6 tasks and readiness evidence. Those instructions now preserve the chosen project, with deterministic comparison/error cases and applicable attempt boundaries. The reviewer found no other concrete blocker in the assigned semester/onboarding/readiness/tracker/project briefs. This was a read-only review followed by root integration, not a new learner trial.

## Remaining limits and next action

The six-week log is ready to use; **no six weeks of student study occurred**. Workload estimates and interface choices remain hypotheses to refine from actual observations. Not every book, video minute, vendor integration or historical claim was re-executed/revalidated. The preserved advanced curriculum retains its existing evidence limits; no new labor-market or employment guarantee is made.

The learner's next action is [Week 0's first small task](../guides/week-0.md#week-0-plan), or [M1 equivalence/readiness](../guides/readiness-checks.md#m1-ready) if already programming. Save one artifact and a next-task note, then use actual study feedback to adjust the schedule.
