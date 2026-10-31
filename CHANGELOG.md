[🏠 Roadmap home](README.md)

---

<a id="refresh-log"></a>
# 🗓️ Refresh Log

Each pass records what changed, what was verified, and what was deliberately left alone. Full HTTP status logs live in [`audit/VERIFICATION.md`](audit/VERIFICATION.md); per-pass reports live in [`audit/`](audit/).

<a id="v2026-7"></a>
### v2026.7 — AI Engineering Spine · 2026-10-27

**Diagnosis addressed:** v2026.6 fixed the entry ramp, but the middle and advanced layers hadn't caught up with the four 2026 Marina Wyss videos (W1–W4, see [sources](guides/sources.md#citation-key)). Python had no AI-engineering scope or rule for AI coding assistants. The fast lane named the NumPy-from-scratch stage but gave no way to check it. Portfolio projects were separate pieces, not one growing system. M22 described agents without labs. Evals were scattered. CI workflows were staged but never installed. Every source and number below is recorded in **[`audit/v2026.7-research-findings.md`](audit/v2026.7-research-findings.md)**.

| Change | Detail |
| :--- | :--- |
| **[Python skill groups](curriculum/1-foundations.md#python-skill-groups)** | M1 scoped to the four AI-engineering groups (W2): core data and control flow · HTTP/JSON APIs and error handling · file and log I/O · `venv`/`uv` isolation. Beginner-sized version in [first 30 days](guides/first-30-days.md#skill-groups), plus an optional keyless-API [JSON micro-task](guides/first-30-days.md#week-4-json) in Week 4. |
| **[AI usage rule + 3-check gate](curriculum/1-foundations.md#ai-usage-rule)** | During the foundations phase AI may only explain and quiz. You unlock coding assistants by passing a [read · debug · data-flow gate](curriculum/1-foundations.md#three-check-gate). After the gate: spec-driven prompting, auditing AI-written tests, and code review. Linked from START-HERE, the first 30 days and the tracker. |
| **[NumPy From Scratch sprint](curriculum/3-classical-ml.md#numpy-sprint)** | A 3-step sequence before `.fit()`: visual maths map (2–4 weeks max) → algorithm map → logistic regression, K-Means and a decision tree in NumPy. New **[harness](resources/numpy-from-scratch/README.md#numpy-from-scratch)**: `starter/` stubs, `reference/` solutions and 17 `pytest` tests, with optional sklearn agreement. CI runs the tests against the reference solutions to prove them. |
| **[Portfolio Spine](guides/portfolio-spine.md#portfolio-spine)** (new) | One real problem grown through five levels: L1 API + schema output → L2 RAG + evals → L3 read-only-first ReAct agent → L4 router/worker/checker → L5 self-improving loop (optional). Exit criteria per level, plus a mandatory **[`DECISIONS.md`](resources/templates/DECISIONS.md)** with a 1×/10×/100× cost and latency table. Wired into the Four-Year Plan (P5/P7), the fast lane (Stages 4–5), the README track row and the tracker. |
| **[M22 labs](coursepages/m22-agentic-ai/README.md#labs)** | Lab 1 raw ReAct loop · Lab 2 `SKILL.md` (Agent Skills spec, Supabase skills) · Lab 3 constrained decoding (Outlines/guidance vs `instructor` retries vs native structured outputs) · Lab 4 LangChain's write/select/compress/isolate, with *Lost in the Middle*, the 46-vs-19-tool result and a [compounding-error box](coursepages/m22-agentic-ai/README.md#compounding-errors) ($0.95^{10}\approx60\%$, $0.95^{20}\approx36\%$). MCP spec updated to 2026-07-28. |
| **[Evaluation harness](coursepages/m24-mlops-llmops-agentops/README.md#evaluation-harness)** | A 4-part harness in M24: 20–50-case golden failure set · code graders + human-calibrated LLM judge · N-run pass rates · token and cost regression telemetry. Includes a licence-checked free stack (Promptfoo, Inspect AI, Ragas, DeepEval, Langfuse; Phoenix labelled ELv2). Applied to RAG in [M21](coursepages/m21-rag-vector-dbs/README.md#evaluation-harness) and to safety and [Level-5 reward hacking](coursepages/m23-ai-safety/README.md#level-5-loops) in M23 (Karpathy `autoresearch`, DeepMind, METR, Anthropic). |
| **Link freshness** | [`tools/check_links.py --external`](tools/README.md) added. First full pass: 343 external URLs → 11 FAIL, 8 fixed (MIT OCW 18.01A/18.01/18.06/18.S096, Princeton COS 597G, *How to Prove It*, *What If*, Angrist–Krueger) plus moved-domain updates (BlueDot, LangChain, LlamaIndex, Inspect, Ragas). Three textbook hosts time out from the sandbox and are left for a manual re-check. Report: [`audit/v2026.7-external-links.md`](audit/v2026.7-external-links.md). |
| **CI and config** | [`tools/check-links.workflow.yml`](tools/check-links.workflow.yml) upgraded: internal links + NumPy harness on every push, plus a monthly external report. **Still staged, not live:** the automation token was refused write access to `.github/workflows/` (`workflows` permission), so the owner must install it with one commit, as must the corrected [empty-issue workflow](tools/delete-empty-issues.workflow.yml) (steps in [`tools/README.md`](tools/README.md#install-ci)). `CNAME` (`ds.ossu.dev`) deleted, since Pages isn't enabled. `build_hub.py`/`split_readme.py` documented as historical, because their `README.md.orig` input no longer exists. |
| **Citation key** | W1–W7 added to [`guides/sources.md`](guides/sources.md#citation-key). Video 1's title corrected. |

**Deliberately unchanged:** module numbering, existing module projects, all timeline estimates (the "realistic timeline" follow-up video states no stage durations; see [findings §1.1](audit/v2026.7-research-findings.md#timeline)), the free-first policy, and "Open Week 0" as the only beginner instruction.

<a id="v2026-6"></a>
### v2026.6 — First 30 Days · 2026-10-13

**Diagnosis addressed:** a first-year CS student who was a complete Python beginner could not start Week 0/1. Onboarding gave three conflicting first steps (START-HERE: CS50P; the Foundations matrix: Scrimba → Automate → CS50P; the four-year plan: a 15-question diagnostic + all of CS50P + Missing Semester + M0b + 30 LeetCode + accounts, all in week 1). The diagnostic it required had never been written. The Scrimba link had silently redirected to a LangChain.js course. The first project was a Week 9–14-level task. **No rigour was deleted:** advanced material was moved into collapsible "Advanced / later" blocks, with text and anchors preserved.

| Change | Detail |
| :--- | :--- |
| **[`guides/week-0.md`](guides/week-0.md#week-0)** (new) | 7 days × 45–60 min, Scrimba *Learn Python* (c03) only. Daily task table with a "done when" column, retrieval warm-ups, a 15-minute bad-day fallback, an implementation-intention prompt, and Day 7 = rebuild PayUp from memory and share it. Says plainly: no diagnostic, GitHub, tracker or track choice yet. Includes a cited **[Why this design](guides/week-0.md#why-this-design)** note. |
| **[`guides/first-30-days.md`](guides/first-30-days.md#first-30-days)** (new) | Week 1: CS50P L0 + PS0 in cs50.dev, first repo `python-journey`. Week 2: CS50P L1 + Khan Precalculus course challenge (placement only) + 3Blue1Brown EoLA 1–3. Weeks 3–4: CS50P L2–3, five named Exercism exercises, first original mini project. Each week: goal, hours, ≤ 4 done-when boxes and a "math meets code" micro-task. |
| **[`START-HERE.md`](START-HERE.md)** | The only beginner instruction is **Open Week 0**. Other rows kept for Week-0 finishers, experienced, four-year-plan and returning learners. All 15 anchors preserved. README and FAQ pointers aligned. |
| **[Four-Year Plan S1](guides/four-year-plan.md#s1)** | Week 0 Scrimba → Weeks 1–10 CS50P. Maths placement moved to week 2 and made non-gating. DSA deferred to week 5 (after CS50P L3). LinkedIn/Codeforces accounts moved to week 4. Starter project before the weather CLI. Exit check now starts with "Week 0 done". |
| **[`curriculum/1-foundations.md`](curriculum/1-foundations.md#new-here)** | Calm 5-line "Start here if you're new" box. Fear copy, the Math Maturity Operating Manual, Modern Python Tooling, Lean, Axler and Boyd moved into `<details>`. Honest [maths placement](curriculum/1-foundations.md#math-diagnostic) replaces the unsupplied diagnostic. New [beginner maths track](curriculum/1-foundations.md#beginner-math-track). M0b reduced to *Book of Proof* ch. 1–4 at 15 min/day; the 200-exercise gate became a recommended target. Math Academy labelled paid/optional. Course matrix and pairing stack updated. New [M1 starter project](curriculum/1-foundations.md#m1-starter-project) before the [weather-CLI capstone](curriculum/1-foundations.md#m1-capstone). |
| **[Progress tracker](guides/progress-tracker.md#starter-tracker)** | 12-box starter tracker on top, a one-line daily log and a real [resume](guides/progress-tracker.md#resume) section. The full tracker is collapsed, verbatim. |
| **[Stuck or unmotivated?](guides/how-to-read-a-module.md#stuck-or-unmotivated)** | 10 symptom → 15-minute action rows. |
| **Link fixes** | Scrimba `learn-python-c02t` (now redirects to LangChain.js) → `learn-python-c03`. Helsinki `programming-24` → `programming-26` (the 2026 edition). Dead MIT 18.01A exam link flagged. 32 pre-existing broken internal anchors repaired (`#resume`, `#reading-order`, `#module-default-1`, `#known-limitations`, six stratum anchors). [`tools/check_links.py`](tools/check_links.py): **0 failures**. Every added or changed external URL is logged in [`audit/VERIFICATION.md`](audit/VERIFICATION.md#v2026-6-first-30-days). |

**Deliberately unchanged:** module numbering, the module projects, the free-first policy, and all advanced curriculum prose (moved, not deleted). No new compulsory course was added beyond Scrimba for Week 0.

### v2026.5 — Clear Path · 2026-08-30

**Diagnosis addressed:** first-time readers could not tell **what to do**. Feedback from students reading the repo cold produced three complaints: it was unclear whether this was software to install or a document to read; the entry points offered ~35 competing starting choices before any action; and each module's long resource list read as a mandatory to-do list rather than as link-rot insurance. No curriculum content was rewritten in this pass — every change is navigational, explanatory, or a factual correction.

| Change | Detail |
| :--- | :--- |
| **[`START-HERE.md`](START-HERE.md)** | New single entry point, linked from the top of the README. States plainly that there is no software to install, reduces the whole repository to **one** decision ("can you already write Python loops and functions?"), and gives a day-1-to-day-7 plan. |
| **[`guides/how-to-read-a-module.md`](guides/how-to-read-a-module.md)** | Explains module anatomy and what each resource label obliges you to do. Contains the **[Pick-One table](guides/how-to-read-a-module.md#pick-one)** — one default free course pre-chosen for all 27 modules, extracted from the existing `Primary Course Link` lines — plus a worked example of reading M9 correctly (total consumed: one course, three chapters, one project). |
| **[`FAQ.md`](FAQ.md)** | Answers the recurring structural questions: why the module numbers skip 19 and 20, the true module count, realistic timelines, and a full **symbol legend** (✅ ⚠️ ❌ 🔁 ⏭ 📦 ⚡ 🩺 + stratum colours) that previously existed only in this changelog and `audit/`. |
| **[`guides/sources.md`](guides/sources.md)** | 39 citations of the form *"Video 1 (05:05)"* appeared across 10 files with no key anywhere in the repo. All are now resolvable to full URLs, with a note on reading practitioner interviews as testimony rather than research. |
| **README first screen** | Removed the pre-content navigation clutter. Added a "what this is in 30 seconds" table, a prominent pointer to `START-HERE.md`, and an explicit warning that resource lists are **a menu, not a to-do list**. "Start here" became "Entry points by experience" (anchor preserved); the file map is now tiered, ending with *maintainer material — safe to ignore as a learner*. |
| **Stratum pages** | A one-line "reading this page" note added to all six curriculum pages, pointing at the Pick-One table and the citation key. |
| **Factual corrections** | Four reader-facing references to the non-existent **M19** repaired (three in [`resources/books.md`](resources/books.md), one in [`curriculum/1-foundations.md`](curriculum/1-foundations.md)) — they now point at M24 and the M21–M24 range. The version badge, which read `2026.3` while this log read `v2026.4`, is now generated to match. |
| **Community health files** | [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) (Contributor Covenant v2.1) added, per [GitHub's community-health guidance](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors). `CONTRIBUTING.md` documents the resource bar (free-first, named source, replaces-rather-than-adds), the ✅/⚠️/❌/🔁 verification legend actually used in `audit/`, and why module numbers are never recycled. |
| **Issue templates** | The inherited RFC template still described "the current OSSU Curriculum" and linked to `ossu/data-science`. Replaced with four **YAML issue forms** — dead link, resource change, *something was confusing*, and RFC — plus a `config.yml` chooser pointing at `START-HERE.md`, the FAQ, and the module guide. The empty-issue workflow keyed off a sentence in the deleted template, so it needed correcting too; because the automation token cannot write to `.github/workflows/`, the fixed version ships as [`tools/delete-empty-issues.workflow.yml`](tools/delete-empty-issues.workflow.yml) for one-step manual install (see [`tools/README.md`](tools/README.md)). |
| **Link integrity** | All internal links and anchors re-verified with [`tools/check_links.py`](tools/check_links.py) — 0 failures. |

**Deliberately unchanged:** module sequencing, prerequisites, the free-first policy, all curriculum prose, and the vacant M19/M20 numbering.

### v2026.4 — Readable Repo · 2026-08-18

**Diagnosis addressed:** the roadmap's content was strong but delivered as a single 2,236-line, ~300 KB `README.md` — overwhelming on first contact and slow to render. No curriculum text was rewritten in this pass; content was **moved verbatim** and only link paths were mechanically rewritten.

| Change | Detail |
| :--- | :--- |
| **Hub README** | Root `README.md` reduced to a ~160-line landing page: hero, goal, who-this-is-for, start-here, track chooser, a "where everything lives" map, curriculum-at-a-glance, and acknowledgements. |
| **`curriculum/`** | Six stratum pages (`1-foundations.md` … `6-frontier-production.md`) carrying all 27 module specs, plus a [`curriculum/README.md`](curriculum/README.md) index listing every module and the project-enforcement rule. Every page has home/prev/next breadcrumbs. |
| **`guides/`** | [Practitioner fast lane](guides/practitioner-track.md), [companion curricula](guides/companion-curricula.md), [career operations](guides/career-operations.md), and the [progress tracker](guides/progress-tracker.md) as standalone pages. |
| **`resources/`** | [Books + Practitioner Shelf](resources/books.md) and the [production toolchain](resources/toolchain.md). |
| **`CHANGELOG.md`** | The refresh log moved here from the README (this file). |
| **Link integrity** | All internal links (including `coursepages/` and `audit/` cross-references) were rewritten to the new locations and verified by [`tools/check_links.py`](tools/check_links.py) — 0 failures across every `.md` file. A ready-to-install CI workflow ships as [`tools/check-links.workflow.yml`](tools/check-links.workflow.yml) (see [`tools/README.md`](tools/README.md) for the one-step install). |
| **Tooling** | The split itself was performed by [`tools/split_readme.py`](tools/split_readme.py) and [`tools/build_hub.py`](tools/build_hub.py), committed for auditability; a byte-level diff verified all 13 moved sections match the original text exactly after un-doing the mechanical link rewrites. |

### v2026.3 — Practitioner's Pass · 2026-07-30

**Diagnosis addressed:** the curriculum was academically strong but theory-first and intimidating — no practitioner entry point, no enforced project-per-module, no career-reality layer, and no distinct "AI Engineer (Applications)" identity of the kind the 2026 market hires for.

| Workstream | Change | Primary evidence |
| :-- | :--- | :--- |
| **A** | [🚀 Practitioner Track (Fast Lane)](guides/practitioner-track.md#practitioner-track) — a sequenced 6-stage / 6–9-month path; the [track table](README.md#choose-your-track) split into **AI Engineer (Applications)** and **AI Engineer (Systems/Research-adjacent)**; ⚡ **Intuition-First Alternative** callouts added to [M0](curriculum/1-foundations.md#module-0), [M2](curriculum/1-foundations.md#module-2), [M3](curriculum/1-foundations.md#module-3), [M5](curriculum/1-foundations.md#module-5), each stating what you give up and when to come back | Video 1 (00:44–01:09, 03:00–07:15); video 3 (00:53, 04:47) |
| **B** | [Module 1](curriculum/1-foundations.md#module-1) rebuilt around a four-phase pacing structure with ship-milestones, a [free Python course matrix](curriculum/1-foundations.md#python-course-matrix) (8 courses), the recommended pairing stack, the **tutorial-hell escape protocol**, and a disciplined AI-assistant policy naming the **fluency illusion** | Both Scrimba articles; video 1 (03:00–04:00, 09:30); video 3 (01:21) |
| **C** | [Module-project enforcement rule](curriculum/README.md#module-projects) + **18 new 📦 Module Project blocks** so every module M1–M25 now carries a mandatory deliverable with tests, README, and a results memo | Video 1 (05:40–06:05, 10:45–14:05); video 2 (11:30) |
| **D** | [🧭 Career Operations](guides/career-operations.md#career-operations) appendix and the [skills ↔ job-description mapping](guides/career-operations.md#skills-checklist) grounded in **16 live 2026 postings** | Video 2 (04:30–18:40); 16 Greenhouse postings, surveyed 2026-07-26 |
| **E** | [🧰 Practitioner Shelf](resources/books.md#practitioner-shelf) — the applied seven-book canon added alongside (not instead of) the Tier 1 academic spine | Video 3 (full); publisher/author pages |
| **F** | [Minimum Production Bar](curriculum/6-frontier-production.md#production-bar) (12 items) in M24 + toolchain; the [prompting vs RAG vs fine-tuning ladder](curriculum/6-frontier-production.md#module-21) in M21; prompt-injection security and agent eval pipelines promoted to first-class topics in [M22](curriculum/6-frontier-production.md#module-22); Streamlit added and agent-framework pins refreshed in the [toolchain](resources/toolchain.md#toolchain) | Video 1 (07:15, 10:45–12:30); video 3 (05:52); surveyed postings (evaluation in 6/7 AI-Eng roles) |
| **G** | Audit trail, TOC, progress tracker, version badge, `coursepages/` sync, and this log | [`audit/AUDIT_v2026.3.md`](audit/AUDIT_v2026.3.md) |
| **H** | **Visual pass** — a hero banner, a six-stratum journey infographic, and a section banner for each stratum, all in one consistent dark-navy visual language. Every asset is licence-clean: two are model-generated originals, six are rendered deterministically by [`assets/make_banners.py`](assets/make_banners.py), which is committed so any banner can be regenerated or restyled. No third-party or stock imagery is used. Provenance in [`assets/README.md`](assets/README.md) | Trailing brief instruction to match the presentation quality of [microsoft/Data-Science-For-Beginners](https://github.com/microsoft/Data-Science-For-Beginners) |

**Sources consumed in full**

* **Video 1** — [How to Become an ML Engineer](https://www.youtube.com/watch?v=UZ_rK9gzVSc) (Senior Applied Scientist, Twitch) — five-phase practical path, from-scratch NumPy discipline, portfolio architecture standard, the fluency illusion, project archetypes.
* **Video 2** — [Breaking into AI/ML from a non-technical background](https://www.youtube.com/watch?v=FeQZmQMffzc) (Applied Scientist, Amazon) — internal locus of control, real-projects-for-real-organisations, interviews-as-data, realistic transition windows.
* **Video 3** — [The Only 7 Books You Need to Become an AI Engineer](https://www.youtube.com/watch?v=Pr9oRVtAqCM) (ex-Coursera / ex-Amazon) — the AI Engineer role definition, intuition-over-derivation, notebook-to-production progression, the seven-book canon.
* **Article 1** — [Scrimba: Best Free Python Courses for Beginners in 2026](https://scrimba.com/articles/best-free-python-courses-for-beginners-in-2026/) ✅
* **Article 2** — [Scrimba: How to Learn Python — A Beginner's Guide (2026)](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/) ✅
* **Job market** — 16 live postings from public Greenhouse boards (Anthropic, Scale AI, Figma, Databricks, Cloudflare, Discord, Airtable), surveyed 2026-07-26. Enumerated in [`audit/AUDIT_v2026.3.md`](audit/AUDIT_v2026.3.md).

**Verification summary:** 70 URLs HTTP-checked · **66 ✅ 200** · **3 ⚠️ 403** (bot-gated, browser-accessible: two O'Reilly product pages, BLS) · **0 ❌ dead links shipped**. Four candidate URLs were found broken during research and are **not** in the README: two No Starch Manga Guide path guesses, the per-title StatQuest URLs, and `bytebytego.com/courses/generative-ai-system-design-interview`. Framework versions re-pulled from the PyPI JSON API on 2026-07-30.

**Corrections made to previously-published claims** (found while verifying, not part of any workstream's remit):

| Location | Was | Verified actual | Evidence |
| :-- | :--- | :--- | :--- |
| M1 Required Reading | _Fluent Python_ "3rd Edition, 2025" | **2nd Edition (2022)**; a 3rd edition is not published | [fluentpython.com](https://www.fluentpython.com/) ✅ states "Fluent Python, Second Edition"; matches Tier 1 row 20 |
| M1 Required Reading | _Python Crash Course_ "4th Edition, 2025" | **3rd Edition**; no 4th edition exists | [No Starch catalogue](https://nostarch.com/python-crash-course-3rd-edition) ✅ lists 3rd Ed. as current |
| Practitioner Shelf P7 | Source video credits Alex Xu & Sahn Lam | **Alex Xu, Ali Aminian, Hao Sheng** | [Publisher announcement](https://blog.bytebytego.com/p/our-new-book-generative-ai-system) ✅ |
| Toolchain agents row | smolagents 1.24.0 · LangGraph 1.1.9 | **smolagents 1.26.0 · LangGraph 1.2.10** | PyPI JSON API, 2026-07-30 |

**Deliberately not changed:** the Tier 1 / Tier 2 reading lists, the module numbering scheme (including the M6½ and M8a/M8b splits and the M19/M20 gap), and the mathematical content of M0, M2, M3, M5, M9–M12, M13, and M15. The practitioner doctrine is added **alongside** the academic spine as a labelled alternative route, never as a replacement — where the two conflict, both are stated with their conditions.

### v2026.2 and earlier

See [`audit/FINAL_AUDIT.md`](audit/FINAL_AUDIT.md), [`audit/VERIFICATION.md`](audit/VERIFICATION.md), and [`audit/IMPROVEMENT_SPEC.md`](audit/IMPROVEMENT_SPEC.md) for the P1–P5 verification passes that established the 27-module structure, the free-first resource policy, and the link-verification conventions (✅ live · ⚠️ bot-gated · ❌ dead · 🔁 fixed-with-alternative) used throughout.

---

[🏠 Roadmap home](README.md)
