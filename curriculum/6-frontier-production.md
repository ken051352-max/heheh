[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [← 🟪 Deep Learning (M15–M17)](5-deep-learning.md)

---

# 🔴 FRONTIER & PRODUCTION STRATUM — Modules 18, 21–26

<img src="../assets/stratum-6-production.jpg" alt="Frontier and production AI, modules 18 and 21 to 26" width="100%">

Build on one evolving project: understand the model, retrieve useful evidence, constrain actions,
evaluate failures, operate the system, and communicate a decision. Each module has one required
artifact and clearly marked extensions. Follow the [learning contract](README.md#learning-contract)
and [evidence policy](../guides/sources.md#evidence-policy). Free lectures and local exercises form
an accessible route; recommended books are selected for quality, whether paid or freely available.

<a id="module-18"></a>
## Module 18: Large Language Models, Post-Training & Evaluation

**Why:** Decide what an existing model can do, when adaptation is justified, and how to demonstrate
its limitations. Learning to call a model and learning to train one are different milestones.

**Strict Prerequisites:** M15–M16 for the full module. M17 is required before the PPO/RL extension.
The application subset below is available after M1 and does not count as completing full M18.

<a id="application-foundations"></a>
### Application foundations — M18-app

**Prerequisite:** M1, including typed input validation, HTTP failure handling, and tests.

- Explain tokenization, context limits, sampling variability, model/data provenance, and the
  distinction between an answer, a citation, and supporting evidence.
- Build a small extraction or classification application. Keep its input/output contract separate
  from the model adapter; record model identifier/revision and generation settings.
- Compare a deterministic heuristic, zero-shot prompting, and a few-shot prompt on a frozen task
  set. Define semantic correctness as well as schema validity; inspect false positives/negatives.
- Use Pydantic v2 for application validation. Compare prompt-only JSON with constrained generation
  through [Outlines](https://dottxt-ai.github.io/outlines/latest/), or study the official
  [OpenAI](https://developers.openai.com/api/docs/guides/structured-outputs) and
  [Anthropic](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) interfaces.
  Providers support different schema subsets. Handle refusal, incomplete generation, unsupported
  schema, transport failure, and domain-invalid values explicitly. Valid structure does not prove
  factual correctness or authorization.

**Completion evidence:** a runnable adapter, mocked transport/error tests, and an evaluation report
from a **real model**. A small local model such as
[SmolLM2-135M-Instruct](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct) provides a CPU
experiment; weak results are legitimate evidence. Mocks validate plumbing, not model quality.
Record hardware, download size, and measured runtime; paid API access is unnecessary.

<a id="application-integration"></a>
**Application-engineering extension — a small complete product:** after the M18-app core, connect the adapter to one simple local interface and a typed backend. A plain HTML form or small Python UI is sufficient; a particular frontend framework is not required.

Retain one useful end-to-end task: validated input, clear loading/success/error states, minimal persistence with an explicit schema, and a reproducible start command. Test a successful flow, malformed input, timeout/refusal and a failed dependency using deterministic fixtures. Keep real-model quality results separate from those integration tests. If you add accounts or multiple users, enforce authorization on the server and test cross-user access. Use [M24](#module-24) when turning this exercise into a production portfolio system; a local teaching demo alone does not meet its full production bar.

The [employer sample](../audit/career-research-2026-11-05.md) motivates this targeted software exercise. It does not add web development as a requirement for statistical/research routes.

### Full module: understanding and adapting models

Full M18 includes the application-foundations outcomes above as well as the training and evaluation
outcomes below. Reuse the same adapter and frozen task where appropriate.

**Core outcomes:**

- Trace tokens through a causal transformer, distinguish pretraining from SFT and preference
  optimization, and explain how train/validation/test contamination changes conclusions.
- Prepare licensed, deduplicated data; split by source/entity before generating related examples;
  mask the appropriate loss tokens and inspect the tokenizer/chat template.
- Implement SFT and a LoRA adaptation with [PEFT](https://huggingface.co/docs/peft/en/index) and
  [TRL](https://huggingface.co/docs/trl/en/index). Explain frozen base weights, rank, target modules,
  and the memory tradeoffs of QLoRA. Pin a compatible environment rather than copying `main` docs
  into an older installation.
- Understand reward modeling, PPO-based RLHF, DPO's preference-pair objective and reference policy.
  [DPO](https://huggingface.co/docs/trl/en/dpo_trainer) does not require a separately trained reward
  model; it is not an on-policy RL algorithm. Preference labels still encode judgments and biases.
- Measure held-out task quality, cross-entropy/perplexity where appropriate, robustness, latency,
  and resource use. Separate improved formatting from improved reasoning or factuality.

**Depth menu:** scaling laws and data curation; FlashAttention and paged KV caches; quantization,
continuous batching and speculative decoding; MoE and state-space alternatives; long-context
retrieval; multimodal models; distillation; advanced preference objectives and RL with verifiable
rewards. Choose one extension after the core artifact; report the workload behind performance claims.

**Free lectures for the full module:** [Stanford CS336](https://cs336.stanford.edu/).
**Application lecture route:** [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/).
**Practical companion:** [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1).
**University depth:** CS336 assignments;
its full GPU systems/training workloads exceed the local core. Assignment 5 covers alignment and
reasoning RL; DPO is an optional part. CPU correctness exercises do not reproduce the full course.
**Recommended main books:** Sebastian Raschka, [*Build a Large Language Model (From Scratch)*](https://www.manning.com/books/build-a-large-language-model-from-scratch)
(Manning, 2024), for mechanisms; Chip Huyen, [*AI Engineering*](https://huyenchip.com/books/)
(O'Reilly, 2025), especially evaluation, dataset engineering, and fine-tuning. The free
[Jurafsky–Martin draft](https://web.stanford.edu/~jurafsky/slp3/) supplies broader NLP theory.

**📦 Module Project (mandatory) — Adapt a small model and evaluate the tradeoff.** Use a narrow,
licensed task and a genuinely trained small LoRA adapter. CPU training on a tiny model and short
sequences is acceptable; QLoRA/GPU scaling is an extension. Compare base zero-shot, improved prompt,
fixed-context baseline, and adapted model on the same held-out examples. Add full retrieval at M21.
Submit the data card, split manifest, training curve, executable scoring/tests, locked environment,
README, and results memo. A negative result passes when the method and limitations are sound.
**Stretch:** DPO on separately curated preference pairs, with a regression check on another ability.

---

<a id="module-21"></a>
## Module 21: RAG, Vector DBs & Retrieval Systems

**Why:** Retrieve authorized, relevant evidence and determine whether it improves the answer.
[Menlo's 2025 enterprise report](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)
surveyed about 500 U.S. decision-makers and combined responses with market modeling. Such an
investor-produced sample provides context, not a universal deployment census or a reason to use RAG.

**Strict Prerequisites:** M1, M8a, and [M18-app](#application-foundations) competence (also covered
by full M18). M11's vector geometry is recommended; learn cosine similarity before dense retrieval.

**Core outcomes:**

- Ingest a small corpus with document IDs, versions, provenance, and access metadata; preserve
  page/section citations through chunking and re-indexing.
- Compare BM25, dense retrieval, reciprocal-rank fusion, and a cross-encoder reranker on one corpus.
  Start with exact vector search before measuring approximate-index recall/latency tradeoffs.
- Evaluate hit@k, context precision, recall@k where relevance labels are complete, and answer
  faithfulness/correctness. Assess unanswerable questions, stale documents, and authorization filters.
- Distinguish [ColBERT](https://github.com/stanford-futuredata/ColBERT) text late interaction from
  [ColPali](https://github.com/illuin-tech/colpali) visual document retrieval. They are depth options;
  ColPali is not a drop-in name for ordinary single-vector text embeddings.

**Default local stack:** text/Markdown exports → BM25 +
[BGE-small](https://huggingface.co/BAAI/bge-small-en-v1.5) CPU embeddings → local LanceDB or NumPy
exact search → a small BGE cross-encoder on a bounded candidate set. Local PostgreSQL/pgvector is
a SQL-oriented alternative. Hosted Cohere reranking and paid generation are optional comparisons.

**Free lecture:** [Full Stack LLM Bootcamp — Augmented Language Models](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/augmented-language-models/)
(2023 concepts; use current implementation docs). **Practical reading:**
[Pinecone Learn](https://www.pinecone.io/learn/),
[LlamaIndex docs](https://developers.llamaindex.ai/python/framework/), and the
[original RAG paper](https://arxiv.org/abs/2005.11401).
**Main book:** Huyen, *AI Engineering*, retrieval and evaluation chapters.

**Decision framework:** start with a deterministic or no-retrieval baseline, then test prompt
examples, fixed context, retrieval, and fine-tuning against observed failure categories. These
methods can complement each other; no universal cost ranking applies. Retrieval may supply missing
facts but cannot guarantee their correctness. Fine-tuning may change knowledge or behavior but does
not maintain a source-of-truth database. Measure the component that earns its extra complexity.

**📦 Module Project (mandatory) — One evaluated retrieval system.** Freeze 20–50 labeled questions
and supporting document IDs before tuning. Use separate development examples. Compare no retrieval,
BM25, dense, hybrid, and hybrid plus reranker under the same generation settings. Report retrieval
metrics, claim-level evidence checks, answer correctness, abstention, and latency. This small set is
a teaching/regression set, not evidence of population-wide reliability. Submit ingestion and scorer
tests, the versioned corpus/eval, reproducible commands, README, and memo; document observed failures.
Mocked generation covers integration tests only; answer-quality claims need real generated answers.
**Stretch:** one of contextual retrieval, GraphRAG, late interaction, or multimodal retrieval with
an ablation against the core system. [Detailed lab and rubric](../coursepages/m21-rag-vector-dbs/README.md).

---

<a id="module-22"></a>
## Module 22: Agentic AI — Bounded Workflows, Tools, MCP & Memory

**Strict Prerequisites:** M21 and [M18-app](#application-foundations) competence.
**Why:** Give a model only the actions needed for a defined task, then demonstrate that failures are
bounded. [Anthropic's workflow patterns](https://www.anthropic.com/engineering/building-effective-agents)
provide a useful design vocabulary; they do not make a particular framework mandatory.

**The Minimal Workflow Principle:** deterministic baseline → fixed workflow → one model-directed
loop → multiple agents only when a measured benefit justifies coordination and failure modes.

- Use intent-based tools with typed inputs/outputs; aim for compact schemas (a 1 KB target is a
  classroom design budget, not an MCP rule). Validate arguments and results outside the model.
- Enforce tool/tenant allowlists, total step and time budgets, bounded retries, and I/O timeouts.
  Retried writes require durable idempotency; merely accepting a key does not implement it.
- Keep authorization in trusted code. Bind human confirmation to the exact privileged/destructive
  action and payload. Model text, tool annotations, and a model-supplied `approved=true` confer no power.
- Compare full tool lists with progressive discovery; record selection accuracy, schema tokens,
  latency, and recovery. Cache catalogs by caller authorization and honor freshness/invalidation.
- Separate working context, episodic summaries/checkpoints, and durable semantic memory. Preserve
  provenance, timestamps, tenant isolation, expiry, contradiction resolution, and deletion controls.

**MCP compatibility:** teach released [revision 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28),
not an invented October revision. It uses per-request version/capability metadata and mandatory
server support for `server/discover`; the client may discover first. Tool lists support pagination
and cache metadata. `outputSchema` is optional in the protocol; this lab requires typed output.
Annotations such as `readOnlyHint` and `destructiveHint` are untrusted hints. The
[Python SDK migration guide](https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/migration.md)
distinguishes v2 `MCPServer`/snake_case Python fields from wire JSON names and legacy v1 tutorials.
SDK v2 supports modern and older clients; record the pair actually tested. Tasks, A2A, Agent Skills,
and WebMCP are separate extension/interoperability topics, not required by every MCP server.

**Free course:** [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/), with local
substitutes for hosted exercises; **depth:** [Berkeley Agents MOOC](https://llmagents-learning.org/).
**Main book:** Huyen, *AI Engineering*, tools, planning, memory, and failure analysis.

**📦 Module Project (mandatory) — A bounded, evaluated tool assistant.** Expose a small local SQL
fixture through an actual MCP SDK server, then connect a local SDK client. Implement a deterministic
workflow and a model-directed alternative over the same 20 tasks. Include malformed requests,
unknown tools, permission failures, stale discovery, timeouts, and duplicate writes. Submit typed
schemas, protocol transcript, control tests, repeated real-model outcomes, traces, and decision memo.
Start with [the local contracts lab](../resources/agent-lab/README.md); its scripted tests establish
application controls, not model quality or MCP conformance. Follow [Labs 1–5](../coursepages/m22-agentic-ai/README.md#labs)
for staged extensions. Multi-agent research and public benchmark runs are optional depth.

---

<a id="module-23"></a>
## Module 23: AI Safety, Alignment, Interpretability, Evals & Policy

**Strict Prerequisites:** [M18-app](#application-foundations) for application threat modeling;
M22 before tool-escalation labs. M15–M16 before mechanistic-interpretability research extensions.

**Core outcomes:** map assets, actors, trust boundaries, and failures using the
[OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) and
[NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework), plus its
[GenAI Profile](https://doi.org/10.6028/NIST.AI.600-1). NIST describes the framework as voluntary and
under revision; these references do not certify compliance or prove safety.

- Distinguish direct/indirect prompt injection, data/model poisoning, sensitive-data disclosure,
  improper output handling, excessive agency, and unbounded resource consumption.
- Match each threat to an enforced control and a reproducible test. Include tenant crossings,
  poisoned retrieval/memory, forbidden tools, malformed outputs, and budget exhaustion.
- Use deterministic checks for side effects and access violations; use independently labeled
  examples to calibrate judgments about harmful or unsupported answers. Measure benign false blocks.
- Learn specification gaming, reward-model bias, and evaluation contamination. Keep held-out data
  and scorer permissions separate from any agent that proposes improvements.
- Write a system/model card: intended use, data/model provenance, populations, limitations, measured
  failures, mitigation owner, and residual risk. Map relevant policy obligations to primary text.

**Free lecture route:** select safety, benchmarks/evaluation and security videos from
[Berkeley Understanding LLMs, Spring 2024](https://rdi.berkeley.edu/understanding_llms/s24).
The full graduate course is not required for this application's threat-modeling core.
**Alternative curriculum:** [BlueDot AI Alignment](https://bluedot.org/courses/alignment) requires
a free account for full materials; cohort admission and facilitation have separate terms. **Practical framework:**
[Inspect AI](https://inspect.aisi.org.uk/). **Research depth:**
[Transformer Circuits](https://transformer-circuits.pub/), induction heads, superposition, SAEs,
activation patching, and scalable oversight. A feature interpretation needs counterexamples and
causal interventions; labeling five activations does not establish monosemanticity.
**Principal recommended book:** Chip Huyen's [*AI Engineering*](https://huyenchip.com/books/)
(paid), especially evaluation and system-design chapters. Russell's *Human Compatible* and
Christian's *The Alignment Problem* are paid broader-framing references; technical papers and
threat models remain necessary for the chosen lab.

**📦 Module Project (mandatory) — Threat model plus regression suite.** Extend the M18/M21 system
(and M22 tools when present) with direct/indirect injection, poisoned-content, sensitive-data, and
privilege-escalation cases. Add unseen variants and benign controls. Assert unauthorized side effects
are zero on the test set, report attack success and false-block counts, and document remaining gaps.
Submit runnable tests, a results table, risk register, and two-page decision memo.
**Stretch:** one interpretability replication or a sandboxed optimization loop with a held-out judge.
[Detailed safety lab](../coursepages/m23-ai-safety/README.md).

---

<a id="module-24"></a>
## Module 24: MLOps + LLMOps + AgentOps

**Strict Prerequisites:** one completed, evaluated project; M22 for AgentOps and the relevant M23
threat/evaluation controls for an AI application. Classical-model projects do not require LLM modules.

**Core outcomes:** package and serve a model; version its dependencies/data/configuration; run
checks on push/PR; observe failures; and restore a known-good release. Choose the operational layer
appropriate to the project. Distributed training, Kubernetes, feature stores, and cloud infrastructure
are extensions, not prerequisites for a local production-style artifact.

**Free lectures:** [Full Stack Deep Learning 2022](https://fullstackdeeplearning.com/course/2022/).
**Practical course:** [Made With ML](https://madewithml.com/).
**Main books:** Huyen, [*Designing Machine Learning Systems* and *AI Engineering*](https://huyenchip.com/books/).
They serve complementary classical-ML and foundation-model systems topics. Both appear in the
[University of Helsinki's 2026 systems course](https://studies.helsinki.fi/courses/course-implementation/hy-opt-cur-2627-648f020d-a607-4e96-8bff-b5fc34e6d76a).
Treveil et al., *Introducing MLOps*, is a shorter companion, not an additional completion gate.

<a id="production-bar"></a>
### 🏁 Minimum Production Bar for Portfolio Projects

Meet this complete bar for **one M24 centerpiece**. Earlier modules use their own smaller project
rubrics. A private local repository and reproducible local service are valid evidence.

| # | Requirement | Review evidence |
|---|---|---|
| 1 | Reproducible package | Importable code, entry point, Python version, locked dependencies, clean-clone command |
| 2 | Automated tests | Data/transform boundary tests, numerical tolerances when needed, and one end-to-end path |
| 3 | Typed interfaces | Checked public type hints and validated external/config payloads; Pydantic v2 is the default Python option |
| 4 | Structured logs | Request/run IDs, errors and latency; secrets and sensitive payloads redacted |
| 5 | Configuration | Validated config, ignored local secrets, safe example config |
| 6 | Container | Dockerfile, pinned base, non-root execution, .dockerignore, successful local smoke run |
| 7 | Automated CI and eval gates | Push/PR lint/type/tests plus deterministic evaluation gates; changed model/prompt/data evaluated before release |
| 8 | Artifact lineage | Data/model/prompt/config identifiers and hashes, source commit, run parameters, metrics; local MLflow or manifest is sufficient |
| 9 | Reachable artifact | Local endpoint/container command and recorded response, or an optional hosted demo |
| 10 | Monitoring | Health, error/latency/resource metrics, one tested alert, and applicable quality/drift controls |
| 11 | Runbook and rollback | Architecture, clean-clone instructions, previous artifact/config restore command, deliberately tested rollback |
| 12 | Results memo | Baseline, budget, results, uncertainty, observed incident and recovery, limitations and next decision |

For LLM/agent projects, trace model, retrieval, and tool steps using
[OpenTelemetry GenAI conventions](https://github.com/open-telemetry/semantic-conventions-genai).
They currently have **Development** status; record the semantic-convention revision and instrumentor
versions. Capture prompts/responses only with an explicit data policy. Start with local traces;
Langfuse or Phoenix can provide a viewer. Provider costs and quotas are optional measured inputs.

**📦 Module Project (mandatory) — Operate one existing project.** Meet all 12 rows. Induce one
failure (unavailable dependency, corrupt input, or budget exhaustion), show the alert, and restore the
previous working release. Record deployment and rollback commands, lineage, resource budget and
actual results. A ten-minute setup is a useful goal, not a universal pass threshold for downloads.
**Stretch:** canary/shadow evaluation or distributed scaling with a measured need.
[Coursepage and shared evaluation harness](../coursepages/m24-mlops-llmops-agentops/README.md#evaluation-harness).

---

<a id="module-25"></a>
## Module 25: Product DS, Business, Communication & Storytelling

**Strict Prerequisites:** M6 and M7 for full M25; M6½ is required when claiming causal impact.
A modeling module is useful when the decision involves a predictive model, not for every product analysis.

<a id="product-brief"></a>
### Product brief — M25-brief

Available after M1: identify a user, a decision, the current workflow, a measurable acceptance
criterion, and a resource budget. Write a one-page brief and get feedback from a reviewer. Label
hypothetical data and assumptions. This descriptive application subset makes no causal-impact claim
and does not replace the statistical requirements of full M25.

**Core outcomes:** operationalize a metric tree (unit, denominator, observation window, inclusion
rules); distinguish a product change from instrumentation/population changes; estimate uncertainty;
propose a decision with guardrails and the evidence that would reverse it. Explain costs of errors,
proxy failures, missing data, selection bias, and ethical tradeoffs in ordinary language.

**Free video route:** [Storytelling with Data public videos](https://www.storytellingwithdata.com/videos).
**Free references:** [Ron Kohavi's ExP papers](https://exp-platform.com/) and
[Shneiderman's visualization paper](https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf).
**Recommended main books:** Kohavi, Tang & Xu, *Trustworthy Online Controlled Experiments*, and
Knaflic, *Storytelling with Data*. Use their experiment-interpretation and audience/visualization
chapters for this project. Library availability is useful but is not a promise of free access.

**📦 Module Project (mandatory) — An evidence-backed product decision.** Analyze a retention or
conversion change with an explicit metric contract and segment/time checks. Produce a metric tree,
one-page recommendation, reproducible analysis/tests, and a short readout (video, narrated slides,
or accessible written equivalent). State uncertainty, expected value with sensitivity, guardrails,
and the proposed next experiment. Causal claims need identification and M6½ evidence; synthetic
scenarios must be labeled. Include reviewer feedback and the resulting revision.
[Detailed rubric](../coursepages/m25-product-ds/README.md).

---

<a id="module-26"></a>
## Module 26: Capstone — Research, Systems & Applied Tracks

**Prerequisites:** completion of the chosen role's core and the modules supporting this project.
Research requires M6, M25-brief and the theory/methods relevant to its question; M15 is needed for
a deep-learning project, not for every research capstone. Systems requires M24 plus applicable safety controls;
Applied requires M6/M7/M25 and M6½ for causal claims. All 27 modules are not a universal gate.

Choose one track. Agree a written question, scope, baseline, budget and evaluation plan before the
main implementation; review a pilot before committing to a large run. A rigorous null result can pass.
The scores below are **roadmap teaching rubrics**, not university grading rules or hiring guarantees.

| Track | Artifact | Rubric (100 points) |
|---|---|---|
| Research | 4–8 page paper/report, related-work matrix, reproducible experiments or proofs | Question/contribution 20; method/baselines/ablations 30; reproducibility/uncertainty 30; writing/limitations 20 |
| Production Systems | Locally runnable or hosted ML/AI service meeting the M24 bar | Architecture 20; functional/quality/safety evals 30; measured latency/resource SLOs 20; monitoring/rollback/reproduction 30 |
| Applied Flagship | Stakeholder decision package and reproducible analysis or application | Problem/metric contract 25; validity and uncertainty 30; decision usefulness/guardrails 25; reproducibility/communication 20 |

**Passing evidence:** at least 75/100, no missing category, reproducible baseline comparison, and no
unsupported claims about impact or safety. Label simulations and inaccessible data; provide a
sanitized fixture or documented access process. Research novelty may be a careful replication,
negative result, or new analysis. Applied impact may be an honest pilot estimate or prospective
experiment design when an actual intervention is unavailable; do not invent ROI or stakeholder use.
For measured causal effects, state the estimand, identification assumptions, uncertainty and sensitivity.

**Submission package:** README and environment; provenance/licensing; data/model/config versions;
tests and evaluation outputs; paper or decision memo; limitations; reviewer feedback. Systems adds
Docker/CI/ops artifacts. Private, selectively shared, and sanitized public packages are all valid.
Publication, paid cloud hosting, and venue acceptance are optional.

**Free research guidance:** [Cambridge MLMI project structure](https://www.mlmi.eng.cam.ac.uk/about-programme/course-structure)
and the [NeurIPS paper checklist](https://neurips.cc/public/guides/PaperChecklist).
**Writing shelf:** *The Craft of Research*, *Writing Science*, and *How to Write a Lot*; choose a
book for the writing problem you actually face. Cross-check citations against the original sources.

---

[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [← 🟪 Deep Learning (M15–M17)](5-deep-learning.md)
