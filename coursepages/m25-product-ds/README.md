[Home](../../README.md) · [Curriculum index](../../curriculum/README.md) · [Resume](../../guides/progress-tracker.md#resume)

# Module 25 — Product DS, Business, Communication & Storytelling

**First task:** Name the audience and decision, then hand-check the numerator and denominator of one metric on a tiny cohort.

[Check prerequisites](#entry-prerequisites) · [Start the lab](#start-lab) · [Completion evidence](#completion)

This page supports the linked module; it is not an additional course to finish. Optional extensions come after the core artifact.

[Full module](../../curriculum/6-frontier-production.md#module-25) ·
[Early application product brief](../../curriculum/6-frontier-production.md#product-brief)

<a id="entry-prerequisites"></a>
## Prerequisites and default route

M6 + M7 for the full module; M6½ before causal-impact claims. Modeling experience is useful when
the decision involves predictions, but descriptive product analysis does not require a model.
The early M25-brief subset defines user needs and acceptance criteria after M1 without claiming
statistical or causal competence.

| Resource | Role and access |
|---|---|
| [Storytelling with Data public videos](https://www.storytellingwithdata.com/videos) | Free lecture/video route; paid workshops and premium archives are separate |
| [Ron Kohavi's ExP papers](https://exp-platform.com/) | Free experimentation evidence and pitfalls |
| [Shneiderman's visualization paper](https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf) | Primary visualization framework |
| Cole Nussbaumer Knaflic — *Storytelling with Data* | Recommended main communication book; paid |
| Kohavi, Tang & Xu — *Trustworthy Online Controlled Experiments* | Recommended main experimentation book; paid, shared with M6½ |
| [Locally Optimistic](https://locallyoptimistic.com/) | Practitioner perspectives; assess advice against the project context |

Books are chosen for quality. Free videos/papers and the local project provide a route without
purchasing a book; a library subscription must not be assumed. Company interview formats vary, so
the project demonstrates a decision-making skill rather than promising a universal interview loop.

<a id="start-lab"></a>
## 📦 Required project — explain a metric change and recommend a decision

Use one of your datasets or a labeled synthetic scenario, such as seven-day retention falling by
three percentage points. State the audience, decision owner and action available to them.

1. **Define the metric:** numerator, denominator, unit of analysis, exposure/cohort, time window,
   inclusion rules, missing events and timezone. Write a small test that checks a hand-worked cohort.
2. **Diagnose:** inspect instrumentation changes, denominator mix, segments, seasonality and timing.
   Distinguish evidence from hypotheses; do not interpret a before/after change as causal proof.
3. **Build the metric tree:** one outcome metric, measurable input metrics and guardrails. Explain
   how a proxy can improve while the user's outcome deteriorates.
4. **Recommend:** quantify plausible value/cost with uncertainty and sensitivity. State the decision,
   what evidence would reverse it, and the next experiment. Causal claims need an estimand,
   identification assumptions and the M6½ analysis; label a proposed experiment as proposed.
5. **Communicate:** one-page memo plus a short readout (video, narrated slides or accessible written
   equivalent). Include one chart chosen for the decision, not a gallery of every analysis.
6. **Review:** obtain peer/mentor/stakeholder feedback when available, or run a documented rubric
   review. Record the revision and unresolved objection; never invent stakeholder endorsement.

<a id="completion"></a>
## Completion rubric

| Criterion | Pass evidence |
|---|---|
| Decision clarity | Named audience, actionable choice, baseline and reversal condition |
| Metric validity | Reproducible cohort/denominator checks; relevant segments and uncertainty |
| Inference discipline | Descriptive, predictive and causal claims distinguished; assumptions explicit |
| Communication | Main recommendation first, readable chart, limitations and guardrails |
| Reviewability | Executable analysis/tests, README, data provenance, memo/readout and revision note |

All five criteria must be met. Unsupported ROI or causal impact cannot compensate for a polished
presentation. A defensible recommendation to collect more evidence or stop an idea is a valid result.
Private, selectively shared, and sanitized public artifacts are all acceptable.

**Optional depth:** a preregistered experiment analysis plan; sequential/multiple-experiment
pitfalls; decision-theoretic threshold selection; a fairness or user-wellbeing tradeoff; or a
stakeholder decision log after a real pilot. These extend the same artifact rather than creating
three unrelated portfolio projects.


---

**After the core:** record the artifact, remaining gap and next task in the [tracker](../../guides/progress-tracker.md#resume), then return to your [chosen route](../../guides/practitioner-track.md#role-pathways). Revisit only the missing skill with the [readiness pattern](../../guides/readiness-checks.md#how-to-check).
