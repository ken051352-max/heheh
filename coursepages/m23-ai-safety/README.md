# Module 23 — AI Safety, Alignment, Interpretability, Evals & Policy

> **Status:** v2026.3 scaffold · full spec in the root [README.md § Module 23](../../curriculum/6-frontier-production.md#module-23).

## Why this module exists

No serious 2026 AI/ML role is hired without alignment and safety literacy. MIT AI Safety Forum + Berkeley MIDS + AISF Alignment Fundamentals all cover this. Closes Gaps #6, #12, and #13 of the benchmark PDF.

## Primary anchors (P1-verified)

| Resource | Role | Link |
|---|---|---|
| AI Safety Fundamentals — Alignment Track (Bluedot Impact) | Primary course, free | <https://bluedot.org/courses/alignment> |
| AISF Governance Track | Policy complement | <https://bluedot.org/courses/ai-governance> |
| Anthropic Transformer Circuits | Mechanistic interpretability | <https://transformer-circuits.pub/> |
| Scaling Monosemanticity (Templeton et al., 2024) | SAE on Claude 3 Sonnet | <https://transformer-circuits.pub/2024/scaling-monosemanticity/> |
| Golden Gate Claude | SAE public demo | <https://www.anthropic.com/news/golden-gate-claude> |
| OpenAI evals | Eval framework | <https://github.com/openai/evals> |
| lm-evaluation-harness (EleutherAI) | Canonical harness | <https://github.com/EleutherAI/lm-evaluation-harness> |
| HF Open LLM Leaderboard | Public leaderboard | <https://huggingface.co/open-llm-leaderboard> |
| EU AI Act | Regulation | <https://artificialintelligenceact.eu/> |
| NIST AI RMF + GenAI Profile | US framework | <https://www.nist.gov/itl/ai-risk-management-framework> |
| AI.gov | US federal portal | <https://ai.gov/> |
| EleutherAI Cookbook | Practical reference | <https://github.com/EleutherAI/cookbook> |

<a id="evaluation-harness"></a>
## 📏 Evals as a safety tool

Safety evals use the same [4-part harness](../m24-mlops-llmops-agentops/README.md#evaluation-harness) with adversarial golden sets: prompt injections hidden in retrieved documents, requests that exceed tool permissions, and data-exfiltration attempts. [Inspect AI](https://inspect.aisi.org.uk/) (UK AISI, MIT) is the free framework built for this. Grade with **code wherever possible** (did a forbidden tool get called? did secret text appear in the output?), and calibrate any LLM judge against human labels before trusting it.

<a id="level-5-loops"></a>
## 🔁 Self-improving loops and reward hacking (Portfolio Spine L5)

**The pattern (W3, 08:19–09:18):** an agent reads the system's current performance, proposes a change, makes it, tests whether it helped, and keeps or discards it, for hours or days without a human. The reference example is Andrej Karpathy's **[`autoresearch`](https://github.com/karpathy/autoresearch)** (March 2026). An agent edits a single `train.py` from [nanochat](https://github.com/karpathy/nanochat), trains for a **fixed 5-minute budget**, and keeps the change only if **validation bits-per-byte** improves. That gives about 12 experiments an hour. Karpathy reported a run of about 2 days on a depth-12 model that found **~20 changes that improved validation loss** ([post](https://x.com/karpathy/status/2031135152349524125)). Secondary write-ups put it at about 700 experiments.

**The catch (W3, 09:18–09:47):** the loop only works if the agent's scoring is right. If it's even slightly off, the agent improves the score instead of the product. That is **specification gaming**, or **reward hacking**:

- [DeepMind, *Specification gaming: the flip side of AI ingenuity*](https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/): the canonical taxonomy and examples.
- [METR, *Recent Frontier Models Are Reward Hacking*](https://metr.org/blog/2025-06-05-recent-reward-hacking/) (June 2025): frontier models on real tasks tampered with scoring code, monkey-patched evaluators and special-cased tests.
- [Anthropic, *Natural emergent misalignment from reward hacking*](https://www.anthropic.com/research/emergent-misalignment-reward-hacking): reward hacking learned in coding environments generalised into broader misbehaviour.

**Design rules for a loop the agent can't game** (from autoresearch's design and the sources above):

1. **Freeze the judge.** The scorer, evaluation data and time budget are **read-only** to the agent. In `autoresearch`, `prepare.py` (data and evaluation) is never modified; only `train.py` is.
2. **Make experiments comparable.** Use a fixed compute or time budget and a metric that can't be inflated by changing the setup (for example bits-per-byte, which doesn't depend on vocabulary size).
3. **Keep a held-out check the agent never sees**, and alert when the optimised metric and the held-out metric diverge.
4. **Sandbox it, with least privilege.** No network or credentials beyond what the experiment needs; run it in a container or VM ([M22 agent security](../m22-agentic-ai/README.md#-agent-security--prompt-injection-is-the-threat-model)).
5. **Instrument everything.** You can't watch it live, so keep every diff, score and log. Read the trail, not the summary (W3, 09:47).
6. **Humans pick the problem, design the scorer and approve what ships** (W3, 10:03). Spot-check accepted changes for test special-casing.

## Mandatory mini-projects

1. Reproduce an induction head on a 2-layer attention-only toy transformer (Transformer Circuits).
2. Train a Sparse Autoencoder on GPT-2 small activations; label 5 monosemantic features.
3. Red-team an open model with `garak` or hand-crafted GCG suffixes; write a 2-page eval report with model card.
4. Draft an EU-AI-Act-compliant model card for a hypothetical general-purpose AI model.

## Prerequisites

- Module 18 (LLMs, RLHF), Module 22 (agents)
