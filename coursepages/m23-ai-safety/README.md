# Module 23 — AI Safety, Alignment, Interpretability, Evals & Policy

[Full module](../../curriculum/6-frontier-production.md#module-23) ·
[Executable control tests](../../resources/agent-lab/README.md)

## Prerequisites and route

Start application threat modeling after [M18-app](../../curriculum/6-frontier-production.md#application-foundations).
Complete M22 before tool-escalation labs. Mechanistic-interpretability extensions require M15–M16;
they do not gate application safety work.

| Resource | Role and access |
|---|---|
| [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) | Released application-risk reference, published August 2026 |
| [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) and [GenAI Profile](https://doi.org/10.6028/NIST.AI.600-1) | Voluntary risk framework; RMF1.0 is under revision |
| [Berkeley Understanding LLMs, Spring 2024](https://rdi.berkeley.edu/understanding_llms/s24) | Selected public videos on safety, evaluation and security; full graduate-course completion is not required |
| [BlueDot AI Alignment](https://bluedot.org/courses/alignment) | Alternative free course; full materials require a free account and cohort facilitation has separate terms |
| [Inspect AI](https://inspect.aisi.org.uk/) | Free evaluation framework |
| [Transformer Circuits](https://transformer-circuits.pub/) | Primary mechanistic-interpretability research |
| [AI Engineering](https://huyenchip.com/books/) — Chip Huyen | Principal recommended book for application evaluation and system design; paid |
| [Human Compatible](../../resources/books.md) / [The Alignment Problem](../../resources/books.md) | Additional book-length framing; paid |

A risk framework is a review aid, not proof of safety or legal compliance. Use current official
regulatory text for jurisdiction-specific mappings; record the version and uncertainty.

<a id="evaluation-harness"></a>
## 📏 A threat model connected to tests

Draw the path user → retrieved documents/memory → model → dispatcher → tools → storage/network.
List protected assets, trusted components, external inputs, credentials and possible side effects.
For each threat, record the attacker capability, enforced control, test, expected outcome, observed
result, owner and residual risk. Use NIST's Govern, Map, Measure, Manage functions as review prompts.

| Scenario | Deterministic assertion | Model-level evaluation |
|---|---|---|
| Direct instruction requests a forbidden action | Dispatcher denies it, no state change | Does the assistant refuse or safely redirect? |
| Indirect instruction hidden in retrieved content | Unapproved action/network destination remains inaccessible | Does the answer follow the document's malicious instruction? |
| Poisoned source or memory fact | Provenance/tenant/expiry rules hold; untrusted data cannot grant permissions | Does unsupported content contaminate the answer? |
| Sensitive-data or cross-tenant probe | Unauthorized records never enter retrieval/context/outputs | Does the model infer or disclose information it should not? |
| Tool-layer privilege escalation | Exact caller/action authorization and payload-bound approval | Does the agent repeatedly request prohibited tools? |
| Replay or resource exhaustion | One side effect per idempotency key; conflict, step and time limits | Can the agent finish/abstain within its budget? |

The [local contracts lab](../../resources/agent-lab/README.md) runs these application-boundary checks
with scripted requests. That is useful even when an injected model asks for the wrong action. It
does **not** establish that any real model resists prompt injection; report model-level results
separately. Filters and prompt wording cannot replace authorization, isolation or bounded execution.

Use the [shared evaluation harness](../m24-mlops-llmops-agentops/README.md#evaluation-harness).
Include benign requests and unseen attack variants. Report attack success and benign false-block
counts with denominators; a zero on a small fixture set is not a zero-risk claim. Define whether
success means an unsafe answer, a blocked attempt, data exposure, or an actual unauthorized action.

<a id="level-5-loops"></a>
## 🔁 Optimization loops and reward hacking — optional depth

An optimization agent can improve the measured score while degrading the intended outcome. Study
[DeepMind's specification-gaming examples](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/)
and [METR's reward-hacking report](https://metr.org/blog/2025-06-05-recent-reward-hacking/).

1. Keep scorer, held-out data, test fixtures and budgets inaccessible to the modifying agent.
2. Restrict edits to a declared surface, use isolated execution, and record every diff and result.
3. Compare experiments under the same compute/data budget and fixed evaluation protocol.
4. Check a separate held-out outcome that was not optimized; investigate divergence and suspicious gains.
5. Require human review of the concrete change before it reaches users or protected systems.

**Done:** demonstrate one scoring shortcut, show that the independent check detects it, and record
what an attacker could still change. A toy scripted optimizer can test isolation; claims about a
model's reward hacking require actual model runs. Benchmark anecdotes are not universal rates.

## 📦 Required project and completion rubric

Extend one existing application with the threat model and scenario matrix above. For a system
without tools, complete content/retrieval/data risks now and add tool tests at M22. Include a model
or system card with intended users, data/model provenance, limitations and observed failures.

**Done when:** tests run by one command, unauthorized side effects are absent in the recorded cases,
benign controls and held-out variants are evaluated, failures are documented, and a two-page memo
identifies the remaining risk and next action. A failed model-level mitigation may still be an
honest learning result when the application controls and evaluation are sound.

**Research extensions — choose one:** reproduce an induction-head result; train a small SAE and
validate candidate feature interpretations with interventions/counterexamples; investigate
activation patching; or evaluate a bounded optimization loop. Do not claim five labeled features
are definitively monosemantic. Broad alignment, interpretability, fairness, privacy, and governance
remain depth topics with their own methods and limitations.
