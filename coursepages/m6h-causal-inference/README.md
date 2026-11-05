# Module 6½ — Causal Inference & Experimentation

[Curriculum specification](../../curriculum/2-statistics-and-data.md#module-6-half) · [Learning contract](../../curriculum/README.md#learning-contract)

**Goal:** make an intervention decision with a specified population, treatment, outcome and time horizon. Estimation code does not establish identification assumptions.

## One free route

Use [Brady Neal's free course](https://www.bradyneal.com/causal-inference-course) with [Hernán and Robins, *Causal Inference: What If*](https://miguelhernan.org/whatifbook). The authors provide the book, code and data free; record the revision downloaded. [Facure's Python handbook](https://matheusfacure.github.io/python-causality-handbook/landing-page.html) is an implementation companion.

**Recommended experimentation book:** Kohavi, Tang and Xu's [*Trustworthy Online Controlled Experiments*](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59) (paid, Cambridge 2020), alongside *What If* for identification. Pearl's *Causality* (paid, second edition) and free [MIT 14.387](https://ocw.mit.edu/courses/14-387-applied-econometrics-mostly-harmless-big-data-fall-2014/) are further econometric/theoretical depth. Lectures remain free; books are selected for quality regardless of price.

## Core lab: a known causal effect

Run the [local causal lab](../../resources/local-labs/README.md) on a CPU:

```bash
python resources/local-labs/causal_inference.py
```

The fixture defines potential outcomes with a constant effect and a binary pre-treatment confounder. Compare randomized difference-in-means, confounded difference-in-means and adjustment by the observed confounder. The lab reports known truth, estimates, bias across repetitions, approximate interval coverage and a prospective normal-theory sample size. It needs no dataset, account or network.

**Before running:** write the ATE estimand, assignment mechanism, causal graph, consistency/no-interference assumption, conditional exchangeability assumption and positivity requirement. Explain which are guaranteed by the generator and which would need justification with real data. Refutation checks can reveal problems; passing them does not prove identification.

**Then change the generator:** weaken overlap, hide the confounder or change the noise. Report bias, uncertainty and sample sizes by stratum. Do not extrapolate synthetic performance to a real policy.

## Core experiment design

Write a plan before looking at simulated treatment outcomes:

| Decision | Required record |
|---|---|
| Estimand | Population, assignment/analysis unit, treatment, outcome, time horizon; ATE vs ATT and why |
| Sample size | Baseline variance/rate, MDE, alpha, power, sidedness, allocation and attrition assumptions |
| Validity | Randomization, interference, missingness, sample-ratio mismatch (SRM), instrumentation checks |
| Analysis | Primary metric, interval, multiplicity policy, guardrails and practical decision threshold |
| Stopping | Fixed horizon or a correctly implemented sequential method; no repeated fixed-horizon p-value peeking |

For CUPED, use only pre-treatment information and estimate the adjustment coefficient on a separate pilot or with a documented cross-fitting scheme. Compare variance across repeated trials and evaluate the adjusted estimand. Sample-size savings are design-specific estimates.

## Optional identification extensions

- **Synthetic control:** construct a treated unit and donor pool; select weights using only pre-treatment outcomes; assess pre-fit, post-treatment gaps and placebo units. State no-interference/no-contamination assumptions. Good pre-fit alone does not prove causality.
- **Difference-in-differences:** state parallel-trends and anticipation assumptions; inspect event-time behavior. A nonsignificant pre-trend test does not prove parallel trends.
- **IV or regression discontinuity:** defend exclusion/relevance or continuity assumptions before estimation. Use author-permitted data or a known synthetic generator.
- **Causal ML:** after M9–M12, use [DoWhy](https://www.pywhy.org/dowhy/) or [EconML](https://econml.azurewebsites.net/) with sample splitting and policy evaluation. Predictive accuracy is not an effect-validation metric.

## Done when

Submit a reproducible README, tests for generator/estimand and estimator identities, the pre-analysis plan and a decision memo. Include known-truth comparisons, repeated-trial uncertainty, a failure case and one identification assumption code cannot test. Record seed, sample size, repetitions and versions. A private artifact is sufficient.

## Prerequisites

M5 core and M6. IV, synthetic controls and causal forests are optional deeper projects; ML-dependent extensions require the relevant M9–M12 material.
