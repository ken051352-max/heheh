[Home](../../README.md) · [Curriculum index](../../curriculum/README.md) · [Resume](../../guides/progress-tracker.md#resume)

# Module 22 — Agentic AI: Bounded Workflows, Tools, MCP & Memory

**First task:** Open the offline contracts lab, inspect one allowed and one denied action, then sketch a deterministic task sequence.

[Check prerequisites](#entry-prerequisites) · [Start the lab](#start-lab) · [Completion evidence](#completion)

This page supports the linked module; it is not an additional course to finish. Optional extensions come after the core artifact.

[Full module](../../curriculum/6-frontier-production.md#module-22) ·
[Local executable contracts lab](../../resources/agent-lab/README.md)

<a id="entry-prerequisites"></a>
## Prerequisites and route

Complete M21 and [M18-app competence](../../curriculum/6-frontier-production.md#application-foundations)
(full M18 also covers it). Start with a deterministic workflow, add one model-directed loop, and
compare the results. Multi-agent frameworks are extensions justified by the workload.

| Resource | Role |
|---|---|
| [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/) | Free course; use local substitutes for hosted exercises |
| [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | Workflow/agent design patterns; 2024 article, current SDKs differ |
| [Berkeley Agents MOOC](https://llmagents-learning.org/) | Free university depth |
| [AI Engineering](https://huyenchip.com/books/) — Chip Huyen | Recommended main book: agents, memory, and evaluation; paid |
| [MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) | Released protocol reference |
| [Python SDK migration](https://github.com/modelcontextprotocol/python-sdk/blob/main/docs/migration.md) | v1/v2 API and wire compatibility |
| [Demystifying agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Tasks, trials, outcomes, and grading |

<a id="tool-design"></a>
## 🛠️ Tool design and released MCP conformance

A tool exposes a capability, not unrestricted access to a database or shell. The application
validates the model's proposed request and decides whether the authenticated caller may perform it.
Begin with [the local contracts lab](../../resources/agent-lab/README.md), whose tests exercise these
boundaries without real payments, credentials, or model calls.

<a id="tool-rules"></a>
### Four tool-design rules

| Rule | Required evidence |
|---|---|
| Intent-based, bounded tools | Names such as `search_orders`; narrow arguments; capped results; no arbitrary SQL/eval |
| Typed, compact contracts | Input validation and typed results; measure schema bytes/tokens; aim for 1 KB per small tool, document justified exceptions |
| Honest annotations and authorization | Correct read/destructive/idempotent hints, plus independent caller/tenant policy and human approval for privileged or destructive actions |
| Actionable bounded errors | Stable error code, safe corrective guidance, retryability and attempt limit; no secrets or raw backend stack traces |

The schema-size target and the choice to annotate every tool are **lab design rules**, not MCP
requirements. Error hints must not suggest bypassing authorization. A permanent permission or schema
error must not trigger an unbounded retry. Do not claim idempotency just because the request has a key.

<a id="mcp-server-example"></a>
### Local server exercise: implement the real interface

Use the official Python SDK v2 and pin the exact installed version. Its migration guide documents
`MCPServer` and snake_case Python fields; protocol JSON still uses names such as `outputSchema`.
Older `FastMCP` tutorials require the corresponding v1 SDK or an explicit migration.

Expose `get_order(order_id)` over a local SQLite fixture and return a typed result containing only
fields available to the authenticated caller. Add a **simulated** refund only after the read-only
path works. The [reference contracts implementation](../../resources/agent-lab/contracts.py) is an
application backend, not an MCP server. Wire it into the SDK rather than inventing a protocol adapter.

For a write, the host must obtain confirmation for the exact tenant, operation and payload, record a
durable idempotency key and payload fingerprint, and apply the state change and replay record in one
transaction. Identical retries return the stored result; a reused key with changed arguments fails.
The local SQLite lab uses `BEGIN IMMEDIATE` to cover concurrent first writes. A real external side
effect also needs the external service's idempotency/transaction design. A model-supplied approval
flag is never the approval authority.

**Verify:** actual SDK client discovery and calls; typed structured output; unknown/malformed
requests; no unauthorized row access; approved/rejected simulated actions; replay after process
restart; concurrent first writes; and no duplicate side effect. Save a redacted protocol transcript.
A desktop commercial client is optional; the SDK client supplies the free route.

<a id="mcp-2026"></a>
### What the 2026-07-28 protocol actually changes

Use the [official changelog](https://modelcontextprotocol.io/specification/2026-07-28/changelog) and
[versioning rules](https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle).
“October 2026 MCP” describes a time of discussion, not a specification identifier.

| Concern | Released contract and learning check |
|---|---|
| Stateless protocol | Modern requests carry version/client capabilities in `_meta`; no modern initialize handshake or protocol session. Application state can live in an explicit durable store |
| Discovery | Servers implement `server/discover`; clients may call it first. `tools/list` is paginated, has cache metadata, and should be deterministically ordered |
| Authorization | Tool lists can depend on per-request authorization, not connection history. Scope caches accordingly; recheck invocation permissions |
| Results | Ordinary results use `resultType: complete`; validate `structuredContent` against `outputSchema` when provided. The lab requires output schemas although the protocol makes them optional |
| Hints | `readOnlyHint`, `destructiveHint`, `idempotentHint`, and `openWorldHint` are untrusted hints, not access controls |
| Compatibility | Record client SDK, server SDK, and protocol revision. Test old/new behavior only if claiming support; v2 has explicit legacy compatibility |
| Optional features | Tasks/MRTR and authorization extensions have their own contracts. Add them only for a corresponding use case |

**Progressive discovery:** compare a full small tool catalog with a namespaced catalog and selected
schema loading. This is an application pattern rather than a protocol guarantee. Keep fresh schemas,
authorization-sensitive caches, and a recovery path when a selected tool disappears. Measure tool
selection, schema tokens, latency, retries, and end-to-end success; fewer schemas may also hide a
needed capability. WebMCP, A2A and Agent Skills are separate interoperability depth topics.

## 🔓 Agent security — prompt injection is the threat model

Direct user input and indirectly retrieved documents can both contain malicious instructions.
Impact depends on privileges and data access, not on whether the injection was direct. Treat tool
outputs and stored memory as untrusted data. Enforce the boundary in code even when a model obeys
an injected instruction.

| Boundary | Concrete control |
|---|---|
| Caller/tenant | Trusted authentication, scoped queries and tool allowlists |
| Privileged action | Human approval bound to the exact action; no prompt-only permission checks |
| External I/O | Destination allowlist, credential scoping, response-size limits and timeouts |
| Code execution | No arbitrary execution in the core lab; isolated restricted runner for an extension |
| Tool/memory content | Provenance, data-role isolation, validation and bounded injection into context |
| Resource use | Total step/time/token budgets and bounded retries; record termination reason |

Filters may reduce unwanted outputs but do not establish an authorization boundary. A container by
itself is not a complete sandbox. Use [M23](../m23-ai-safety/README.md) to measure attack cases and
benign false blocks, and state what the controls do not cover.

## 📊 Agent evaluation

Score final **state** as well as the response: an agent saying “refunded” does not prove a fixture
row changed correctly. Record tool names/arguments, action counts, errors/retries, termination,
latency and resource use. Reuse the [shared harness](../m24-mlops-llmops-agentops/README.md#evaluation-harness).
Report per-task success and repeated-run reliability. `pass@k` means at least one successful attempt;
it is not the chance that every customer gets a correct first answer.

<a id="labs"></a>
## 🧪 Labs: one system, staged improvements

Use one small SQL-backed assistant and a 20-task development/evaluation split. All sizes and budgets
below are teaching defaults to record and adjust, not industry standards. Run deterministic contract
tests offline; run a real local model when measuring selection or answer quality.

<a id="start-lab"></a>
<a id="lab-1"></a>
### Lab 1 · A bounded loop and deterministic baseline

Implement the fixed workflow first. Then let a model propose typed tool requests. The host validates
and dispatches only allowlisted tools, appends results as data, and terminates on a valid final answer
or budget exhaustion. Start with eight tool attempts; count failed attempts too. Apply per-call I/O
timeouts and a total elapsed budget. A between-call clock check cannot interrupt a blocked network call.

**Done:** unknown tool, wrong argument type, malformed JSON, refusal, timeout, repeated failure and
step exhaustion all have tests. Compare the real model with deterministic routing on the same tasks.
The [scripted runner](../../resources/agent-lab/contracts.py) supplies control tests, not the model loop.

<a id="lab-2"></a>
### Lab 2 · Reusable instructions — optional Agent Skills extension

Create one domain-specific skill following the [Agent Skills specification](https://agentskills.io/specification).
Use precise activation metadata and only the needed instructions/scripts. A skill is a distribution
format, not a privilege grant; review executable content before use and preserve tool authorization.

**Done:** compare relevant and irrelevant tasks with/without the skill; report convention violations,
incorrect activation and context cost. A null or negative result is acceptable. Do not require one
particular commercial coding assistant to run the experiment.

<a id="lab-3"></a>
### Lab 3 · Structured calls and failure contracts

Compare prompt-only JSON, validation with bounded retry, and local constrained decoding using
[Outlines](https://dottxt-ai.github.io/outlines/latest/). The
[OpenAI](https://developers.openai.com/api/docs/guides/structured-outputs) and
[Anthropic](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) docs provide
optional provider comparisons. Check supported JSON Schema features and output completion/refusal
status; then validate application meaning and permissions independently.

**Done:** report parse/schema errors, semantic errors, retries and latency over a fixed task set.
Use a small real local model for this comparison. A scripted valid JSON response cannot demonstrate
a decoding algorithm's advantage. Constrained syntax does not make an order ID correct or authorized.

<a id="lab-4"></a>
### Lab 4 · Working context and progressive discovery

Use [write/select/compress/isolate](https://www.langchain.com/blog/context-engineering-for-agents)
as candidate strategies. Keep a compact current task state, retrieve needed tool schemas/documents,
summarize old observations at a declared threshold, and isolate independent subtasks only if useful.
Evaluate distractor tools and a required tool omitted by retrieval; support recovery or abstention.

<a id="compounding-errors"></a>
If each of n necessary steps independently succeeds with probability p, all succeed with probability
pⁿ; for example 0.95¹⁰ ≈ 0.599. Real failures are dependent and agents may recover, so this illustration
is not a measured agent reliability estimate. Measure complete tasks and their actual recovery paths.

**Done:** before/after table for task success, tool selection, context tokens, latency and total
resource use. Do not add 30 tools solely to satisfy a count; use a reproducible distractor catalog.

<a id="lab-5"></a>
### Lab 5 · Three memory tiers with provenance and forgetting

| Tier | Contents | Minimal implementation |
|---|---|---|
| Working | Current instructions, task, recent turns, selected observations | Bounded message context with source labels |
| Episodic | Session summary, unresolved goals, pending approvals, checkpoint | Versioned JSON/SQLite checkpoint; retain source-event IDs |
| Semantic | Durable user/entity facts and retrieval metadata | Tenant-scoped store with observed time, expiry, provenance and conflict policy; embeddings added after correctness |

There is no universal “breaks at session 50” or 400 ms threshold. Measure the workload. Summaries may
lose facts, vector retrieval may miss relevant facts, and full history may be the simplest adequate
baseline for a short session. Separate trusted user statements from facts extracted from external text.

Use the [local memory contracts](../../resources/agent-lab/contracts.py) to test concurrent first
writes, late arrivals, same-time conflicts, tenant isolation, expiry and deletion. Timestamp order
uses trusted source-event time, not arrival time or a model-invented date. The fixture intentionally
stores current facts only; add history/provenance for audit when needed. PostgreSQL row locks alone
do not lock an absent fact row; use an appropriate unique/transaction strategy and test races.

**Done:** replay a synthetic multi-session history with changed preferences, an expired fact, a
conflicting duplicate, malicious retrieved text and another tenant's facts. Compare full history,
rolling summary, and summary plus fact retrieval on the same probes. Count correct, stale, missing
and unauthorized recalls. A semantic-retrieval claim needs a real embedding/ranking implementation;
exact-key fixture tests cover persistence controls only. Record deletion behavior for indexes,
logs/caches/backups and queued events; deleting a row alone is not a complete erasure workflow.

<a id="multi-agent-next"></a>
## Optional next step: multiple agents

After the single-workflow baseline, test one router/worker/checker split on tasks with independent
subproblems. LangGraph, CrewAI and other frameworks are choices, not curricular requirements.
Evaluate coordination failures, citation provenance, shared-state races, tokens and wall time.
GAIA/SWE-bench or browser benchmarks are specialist extensions with their own environment costs;
small subsets do not establish leaderboard-comparable performance.

<a id="completion"></a>
## 📦 Required completion evidence

Submit the actual MCP SDK server/client, bounded assistant, frozen tasks, deterministic contract
tests, real-model comparison, traces, memory design/tests, README and results memo. One system covers
all core outcomes; Lab 2 and multi-agent/public-benchmark extensions are optional. Schemas and controls
must work, but the model is allowed to perform poorly if the evaluation explains it honestly. Private,
selectively shared, and sanitized public artifacts all meet the reviewability requirement.


---

**After the core:** record the artifact, remaining gap and next task in the [tracker](../../guides/progress-tracker.md#resume), then return to your [chosen route](../../guides/practitioner-track.md#role-pathways). Revisit only the missing skill with the [readiness pattern](../../guides/readiness-checks.md#how-to-check).
