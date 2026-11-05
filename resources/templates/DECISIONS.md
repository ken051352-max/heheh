# DECISIONS.md: <project name>

> Copy this template into your project. Add one entry per consequential decision, newest first. When a decision changes, add a superseding entry and retain the history. Reviewable evidence may stay private or be selectively shared.
> From the [Portfolio Spine](../../guides/portfolio-spine.md#decisions-template); pattern: [Architecture Decision Records](https://adr.github.io/).

**Current level:** L1 / L2 / L3 / optional L4 / optional L5 · **Updated:** YYYY-MM-DD

## Acceptance criteria and budgets

Define project-specific criteria before evaluation. State the user task and consequence of each failure. The example measurements below do not prescribe a universal score, latency or cost target.

| Criterion | Target and justification | Observation, date and sample size | Method / uncertainty |
|---|---|---|---|
| Task quality and relevant error slices | | | Frozen cases, rubric, baseline and confidence limits where appropriate |
| Critical safety/permission failures | | | Named adversarial regressions and expected denials |
| Latency at specified concurrency | | | End-to-end timing; enough samples before reporting p95 |
| Cost per successful task | | | All attempts, retries, tools and compute; define success |
| Tool calls / total deadline (L3) | | | Measured bounds and timeout/cancellation behavior |

Label each result **measured**, **simulated**, or **estimated**. A mock validates a contract, not model quality. Qualitative user feedback and a reproducible failure trace can be evidence; do not manufacture numeric scores for them.

## Cost and capacity model

```text
model_cost = sum_over_all_attempts(
    input_tokens * input_price_per_million / 1_000_000
    + output_tokens * output_price_per_million / 1_000_000)
total_cost = model_cost + tool_cost + compute_cost + storage_cost
cost_per_success = total_cost / successful_tasks   # undefined if none succeed
monthly_estimate = measured_or_assumed_tasks_per_day * days * cost_per_task
                  + fixed_monthly_costs
```

Record provider/model, currency, price date/source, cached-token or batch rates when applicable, included/excluded costs, task success definition and all assumptions. Local model compute is not a per-token API bill; disclose hardware/runtime even when no cash charge is incurred.

| Scenario | Tasks/day and concurrency | Measured or estimated cost | Latency evidence / untested assumption | Likely limit and next experiment |
|---|---|---|---|---|
| Observed workload | | | | |
| 10× workload hypothesis | | | | |
| 100× workload hypothesis | | | | |

A linear cost estimate is not a load test. Do not extrapolate a measured p95 without testing queuing, rate limits and changed concurrency.

## D-001 · <decision title>

- **Date / level / status:** YYYY-MM-DD · L2 · proposed / accepted / superseded by D-___
- **Context:** User need, relevant constraints, data rights and the problem forcing this decision.
- **Options:** The simple baseline and at least one plausible alternative; compare complexity and failure modes.
- **Decision:** What was selected and why.
- **Evidence:** Link the run, comparison, source, observed failure or user feedback. Include limitations and contrary findings.
- **Consequences:** Benefits, maintenance cost, risks, rollback and the condition that would trigger reconsideration.

## Decisions to record by level

| Level | Evidence to retain |
|---|---|
| L1 | Baseline/model choice, schema + semantic validation, retry/fallback policy, fixture vs real-model results. |
| L2 | Corpus/data rights, retrieval/store choice, chunking and reranking comparisons, frozen evaluation cases. |
| L3 | Tool allowlist, read/write permissions, trusted approval scope, idempotency/replay and step/deadline limits. |
| L4 — optional | Whether multiple agents outperform the single-workflow baseline; topology, context isolation and failure handling. |
| L5 — optional | Objective validity, reward gaming regressions, bounded proposed changes, review and rollback. |

Finish the chosen project's scope. L4/L5 are extensions when evidence justifies them, not prerequisites for a strong portfolio.
