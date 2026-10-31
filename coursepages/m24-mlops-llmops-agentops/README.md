# Module 24 — MLOps + LLMOps + AgentOps

> **Status:** v2026.3 scaffold · full spec in the root [README.md § Module 24](../../curriculum/6-frontier-production.md#module-24).
>
> Supersedes old Module 19 (MLOps / Systems / Responsible AI) by expanding into three operational tiers.

## Why this module exists

Closes Gap #3 of the benchmark PDF — the 2026 operational stack for (1) classical ML (MLOps), (2) prompt/LLM-driven systems (LLMOps), and (3) stateful tool-using agents (AgentOps).

## Primary anchors (P1-verified)

### MLOps (classical)

| Resource | Role | Link |
|---|---|---|
| Full Stack Deep Learning | Canonical open course | <https://fullstackdeeplearning.com/> |
| Made With ML (Goku Mohandas) | End-to-end MLOps course | <https://madewithml.com/> |
| Chip Huyen — *Designing ML Systems* | Canonical text | — |
| Chip Huyen — *AI Engineering* (O'Reilly 2025) | 2026 successor text | <https://www.oreilly.com/library/view/ai-engineering/9781098166298/> |
| MLflow | Experiment tracking + registry | <https://mlflow.org/> |
| Weights & Biases | Research experiment tracking | <https://wandb.ai/> |
| Feast | Open-source feature store | <https://feast.dev/> |
| Evidently | Drift monitoring | <https://www.evidentlyai.com/> |
| BentoML / KServe / Ray Serve / Triton | Serving | <https://www.bentoml.com/> · <https://kserve.github.io/website/> · <https://docs.ray.io/en/latest/serve/> · <https://developer.nvidia.com/nvidia-triton-inference-server> |

### LLMOps (2024–2026)

| Resource | Role | Link |
|---|---|---|
| Langfuse (self-hostable) | Prompt versioning + observability | <https://langfuse.com/> |
| Helicone | Gateway + observability | <https://www.helicone.ai/> |
| PromptLayer | Prompt management | <https://promptlayer.com/> |
| NeMo Guardrails | Guardrails framework | <https://github.com/NVIDIA/NeMo-Guardrails> |
| Guardrails AI | Guardrails | <https://www.guardrailsai.com/> |
| Llama Guard / PurpleLlama | Meta guardrails | <https://github.com/meta-llama/PurpleLlama> |
| OTel GenAI semantic conventions | LLM observability standard | <https://opentelemetry.io/docs/specs/semconv/gen-ai/> |

### AgentOps (2025–2026)

| Resource | Role | Link |
|---|---|---|
| LangSmith | Agent tracing | <https://www.langchain.com/langsmith> |
| Arize Phoenix | Free self-hostable OTel-native tracing (Elastic License 2.0, source-available) | <https://github.com/Arize-ai/phoenix> |
| W&B Weave | LLM/agent tracing | <https://wandb.ai/site/weave> |
| GAIA benchmark | Agent eval | <https://huggingface.co/gaia-benchmark> |
| SWE-bench | Software-engineering eval | <https://www.swebench.com/> |
| E2B / Daytona / Modal | Sandboxing | <https://e2b.dev/> · <https://www.daytona.io/> · <https://modal.com/> |

## 🏁 The Minimum Production Bar

Every project you ship from Modules 1–25 is measured against one standard, defined in full at
[README.md § Minimum Production Bar](../../curriculum/6-frontier-production.md#production-bar). A notebook that only ever ran on
your laptop is not a project — it is a homework file. The bar, in brief:

1. Runs from a clean clone with one documented command
2. Pinned dependencies (`uv` / `requirements.txt` / lockfile), stated Python version
3. A README that says what it does, why, and what the result was — with a number in it
4. Version control with real commit history, not one `initial commit`
5. Tests on the non-obvious logic, and CI that runs them
6. Config and secrets outside the code (`.env`, never committed)
7. Structured logging, not `print`
8. A reachable artefact: an endpoint, a Streamlit/Gradio app, a scheduled job, or a container image
9. A stated evaluation with a baseline to compare against
10. Error handling for the inputs you know are malformed
11. A written limitations section — what it does *not* do, and where it fails
12. Reproducibility: fixed seeds, versioned data, recorded run parameters

Items 1–4 are non-negotiable for every project. Items 5–12 are what separate the two or three
portfolio-centrepiece projects from the rest.

<a id="evaluation-harness"></a>
## 📏 The 4-part evaluation harness (v2026.7)

The single most under-taught skill in AI engineering (Video 1, 08:30–09:04; W2, 06:31–06:58; W4, 11:15–13:20). Most teams start with **eval by vibes**: run the agent a few times, it looks fine, ship it. Then a prompt tweak or model swap makes it worse, and nobody can say whether or why. This harness replaces that. [M21](../m21-rag-vector-dbs/README.md#evaluation-harness) applies it to retrieval, [M22](../m22-agentic-ai/README.md#labs) to agent trajectories and [M23](../m23-ai-safety/README.md#level-5-loops) to self-improving loops.

<a id="harness-1"></a>
### Part 1 · A golden failure dataset (20–50 real tasks)

- Start with **20–50 tasks drawn from real failures**, each with an unambiguous success criterion. Include some cases that already pass, so a fix for one failure can't quietly break another ([Anthropic, *Demystifying evals for AI agents*](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents); W4, 11:56).
- Find the failures through **error analysis**. Read about 100 traces yourself, label at least the first 30, group them into failure categories, and stop when no new categories appear ([Hamel Husain, *Your AI Product Needs Evals*](https://hamel.dev/blog/posts/evals/) · [LLM Evals FAQ](https://hamel.dev/blog/posts/evals-faq/) · [Marina Wyss, *SWE → AI Engineer*, Month 2](https://www.marinawyss.com/blog/software-engineer-to-ai-engineer-roadmap)).
- Store it as `evals/golden.jsonl` with one line per task: `{"id", "input", "expected" or "criteria", "failure_bucket", "source_trace"}`. Version it in git like code.

<a id="harness-2"></a>
### Part 2 · Two kinds of grader: code first, then a calibrated LLM judge

| Grader | Use it for | Rules |
|---|---|---|
| **Deterministic code grader** | Anything checkable: tests pass, the record exists in the DB, JSON matches the schema, correct tool and arguments, under the step limit, a citation is present | Cheap, objective, run thousands. **Use code wherever code can decide** (W4, 12:08) |
| **LLM-as-judge** | Fuzzy qualities: is the summary faithful, did the reply resolve the complaint, is the tone right | A written rubric with **binary pass/fail per criterion**. Validate the judge **against your own labels** before trusting it: report agreement (or TPR/TNR) on a held-out labelled set, and tighten the rubric until it agrees with you ([Hamel Husain, *Using LLM-as-a-Judge*](https://hamel.dev/blog/posts/llm-judge/) · [Eugene Yan, *Evaluating LLM-Evaluators*](https://eugeneyan.com/writing/llm-evaluators/) · [*Product Evals in Three Simple Steps*](https://eugeneyan.com/writing/product-evals/)) |

Never let an unvalidated judge gate a release. Re-check its agreement whenever you change the judge model or the rubric.

<a id="harness-3"></a>
### Part 3 · Multi-run pass rates, not single runs

Agents are non-deterministic: the same task can pass today and fail tomorrow with no code change (W4, 12:43). Run every task **N times (start with N = 5)** and report:

- **pass rate** per task and overall, and **pass^k** (passes *all* k runs), which matters for customer-facing reliability. An average can hide the 1-in-5 failure you care about.
- **pass@k** (passes *at least once* in k), useful only where retrying is acceptable, such as offline code generation.

<a id="harness-4"></a>
### Part 4 · Cost and operations regression telemetry

Log these **per task, per run**: steps, tool calls, input and output tokens, dollar cost, latency and the termination reason. **A prompt change that keeps accuracy but doubles token cost is a regression** (W4, 13:08). Set budgets in your [`DECISIONS.md`](../../guides/portfolio-spine.md#decisions-template) and fail CI when they're exceeded.

**Run the whole suite on every change** to the prompt, model, retrieval or tools: locally with one command, and in CI on every pull request.

<a id="evals-stack"></a>
### 🧰 Free / open-source evals and observability stack (verified 2026-10-27)

| Tool | Licence | Best at | Use it for |
|---|---|---|---|
| [**Promptfoo**](https://github.com/promptfoo/promptfoo) | MIT | Declarative YAML eval matrices (prompts × models × test cases), CI integration, red-teaming | **Default CI runner** for L1–L4 regression suites |
| [**Inspect AI**](https://inspect.aisi.org.uk/) (UK AI Security Institute) | MIT | Python-first tasks = dataset + solver + scorer; agent/tool evals, sandboxes, multi-epoch runs | **Default for agent evals** (L3–L5) and anything safety-flavoured (M23) |
| [**Ragas**](https://github.com/vibrantlabsai/ragas) | Apache-2.0 | RAG metrics: faithfulness, context precision/recall, answer relevance | The **retrieval leg** (M21, L2) |
| [**DeepEval**](https://github.com/confident-ai/deepeval) | Apache-2.0 | pytest-style LLM assertions | When your team already lives in `pytest` |
| [**Langfuse**](https://github.com/langfuse/langfuse) | MIT core (some enterprise features under a separate licence) | Self-hostable tracing, prompt versioning, datasets, scores | **Default tracing** if you want fully open source |
| [**Arize Phoenix**](https://github.com/Arize-ai/phoenix) | Elastic License 2.0 (source-available, free to self-host; not OSI open source) | OpenTelemetry-native trace inspection, eval notebooks | Local trace debugging with [OTel GenAI conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) |

**Recommended minimal stack:** Promptfoo *or* Inspect for the suite, Langfuse for traces, Ragas for retrieval. Managed tools such as LangSmith or W&B Weave are fine on their free tiers, but pick from the list above if you want no vendor lock-in.

## Mandatory mini-projects

1. **MLOps:** Package a scikit-learn model with MLflow tracking + BentoML serving + Evidently drift dashboard.
2. **LLMOps:** Instrument an LLM app with Langfuse traces + OTel GenAI semantic conventions + a promptfoo eval in CI.
3. **AgentOps:** Trace a LangGraph agent with LangSmith or Phoenix; run GAIA-Level-1 as a regression suite.

## Prerequisites

- Any model from Modules 9–18; Module 22 for the AgentOps half.
