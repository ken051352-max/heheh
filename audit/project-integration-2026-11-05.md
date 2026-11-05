# Original-project integration and final corrections — 2026-11-05

## Active result

The working project is **`C:\.orkas\userWorkSpace\chat-2026-11-03-1\repo`**. Integration and the checks below ran on **`codex/roadmap-overhaul-2026-11-05`**, based on `cbb6afc01ff5b91f5647a9040e2b73cc838f7b8e`, after the user requested applying the work here. The user subsequently requested a pull request; publication is prepared on **`codex/learning-experience-pr-2026-11-05`**, based on default-branch commit `6b682e58521b5d6bba8c76e626f218441c455bad`. That commit has the same starting file contents. The results below are local validation; subsequent publication and remote CI status belong to the pull request.

Before applying, all 100 tracked files were compared with the reviewed checkout's base `6b682e58521b5d6bba8c76e626f218441c455bad`. Their content matched after text line-ending normalization, with no conflicting tracked work. Applied 41 modified files and 41 additions; all 141 reviewed deliverables then matched the prepared result. Existing versions of replaced files were backed up privately under `.git/codex-learning-experience/before/`. The existing `opencode.jsonc` was verified unchanged without copying its content into a deliverable. Follow-up changes described below were made directly in the original project.

## Delivered learning experience

- One [first-semester sequence](../guides/first-semester.md) integrates Week 0 and the first month, selected book reading, adjustable pacing, exam buffers and recovery. Free lectures remain the default; paid books are welcome and optional to purchase.
- The [beginner kit](../resources/beginner-projects/README.md) provides calculator, offline Weather and SQLite starters, separate references, synthetic fixtures, meaningful failure tests and reviewer guidance. Query/join practice precedes full SQL ingestion work.
- [Readiness checks](../guides/readiness-checks.md), prior-study evidence and the tracker govern dependent work. The accepted guessing-game alternative now remains valid through subsequent refactoring/testing milestones.
- A [private six-week study pilot](../guides/study-pilot.md) collects actual pacing and friction observations. No student study results have been fabricated.
- GitHub Markdown navigation, module entry actions, optional depth, resource defaults and six role routes are integrated. The manifest and original explicit anchors remain the compatibility baseline.

The [file inventory](learning-experience-inventory-2026-11-05.md) covers the deliverables individually. Earlier [research](learning-experience-research-2026-11-05.md), [worklog](learning-experience-worklog-2026-11-05.md) and [checkout validation](learning-experience-validation-2026-11-05.md) remain preparation evidence; the executed checks here are separate.

## Additional corrections and evidence

1. **Data Engineer operations route:** the route allowed M24 entry with a pipeline, but M24's core and M26's systems artifact required a model service. M24/coursepage/M26 now explicitly accept a CLI/container pipeline with quality/reconciliation gates, replay safety, lineage, completion/freshness budgets and an executed recovery drill. All 12 production requirements remain. ML/AI projects retain their model-quality, safety and applicable GenAI evidence. An independent reviewer rechecked the corrected route and found the contradiction resolved; the module manifest and prerequisites did not need changing.
2. **Retry-safe task design:** [Apache Airflow best practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#creating-a-task), inspected through Context7 and retrieved directly, explain transaction-like task outputs, consistent replay, fixed input partitions and avoiding duplicate inserts. These support the pipeline assessment. No Airflow installation or integration execution is claimed, and scheduler-specific APIs are not imposed.
3. **Lion attribution:** the deep-learning topic map incorrectly credited “Chesterton.” Direct retrieval of [Chen et al., *Symbolic Discovery of Optimization Algorithms*](https://arxiv.org/abs/2302.06675) verified the title, author metadata, February 2023 date and abstract introducing Lion. Corrected the attribution and linked the primary paper. Exa reached its rate limit during this research; native retrieval succeeded with normal certificate checks.
4. **Visualization scope:** Observable Plot is now explicitly an optional JavaScript choice, with local HTML/npm use, alongside optional Python plotting alternatives. The default remains Matplotlib/Seaborn. [Official getting-started documentation](https://observablehq.com/plot/getting-started) and Context7 `/observablehq/plot` support local use. Removed incidental Plotly/Altair major-version labels; learners pin the compatible version they actually use.
5. **Environment hygiene:** added `.venv-local-labs/` to Git exclusions because the existing lab README explicitly creates that directory. Existing private configuration, environments, caches and personal study logs stay outside deliverables.

## Remaining-source follow-up

The [earlier scan and alternate-client follow-up](learning-experience-external-2026-11-05.md) remain dated observations. The five sources still unresolved at that stage were subsequently inspected through Exa:

| Source | What was actually inspected | Decision and limit |
|---|---|---|
| [Observable Plot](https://observablehq.com/plot/) | Documentation on marks/scales/transforms; getting-started and Context7 corroborate JavaScript/local use | Retain as optional. Earlier direct-client 429 remains an access limitation, not proof of a paywall. |
| [Columbia statistics blog](https://statmodeling.stat.columbia.edu/) | Substantive November 4, 2026 discussion of statistical practice | Retain as optional individual/community discussion; not consensus. Direct-client 403 is not relabeled as browser success. |
| [Stanford CS103](https://web.stanford.edu/class/cs103/) | Current course content, linked proof lecture and condensed slides; native GET also succeeded (200, 32,284 bytes) | Public written-material description is supported; recordings are on Canvas. |
| [Gibbs–Candès adaptive conformal paper](https://proceedings.neurips.cc/paper_files/paper/2021/file/0d441de75945e5acbc865406fc9a2559-Paper.pdf) | Abstract/introduction through extraction; native GET completed all 845,022 PDF bytes, including terminal EOF, with a 30-second timeout | Retain qualified long-run coverage wording; no automatic conditional/horizon-specific guarantee. Earlier partial transfer is preserved as history. |
| [Jim Albert's book review](https://www.tandfonline.com/doi/full/10.1080/10691898.2020.1806761) | Substantive praise and criticism of *Statistical Rethinking*: applied modeling/exposition, theoretical limits and software dependence | Supports a qualified recommendation, not universal superiority. Direct-client 403 remains distinct from alternate content inspection. |

No source was replaced merely because a tool failed. The previously corrected empty CS145 directory and Nielsen HTTPS failure are included in the applied changes. Three endpoints above still have unresolved ordinary direct-client access; all five yielded content through an alternate route. This does not verify every minute of lecture playback or every regional/account flow.

## Executed validation in this project

A fresh ignored `.venv` uses CPython 3.12.10, pytest 9.2.0, NumPy 2.5.4, scikit-learn 1.9.1, DuckDB 1.5.6 and SQLite 3.49.1. Installed the three repository requirements files without changing global packages.

| Suite | Result |
|---|---|
| Tooling regressions | 40 passed |
| NumPy reference implementations | 33 passed |
| Agent contracts | 21 passed |
| Causal/SQLite/DuckDB labs | 18 passed |
| Beginner references/scaffolds | 70 passed |

**182 tests passed, zero skipped.** Also executed the causal, SQLite, DuckDB, calculator, offline Weather, full SQL and query-preview demonstrations in this project. Invalid calculator/Weather inputs produced their expected nonzero exits. Starter mode yielded 65 intentional `NotImplementedError` failures and five supplied-scaffold passes; JUnit inspection found zero setup/import errors or skips. The [fresh transcript](project-integration-checks-2026-11-05.txt) records commands and actual outputs. Reference execution is not evidence of learner mastery.

### Final source integrity and reading walkthroughs

- **1,639 internal links across 71 Markdown files:** zero failures after the final route link was added.
- **Manifest and generated content:** 27 modules, five subsets and six ordered routes pass; manifest contents unchanged. The Data Engineer correction reconciles prose with an already permitted route, so no prerequisite migration is required.
- **Compatibility and coverage:** all 242 original explicit prose anchors preserved; all 17 original audit bodies unchanged; all 143 deliverable files have an individual disposition. Tracked and new-file whitespace checks pass.
- **Exclusions:** private configuration, `.venv`, beginner/local-lab environments, runtime cache and private study records are ignored. Temporary inspection dependencies and images remain under ignored `.research/`.
- **Rendering:** rendered the actual original-project Markdown through GitHub's Markdown API and used a local CSS wrapper with headless Edge 156.0.4314.58. Eighteen pages at 320, 390 and 1280 CSS pixels produced 54 page/width checks, with no document-wide overflow, missing alt attributes or failed tested disclosure interactions. The final pipeline-list/role-link changes were rechecked on their two affected pages at all three widths.
- **Visual inspection:** original-project screenshots of the narrow README, semester and new pipeline-operations section were inspected. The pipeline paragraph was split into correctness, lineage, operations and recovery bullets after the initial narrow screenshot exposed a dense block.
- **Navigation:** 12 browser clicks reached the expected page/anchor: beginner task, milestone index, week 16, SQL preview, readiness repair, recovery, one role route, prior-programming evidence, M9 and the three paths into the pipeline contract. Together with the content review, these cover the seven requested learner scenarios without restarting completed work.

These are agent inspections, not student trials. The wrapper rewrites local Markdown links and supplies aliases for API-prefixed/missing heading IDs; source anchors were checked independently. External media was blocked during layout inspection. Tables/code may scroll internally. This is not a full GitHub application, physical-device or screen-reader conformance audit. The temporary local preview server was stopped after inspection.

## Limits and learner next action

This implementation is reviewable locally. Remote CI, publication, full browser access to every external resource, screen-reader conformance and a real six-week student pilot are not claimed. Workload estimates should change with actual study observations. Current employer examples inform practice and eligibility questions; they do not predict hiring at graduation.

Start with [Week 0's small program](../guides/week-0.md#week-0-plan), or [M1 equivalence/readiness](../guides/readiness-checks.md#m1-ready) if already programming. Save one artifact and an exact next-task note before adding another course.
