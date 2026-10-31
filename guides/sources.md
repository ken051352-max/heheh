[🏠 Roadmap home](../README.md) · [🧭 Start here](../START-HERE.md)

---

<a id="sources"></a>
# 🔗 Sources & citation key

Some pages in this curriculum cite evidence in a shorthand form such as **"Video 1 (05:05)"** or
**"video 3 (04:47)"**. This page is the key that resolves that shorthand. Bookmark it if you read the
practitioner-track material.

---

<a id="citation-key"></a>
## The citation key

| Cited as | Source | Who says it | Used to support |
| :--- | :--- | :--- | :--- |
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
| **Job-market survey** | 16 live postings on public Greenhouse boards (Anthropic, Scale AI, Figma, Databricks, Cloudflare, Discord, Airtable), surveyed 2026-07-26 | — | The [skills ↔ job-description mapping](career-operations.md#skills-checklist) and the two AI-Engineer track rows |

The timestamp in a citation — `(05:05)` — is the point in that video where the claim is made, so you can
check it yourself rather than taking this repository's word for it.

---

## How to read these citations critically

The videos are **practitioner testimony, not research.** Where a W-video cites a paper or benchmark, the v2026.7 pages link the primary source directly ([findings §2](../audit/v2026.7-research-findings.md#w4-sources)). They are cited because they are specific,
verifiable, and internally consistent with each other — not because they are authoritative.

Where the practitioner doctrine conflicts with the academic doctrine, **this curriculum states both and
names the trade-off** rather than choosing. The two clearest examples:

| Question | Practitioner position (videos) | Academic position (this roadmap's spine) | Where the conflict is documented |
| :--- | :--- | :--- | :--- |
| Do I need to derive the maths? | No — intuition suffices for applied work (video 3, 04:47) | Yes — you cannot verify a claim you cannot derive | The ⚡ **Intuition-First** callouts in [M0](../curriculum/1-foundations.md#module-0), [M2](../curriculum/1-foundations.md#module-2), [M3](../curriculum/1-foundations.md#module-3), [M5](../curriculum/1-foundations.md#module-5) |
| How long does this take? | 9–18 months to employable | 24–36 months for the complete path | [Honest timeline](practitioner-track.md) and [FAQ § time](../FAQ.md#how-long) |

**Neither column is wrong.** They measure different finish lines. The practitioner numbers measure
*employability in an applied role*; the academic numbers measure *the complete curriculum including the
proof spine and capstone*. Pick the finish line you actually want before you pick the timeline.

---

## Academic sources

The curriculum's syllabi are synthesised from publicly-available university course pages. The complete
list, with links, is in the [Acknowledgements](../README.md#acknowledgements) — IIT Madras, Harvard, MIT,
Cambridge, Stanford, UC Berkeley, CMU, UMich, Hugging Face, Microsoft, and Anthropic.

All university material remains © its respective institution. This repository cites and organises
publicly-disclosed syllabi; it does not reproduce course content.

---

## Verification trail

Every external link in this repository is HTTP-checked before release. The logs live in
[`audit/`](../audit/):

| File | What it contains |
| :--- | :--- |
| [`audit/VERIFICATION.md`](../audit/VERIFICATION.md) | The full per-URL status table across all passes |
| [`audit/AUDIT_v2026.3.md`](../audit/AUDIT_v2026.3.md) | The v2026.3 pass report |
| [`audit/FINAL_AUDIT.md`](../audit/FINAL_AUDIT.md) | Earlier consolidated audit |
| [`audit/raw_http_checks.txt`](../audit/raw_http_checks.txt) | Raw curl output |

Symbols used next to links throughout the repo are defined in [FAQ § symbols](../FAQ.md#symbols).

> **Corrections are logged, not silently applied.** When verification finds that a previously-published
> claim was wrong, the correction is recorded in [`CHANGELOG.md`](../CHANGELOG.md#refresh-log) with the
> evidence. Four such corrections are on record, including two book editions that were cited a version
> ahead of what actually exists.

---

[🏠 Roadmap home](../README.md) · [🧭 Start here](../START-HERE.md) · [❓ FAQ](../FAQ.md) · [🗓️ Changelog](../CHANGELOG.md)
