[Home](../README.md) · [Module defaults](how-to-read-a-module.md#pick-one)

<a id="sources"></a>
# Sources and evidence

The roadmap combines free lectures, books chosen on merit and reproducible projects. Recommendations are editorial judgments supported by source content, audience fit and independent review; no book or framework is an undisputed winner for every learner.

<a id="evidence-policy"></a>
## Evidence policy

1. **Technical behavior:** use released specifications, official documentation and original papers. Record the revision/date and scope. Draft proposals and SDK behavior are not automatically protocol requirements.
2. **Books:** verify title, authors, edition and legal access with publisher/author pages; cross-check educational fit with university reading lists, substantive specialist reviews or independent comparisons. A publisher endorsement alone is not independent consensus.
3. **Courses:** inspect the actual public syllabus/materials and lecture access. A university degree page is context, not a free course. Do not attribute a roadmap topic to a numbered lecture unless the source supports it.
4. **Quantitative claims:** retain only with population/workload, method, date and limitations. A benchmark, convenience sample or vendor experiment does not establish a universal production rule.
5. **Community evidence:** dated HN/Reddit discussions can reveal differing experiences and candidate resources. Votes, repository stars and trending lists do not prove correctness, suitability or widespread adoption.
6. **Verification status:** separate page content inspected, HTTP response, lab executed, and inferred recommendation. Network failure or bot refusal is unverified access, not proof of a dead page or browser accessibility.

Default lectures are free. Books may be paid, freely available in an authorized edition, or sample/code-only; label these separately. A free trial, certificate, institutional subscription or hosted compute credit is not a universal free entitlement.

## Why these principal books

| Decision | Evidence and limitation |
|---|---|
| Strang for computational linear algebra; CLRS for algorithms | [MIT 18.06 syllabus](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/syllabus/) and [6.006 syllabus](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/) assign these traditions. Map topics to the edition purchased; older lecture page numbers need not match. |
| McElreath for a first applied Bayesian course; BDA/Murphy for depth | [Aalto's BDA course](https://avehtari.github.io/BDA_course_Aalto/index.html) explicitly discusses audience and difficulty, recommends Rethinking and its free lectures; [Jim Albert's review](https://www.tandfonline.com/doi/full/10.1080/10691898.2020.1806761) supplies a separate published assessment. |
| Data-engineering lifecycle plus distributed-systems depth | [Boston University's CS779 syllabus](https://www.bu.edu/csmet/files/2026/06/MET-CS-779-Syllabus-Sum22026O2.pdf) recommends Reis/Housley and DDIA. The [DDIA author release](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html) verifies the 2026 second edition and Chris Riccomini coauthorship. |
| ISLP as classical-ML core; specialist texts when needed | The [author site](https://www.statlearning.com/) gives the Python edition, authors, topic sequence and chapter labs. [HN's reading-list discussion](https://news.ycombinator.com/item?id=42686457) illustrates differing applied/theory preferences; it is not a representative ranking. |
| Bishop/Prince for DL theory; Huyen for application systems | Author/publisher contents distinguish mathematical foundations from application evaluation and operations. [HN discussion](https://news.ycombinator.com/item?id=42686457) independently discusses that distinction; verify chapters against the chosen edition. |

See the [book catalogue](../resources/books.md#books) for exact editions, reading focus and access. Provider pricing and geographic availability are deliberately not frozen into the syllabus.

## Learning-design evidence and its limits

The [learning-experience research record](../audit/learning-experience-research-2026-11-05.md) distinguishes original studies, review findings and design judgment. Retrieval with feedback, revisiting a skill later, and staged worked examples inform the readiness and project materials. They do not establish a universal weekly workload or prove that this roadmap works for every learner.

Use the [six-week pilot](study-pilot.md) to record actual effort, artifacts and friction before changing the plan. A code test proves a tested behavior; a navigation walkthrough checks findability; neither substitutes for a real learner's study evidence. Record AI assistance separately from an independent explanation, debug task or changed-example check.

## Research and course sources

The six strata cite actual course pages from MIT, Harvard, Stanford, Cambridge and IIT Madras, plus author courses and official project documentation. The roadmap is independent and does not imply university endorsement. It selects a core and adds explicitly labeled later topics rather than claiming one university course contains the entire stratum.

Current technical corrections and inspected primary sources are recorded in the [2026-11-05 research record](../audit/research-2026-11-05.md). Test outcomes and per-file coverage are recorded separately in the [overhaul audit](../audit/overhaul-2026-11-05.md).

<a id="citation-key"></a>
## Historical practitioner citation key

Older pages and audit records use the shorthand below. This table preserves those references. The original attribution/description is historical; this pass did not independently rewatch every video or revalidate every timestamp. Use primary documentation for technical claims and the current guides for requirements.

| Cited as | Source | Historical attribution | Earlier use |
|---|---|---|---|
| **Video 1** (= **W1**) | [*How I'd Learn Machine Learning in 2026 (If I Was Starting Over)*](https://www.youtube.com/watch?v=UZ_rK9gzVSc) — Marina Wyss | Senior Applied Scientist, Twitch | The five-phase practical path, the from-scratch NumPy discipline (logistic regression / K-Means / decision tree), the portfolio standard, the *fluency illusion*, and the project archetypes |
| **Video 2** | [*Breaking into AI/ML from a non-technical background*](https://www.youtube.com/watch?v=FeQZmQMffzc) | Applied Scientist, Amazon | The internal locus of control, building for real organisations, interviews-as-data, and the realistic transition timelines |
| **Video 3** | [*The Only 7 Books You Need to Become an AI Engineer*](https://www.youtube.com/watch?v=Pr9oRVtAqCM) | ex-Coursera / ex-Amazon engineer | The AI-Engineer role definition, intuition-over-derivation, the notebook-to-production gap, and the [Practitioner Shelf](../resources/books.md#practitioner-shelf) |
| **Article 1** | [*Best Free Python Courses for Beginners in 2026*](https://scrimba.com/articles/best-free-python-courses-for-beginners-in-2026/) | Scrimba | The [free Python course matrix](../curriculum/1-foundations.md#python-course-matrix), the pairing stack, the Python-2 red flags |
| **Article 2** | [*How to Learn Python — A Beginner's Guide (2026)*](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/) | Scrimba | The four-phase Python pacing structure, milestones, the project ladder, the tutorial-hell protocol |
| **W2** | [*The Only Python You Need to Learn for AI in 2026*](https://www.youtube.com/watch?v=otBkgSZr0no) — Marina Wyss | Senior Applied Scientist, Twitch | The [four Python skill groups](../curriculum/1-foundations.md#python-skill-groups), the [foundations AI rule and 3-check gate](../curriculum/1-foundations.md#ai-usage-rule), the evolving-project idea and [`DECISIONS.md`](portfolio-spine.md#decisions-template) |
| **W3** | [*AI Engineering Roadmap: Projects that Get You Hired*](https://www.youtube.com/watch?v=mGClIHRird8) — Marina Wyss | Senior Applied Scientist, Twitch | The [five-level Portfolio Spine](portfolio-spine.md#levels) and [Level-5 loops](../coursepages/m23-ai-safety/README.md#level-5-loops) |
| **W4** | [*AI Agents Are Not Complicated*](https://www.youtube.com/watch?v=tEORX_PevRM) — Marina Wyss | Senior Applied Scientist, Twitch | The [M22 labs](../coursepages/m22-agentic-ai/README.md#labs) and the [evaluation harness](../coursepages/m24-mlops-llmops-agentops/README.md#evaluation-harness) |
| **W5** | [*How I'd Become an AI Engineer in 2026 (Even with No CS Degree)*](https://www.youtube.com/watch?v=8c8Rrhd2oxo) — Marina Wyss | Senior Applied Scientist, Twitch | Timeline calibration (no stage durations are stated; see [findings §1.1](../audit/v2026.7-research-findings.md#timeline)) |
| **W6** | [*Coding interviews are completely different now*](https://www.youtube.com/watch?v=Do8VuokPbBc) — Marina Wyss | Senior Applied Scientist, Twitch | Interview-format split and the from-scratch algorithms ([findings §1.2](../audit/v2026.7-research-findings.md#interview-prep)) |
| **W7** | [*AI Agents in 38 Minutes — Complete Course*](https://www.youtube.com/watch?v=sNvuH-iTi4c) — Marina Wyss | Senior Applied Scientist (at recording, Amazon) | Multi-agent patterns and topologies ([M22](../coursepages/m22-agentic-ai/README.md#multi-agent-next)) |

## Career and student-program evidence

The [November 2026 career sample](../audit/career-research-2026-11-05.md) records 12 directly inspected employer postings plus official student/program/interview guides. Required, preferred and unstated eligibility are separated; expired leads are excluded or qualified. The [India undergraduate route](india-undergraduate-path.md) uses these as examples of work and eligibility, not a forecast of future demand or sponsorship. Recheck actual openings before applying and refresh a small relevant sample each semester.

## Historical audit records

The older [verification log](../audit/VERIFICATION.md), [v2026.3 audit](../audit/AUDIT_v2026.3.md), [v2026.7 findings](../audit/v2026.7-research-findings.md) and other audit files retain the state and claims of their dates. They do not override current requirements or prove current access. Earlier hiring counts are small, selected samples; earlier proposed diagnostics are non-operational.

A new release records what was changed, inspected, executed and left unverified. The current pass does not claim every historical URL is reachable, every vendor feature was executed, or every book was read cover to cover. Report a wrong or inaccessible resource with the page, date, problem and a verified replacement when available.
