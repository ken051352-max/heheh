# Learning experience implementation — 2026-11-05

This is a new implementation record. Earlier audit bodies remain historical.

## Scope and starting point

- Fresh sandbox clone of `https://github.com/ken051352-max/heheh.git`.
- Base: `6b682e58521b5d6bba8c76e626f218441c455bad` (prior overhaul merged).
- Working branch: `codex/learning-experience-2026-11-05`.
- Primary learner: first-year BTech CSE/AI in India, role undecided; free lectures, books selected on quality.
- No existing website application was found in the tracked tree; GitHub Markdown is the product being improved.

## Checklist

- [x] Clone and inspect existing work; establish separate file ownership.
- [x] Review all tracked files individually and relevant new files; inspect images visually.
- [x] Research consequential lecture, reading, assessment and interface choices.
- [x] Implement one semester sequence integrated with existing onboarding.
- [x] Add runnable beginner projects and independent readiness checks.
- [x] Implement a private six-week study log and revision process.
- [x] Integrate entry, tracker, module and career navigation.
- [x] Run fresh checks, references, demos, external checks and learner walkthroughs.
- [x] Review final diff, anchor compatibility and complete inventory.

## Decisions and changes to the initial direction

1. Preserve the merged curriculum overhaul and its manifest rather than recreate it. The new work addresses use of the roadmap: sequencing, practice and feedback. Advanced content will be retained when review finds it coherent.
2. Keep the existing Week 0 and weeks 1–4 anchor identities, with one canonical semester schedule. A calendar milestone is not proof of full-module completion.
3. Use local standard-library exercises where adequate. A Weather CLI can be assessed with fixtures and mocked transport; a SQL investigation can start with SQLite before PostgreSQL-specific plan analysis in full M8a.
4. Reduce overloaded onboarding: three Week 0 apps plus full problem sets and additional exercises did not fit the stated beginner budget defensibly. Use CS50P through orientation and the first semester; selected practice establishes roadmap outcomes, while the course's certification has its own full requirements. Scrimba remains optional; its public free-access declaration was recovered through direct HTML, so this change is not an inferred paywall claim.
5. Replace wide generated default-resource and role tables with stacked sections. Preserve the manifest, six routes and all generation marker names; keep compact prerequisite tables. No prerequisite or module-ID migration is required.
6. Correct active support links inherited from another fork. Historical audits keep their original destinations and observations.
7. Integration review found that the proposed two-week SQL preview accidentally required the full ingestion/transaction kit before its design/writing lessons. Add a supplied in-memory query workspace; weeks 15–16 now assess filtering and joins. Keep ingestion, payment reconciliation and plans in the subsequent M8a investigation. This corrects a prerequisite mismatch without discarding useful later work.
8. A final alternative-client access check recovered 33 scanner warnings but exposed an empty CS145 directory. Replace it with the inspected Fall 2020 slide archive and label its Canvas recordings separately. Use Nielsen's retrieved public HTTP book address after its HTTPS certificate failed; preserve unresolved access limits in the reports.
9. An independent final challenge found that the accepted guessing-game alternative reverted to calculator-only tasks in Weeks 5–6. Preserve either starter through the same learning outcomes, with explicit deterministic game cases, applicable attempt boundaries and changed-example evidence. No second project is imposed.

## Navigation evidence and limits

- [GitHub formatting documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) was searched and its heading, relative-link and anchor rules inspected. Stable explicit anchors and descriptive relative links remain the navigation convention.
- [GitHub collapsed-section documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections) was fetched. It supports native `details`/`summary` with Markdown separated by blank lines. Required tasks stay visible; optional reference maps can be folded. This is a documented feature, not evidence that this particular interface is usable for every learner.
- [W3C reflow guidance](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) was fetched. It explains the 320-CSS-pixel criterion and the two-dimensional content exception. It motivates reducing table-heavy reading; it does not establish WCAG compliance for the repository.
- The actual Markdown was rendered through GitHub's public Markdown API, then inspected in a local wrapper using `github-markdown-css` and headless Edge. API HTML, screenshots and temporary rendering dependencies stay in ignored `.research/`. The validation record distinguishes this proxy from the full GitHub application, regional lecture playback and screen-reader testing.
- SQLite's [query-only PRAGMA](https://www.sqlite.org/pragma.html#pragma_query_only) was inspected by direct HTTP section extraction after Exa returned only the page introduction. It blocks ordinary data changes but is not a fully read-only security boundary. The query workspace uses it against accidental edits to an in-memory teaching database, with an executed rejection test.

Workload estimates and interface choices are planning judgments. Source inspections, code execution and proxy walkthroughs are recorded separately in the validation record; no student trial has occurred.
