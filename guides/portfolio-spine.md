[Home](../README.md) · [Role pathways](practitioner-track.md)

<a id="portfolio-spine"></a>
# The Portfolio Spine: one evolving application

Build one system for a concrete problem and improve it through measured releases. Start after full [M1 core completion](../curriculum/1-foundations.md#m1-capstone) and the [independent-understanding checks](../curriculum/1-foundations.md#three-check-gate). The [first-semester Python projects](first-semester.md) are the earlier starting point; this application sequence comes later. Levels 1–3 form a useful application route; levels 4–5 are optional experiments. A deterministic workflow or retrieval-only system can be the right final design.

<a id="pick-a-problem"></a>
## Choose a problem and data you may use

A study assistant over public course rules, a support helper over synthetic orders or a search tool over an open-source manual are suitable examples. You can be the user. Document source/license and scope; there is no need to prove the data were absent from model training. Synthetic or private review fixtures are acceptable when the limitation is stated.

<a id="levels"></a>
## Releases and evidence

<a id="level-1"></a>
### L1: model boundary

A small local script/service with one task and a typed input/output contract.

**Evidence:** Deterministic baseline, fixed examples, schema checks plus semantic checks, explicit refusal/error handling, README and memo. Use [M18-app](../curriculum/6-frontier-production.md#application-foundations).

<a id="level-2"></a>
### L2: retrieval

Add document retrieval only when needed.

**Evidence:** A frozen 20–50-case teaching set with source evidence, no-retrieval and lexical baselines, retrieval metrics, citation/answer assessment and failure slices. Use [M21](../coursepages/m21-rag-vector-dbs/README.md).

<a id="level-3"></a>
### L3: bounded tools

Start with a deterministic workflow; compare one model-controlled loop.

**Evidence:** Allowlists and validation enforced in code, trusted confirmation for destructive actions, idempotency, timeout/step/retry bounds, traces and repeated-task outcomes. Use [M22](../coursepages/m22-agentic-ai/README.md#labs).

<a id="level-4"></a>
### L4: multiple agents, optional

Split work only if a measured bottleneck warrants it.

**Evidence:** Same evaluation workload and budgets as L3, context/permission boundaries, injected worker failures and a before/after quality-cost-latency comparison. Keeping L3 is a valid result.

<a id="level-5"></a>
### L5: proposed improvements, optional research

A sandboxed agent proposes and tests a limited change.

**Evidence:** Frozen scorer/test data outside agent write access, held-out evaluation, audit trail and human review of any accepted change. Use [M23 experiments](../coursepages/m23-ai-safety/README.md#level-5-loops).

**Module mapping:** L1 covers the M18 application subset, not the M1 Weather CLI or full M18 training project. L2 can cover M21. L3 plus the actual MCP SDK lab can cover M22. M23 needs its threat-model and regression evidence; merely adding a checker agent is insufficient. M24 needs the complete [production bar](../curriculum/6-frontier-production.md#production-bar), regardless of the chosen level. Map evidence explicitly before marking a module complete.

<a id="level-rules"></a>
## Rules at every release

1. Keep one repository and a commit/tag per milestone. Storage and review can be private.
2. Build an evaluation before changing the feature. Reserve untouched cases for assessment and report the set size; a small teaching set does not establish broad safety.
3. Test realistic failures, including invalid outputs and denied actions. Mocked responses test software boundaries; real local-model experiments establish model behavior.
4. Add async/concurrency or streaming when needed. Record and test the chosen cap, backpressure and cancellation behavior. A concurrency limit is not a requests-per-minute rate limiter.
5. Introduce relevant safety tests as soon as untrusted content enters the system. Accumulate production evidence and complete M24 before claiming its outcome.
6. Prefer a simpler system when evaluation shows no useful gain from added complexity.

The [offline agent lab](../resources/agent-lab/README.md) demonstrates deterministic permission, replay and memory contracts. It does not demonstrate answer quality, actual payments or MCP protocol conformance.

<a id="decisions-template"></a>
## Record decisions

Copy the [DECISIONS template](../resources/templates/DECISIONS.md). Record context, alternatives, decision, evidence and consequences. A negative comparison or an abandoned feature is useful evidence when documented honestly.

| Level | Decisions to record |
|---|---|
| L1 | Task/metric, model and license, schema and semantic validation, refusal/failure policy, resource budget |
| L2 | Corpus rights, chunking, retrieval baseline, embedding/reranker, evaluation cases and citation checks |
| L3 | Tools and authorization, confirmation binding, idempotency scope, step/time budgets and memory lifetime |
| L4 | Why more agents, each context/permission boundary, failure behavior and measured benefit |
| L5 | What may change, who owns the metric/holdout, sandbox limits and human acceptance rule |

<a id="cost-math"></a>
## Cost and latency

Measure successful and failed work. Record dated provider prices if used; local execution still consumes time and hardware resources. Separate measured local results from hypothetical hosted estimates.

```text
request_cost = input_tokens * price_per_input_token
             + output_tokens * price_per_output_token
             + retrieval/tool/allocated_infrastructure_cost
cost_per_successful_task = total_cost_of_all_attempts / successful_tasks
monthly_estimate = measured_or_assumed_requests_per_month * mean_request_cost
```

Sum all model/tool calls in a multi-step task. Account for retries, cache pricing, fixed infrastructure and idle costs where applicable. Report the number of trials, workload and p50/p95 latency; choose targets from the application, not a universal 400 ms requirement.

| Scenario | Requests | Estimated monthly cost | Measured latency or untested estimate | First limiting factor |
|---|---|---|---|---|
| Current workload | | | | |
| 10 times the workload | | | | |
| 100 times the workload | | | | |

For arithmetic practice only: 3,000 input and 500 output tokens at hypothetical prices of $1 and $4 per million cost $0.005 per request before other costs. These are invented prices, not a current vendor quote.
