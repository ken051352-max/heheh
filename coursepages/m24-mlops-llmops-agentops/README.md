[Home](../../README.md) · [Curriculum index](../../curriculum/README.md) · [Resume](../../guides/progress-tracker.md#resume)

# Module 24 — MLOps + LLMOps + AgentOps

**First task:** Reproduce one evaluated project result and mark which production-bar item is missing first; work on that item.

[Check prerequisites](#entry-prerequisites) · [Start the lab](#start-lab) · [Completion evidence](#completion)

This page supports the linked module; it is not an additional course to finish. Optional extensions come after the core artifact.

[Full module](../../curriculum/6-frontier-production.md#module-24) ·
[Canonical Minimum Production Bar](../../curriculum/6-frontier-production.md#production-bar)

<a id="entry-prerequisites"></a>
## Prerequisites and default route

Bring one completed, evaluated project. M22 is required for the AgentOps extension, and the
relevant M23 threat/evaluation controls apply to AI applications. Data pipelines and classical models can complete
M24 without LLM or agent modules. For the Data Engineer route, carry the M8a/M8b project through the
[pipeline operations contract](../../curriculum/6-frontier-production.md#data-pipeline-operations): data-quality/reconciliation gates, safe replay, completion/freshness budgets and tested recovery. Select transferable testing/deployment/monitoring material below and reuse M8b's pipeline resources; model training is not an added prerequisite.

| Resource | Role and access |
|---|---|
| [Full Stack Deep Learning 2022](https://fullstackdeeplearning.com/course/2022/) | Free lectures and labs; default systems course |
| [Made With ML](https://madewithml.com/) | Free code-oriented companion |
| [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/) | Free LLMOps lectures; supplement dated SDK examples with current docs |
| [Designing ML Systems / AI Engineering](https://huyenchip.com/books/) — Chip Huyen | Recommended main books for classical/AI application systems; complementary paid texts |
| [OpenTelemetry GenAI](https://github.com/open-telemetry/semantic-conventions-genai) | Current source; Development status, version-sensitive conventions |
| [MLflow](https://mlflow.org/) | Local experiment/artifact tracking option |

<a id="start-lab"></a>
## 🏁 One production bar, one centerpiece

The [12-row canonical bar](../../curriculum/6-frontier-production.md#production-bar) is the single
completion checklist: package, tests, typed boundaries, structured logs, configuration, container,
CI/eval gates, artifact lineage, runnable artifact, monitoring, rollback/runbook, and results memo.
Meet it once, deeply, in M24. Earlier modules retain their smaller learning rubrics.

A local Docker service or pipeline job with a documented smoke run is valid; public hosting, Kubernetes and paid
cloud accounts are optional. Run metadata can begin as a versioned manifest or local MLflow store.
Use one adequate tool for each need; installing every framework is not a learning outcome.

<a id="evaluation-harness"></a>
## 📏 The four-part evaluation harness

**Scope:** this task/trial harness covers model, retrieval and agent behavior. A data-only pipeline uses deterministic schema, reconciliation, bad-record and replay fixtures plus operational measurements from the pipeline contract; it does not need synthetic prompts, token counts or an LLM judge.

Use the same harness across [retrieval](../m21-rag-vector-dbs/README.md#evaluation-harness),
[agents](../m22-agentic-ai/README.md#labs), and [safety](../m23-ai-safety/README.md#evaluation-harness).
[Anthropic's evaluation guide](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
distinguishes tasks, trials, graders, transcripts and actual final state. Treat those as separate
objects in your project so a persuasive response cannot substitute for a correct state change.

<a id="harness-1"></a>
### Part 1 · Versioned tasks and held-out evidence

Start with 20–50 representative tasks, including known failures and ordinary passing cases. This is
a teaching/regression set, not a reliability certification. Develop on separate examples; protect a
held-out subset from repeated prompt tuning. Record data provenance and why each category matters.

Store one JSONL object per task with a stable ID, input, expected output or rubric, category, and
source. Add relevant document IDs for retrieval and expected final state/allowed side effects for
agents. Freeze corpus/model/config identifiers for each run. Label synthetic data explicitly.

<a id="harness-2"></a>
### Part 2 · Code graders and calibrated judgments

| Grader | Use | Required checks |
|---|---|---|
| Deterministic | Output schema, task-specific exact answer, tool arguments, DB state, citations, budgets | Test grader edge cases and known pass/fail fixtures; citation presence is not evidential support |
| Human rubric | Correctness, supported claims, usefulness, refusal appropriateness | Explicit criteria, examples and adjudication of ambiguous labels |
| LLM judge | Scalable approximation of a human rubric | Validate on separate human-labeled examples; report false accepts/rejects and agreement; revalidate model/rubric changes |

Use deterministic or human grading for a free local route. A paid judge is optional. Never claim
that schema-valid output proves semantic correctness, and never let an unvalidated judge alone
approve a release. Keep grader/data permissions separate from any optimization agent.

<a id="harness-3"></a>
### Part 3 · Repeated trials and uncertainty

For stochastic systems start with five trials per task when feasible; publish the actual trial
count, seeds/settings and raw outcomes. Report first-attempt success, per-task pass rate and the
number of tasks that pass **all** trials. `pass@k` (at least one success) applies only when those
retries are permitted; it is different from `pass^k` (all k succeed).

Report counts, denominators and uncertainty. Repeated trials of one task do not create independent
new tasks; compare changes on paired tasks and report per-category failures. A five-instance public
benchmark subset is a learning exercise, not a leaderboard estimate.

<a id="harness-4"></a>
### Part 4 · Resource and operational regressions

Record task/run ID, source commit, model/prompt/data versions, grader version, actual final state,
termination reason, latency, steps, retries and token counts. Track peak local memory/runtime; add
API cost only for hosted runs. Define acceptable quality/resource changes in the decision memo
before comparing candidates. A cost increase can be justified by a measured quality gain.

Run deterministic control and integration tests on every push/PR. Evaluate any change to model,
prompt, data, retrieval or tools before release using the frozen real-system suite. Small local-model
checks can run in CI; expensive sweeps can run separately with results tied to the exact commit.
Mocks are useful for stable transport failures, but cannot approve a model-quality change.

<a id="evals-stack"></a>
### Minimal evaluation and observability stack

Start with Python tests, JSONL task/run records and local structured logs. Add
[Inspect](https://inspect.aisi.org.uk/) or [promptfoo](https://github.com/promptfoo/promptfoo) for
suite orchestration, [Ragas](https://github.com/vibrantlabsai/ragas) for relevant retrieval metrics,
and one viewer such as [Langfuse](https://github.com/langfuse/langfuse) or
[Phoenix](https://github.com/Arize-ai/phoenix) if useful. Check repository licenses and hosted terms;
free self-hosting, open source, and free managed service are different claims.

For GenAI telemetry, pin the
[semantic-convention revision](https://github.com/open-telemetry/semantic-conventions-genai) and
instrumentor versions. Trace model, retrieval and tool operations with correlated IDs; record errors
and budget exhaustion. The conventions have Development status and may change. Keep sensitive
prompt/response content capture off unless the project has an explicit data policy. Metrics and
redacted traces are enough to begin.

<a id="completion"></a>
## 📦 Required project — operate and recover one system

1. Select one evaluated project and meet all rows of the canonical production bar. Use a local
   package/container, validated configuration, test suite, artifact manifest, and automated CI.
2. Define a measured resource/quality budget on stated hardware and workload: service latency/concurrency
   or pipeline completion/freshness under a declared schedule. Store input/output data, code/config and any model/prompt identifiers needed to reproduce the baseline.
3. Introduce an observable failure: unavailable dependency, invalid payload, corrupted artifact,
   budget exhaustion or a controlled distribution change. Record the alert and investigation.
4. Restore a previous known-good artifact/configuration using the documented rollback command.
   For a pipeline, restore consistent data/checkpoint state or replay fixed inputs, verifying that outputs are neither duplicated nor partially published.
   Run the smoke/evaluation gates again and record the outcome. A rollback paragraph without an
   executed drill does not satisfy the systems artifact.
5. Submit the architecture, runbook, clean-clone instructions, lineage, incident memo, and results.

**Done:** one command reproduces the service or pipeline job and verification; every checklist row points to
concrete evidence; quality and resource limits are declared; the rollback drill succeeds. Public
hosting is optional. **Stretch:** one justified canary/shadow evaluation, distributed workload, or
feature-store integration. Do not build classical, LLM and agent services solely to tick three boxes.


---

**After the core:** record the artifact, remaining gap and next task in the [tracker](../../guides/progress-tracker.md#resume), then return to your [chosen route](../../guides/practitioner-track.md#role-pathways). Revisit only the missing skill with the [readiness pattern](../../guides/readiness-checks.md#how-to-check).
