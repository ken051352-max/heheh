[🏠 Roadmap home](../README.md) · [🧭 Start here](../START-HERE.md) · [🗓️ Four-Year Plan](four-year-plan.md#flagship-projects) · [🚀 Fast lane](practitioner-track.md#practitioner-track)

---

<a id="portfolio-spine"></a>
# 🧱 The Portfolio Spine: one system, five levels

**The idea in one sentence:** instead of four unrelated toy projects, build **one** AI system for a real problem and grow it through five levels of engineering. Each level is a release of the *same* repository.

Hiring managers learn almost nothing from course exercises or Kaggle notebooks where the problem, data and metric were all handed to you (Video 1, 06:09–06:46). They learn a lot from a system that grew over time, with tests, evals and written trade-offs (W2, 03:40–04:42; W3, 00:12–10:30).

> **When to start:** after the [3-check gate](../curriculum/1-foundations.md#three-check-gate). Level 1 needs skill groups 1–4 from [M1](../curriculum/1-foundations.md#python-skill-groups). Levels 2–4 run alongside [M21](../curriculum/6-frontier-production.md#module-21)–[M24](../curriculum/6-frontier-production.md#module-24).
>
> **How this fits the other plans:** the spine **is** the AI-engineering flagship. In the [Four-Year Plan](four-year-plan.md#flagship-projects) it is P5 (L1–L2) → P7 (L3–L4). In the [fast lane](practitioner-track.md#practitioner-track) it is Stages 5–6. It *replaces* the separate M21/M22 mini-projects; it doesn't add to them.

---

<a id="pick-a-problem"></a>
## Step 0 · Pick one real problem

Pick something with a **real user** (you count) and **data no model has seen**. The two examples from the source videos:

- **Nutrition / meal-planning coach** (W3): your own meal logs and family recipes → weekly menu → grocery list.
- **Support assistant for a small online shop** (Video 1, 06:46): order lookups, a refund policy, ticket routing.

Other good fits are a study assistant over your university's regulations, a runbook assistant over an open-source project's docs, or a club's event and membership helper. See [build for real people](career-operations.md#5-build-for-real-people-not-for-datasets).

---

<a id="levels"></a>
## The five levels

| Level | You ship | Skills it proves | Exit criterion (all must hold) | Course page |
|---|---|---|---|---|
| <a id="level-1"></a>**L1 · API wrapper + structured output** | A Python script, then a small Streamlit/Gradio UI, calling one LLM API on your real task | HTTP + JSON, API keys from the environment, **schema-validated output**, retries/fallback when the model flakes | Output parses against a schema on 100 % of 20 test inputs; one test per failure mode (timeout, bad JSON, refusal); key never in git | [M1 groups](../curriculum/1-foundations.md#python-skill-groups) · [M22 Lab 3](../coursepages/m22-agentic-ai/README.md#lab-3) |
| <a id="level-2"></a>**L2 · Custom-data RAG + evals** | L1 connected to *your* documents (logs, recipes, policies) | Chunking, embeddings, a vector store, retrieval; **an eval set and an LLM judge**; knowing *when* RAG beats prompting or fine-tuning | A 20–50-case [golden set](../coursepages/m21-rag-vector-dbs/README.md#evaluation-harness); retrieval metric + answer metric reported against a no-RAG baseline | [M21](../coursepages/m21-rag-vector-dbs/README.md#evaluation-harness) |
| <a id="level-3"></a>**L3 · Read-only-first ReAct agent** | L2 given tools: search your logs, a calculator, web search. **Read-only first** | The ReAct loop, termination and step limits, tracing; *then* gated write actions with human approval | Raw loop written by hand once ([Lab 1](../coursepages/m22-agentic-ai/README.md#lab-1)); traces for every run; pass rate over N runs reported; no write tool until reads are reliable | [M22](../coursepages/m22-agentic-ai/README.md#labs) |
| <a id="level-4"></a>**L4 · Multi-agent router / worker / checker** | L3 split into a **router**, domain **workers** (e.g. planner and grocery builder) and a **checker** that reviews output before the user sees it | Context isolation, tracing across agents, prompt-injection and data-leak guardrails, **adversarial fault tests**, a container deployment, cost and latency budgets | Fault-injection suite passes (e.g. feed the planner a fake ingredient; the checker must catch it); p95 latency and cost per task within the budgets in `DECISIONS.md` | [M22](../coursepages/m22-agentic-ai/README.md#lab-4) · [M24](../coursepages/m24-mlops-llmops-agentops/README.md#evaluation-harness) |
| <a id="level-5"></a>**L5 · Self-improving loop** *(optional, advanced)* | An agent that proposes a change, runs it, scores it, and keeps or discards it, in a sandbox | **A metric the agent can't game**, full execution trails, and clearly defined human checkpoints | Scorer and test data are read-only to the agent; held-out checks catch metric gaming; a human approves anything merged | [M23](../coursepages/m23-ai-safety/README.md#level-5-loops) · [M24](../coursepages/m24-mlops-llmops-agentops/README.md#evaluation-harness) |

**Be honest about levels 4 and 5.** Even senior production work is often level 2 or 3: "we're hired to be useful, not fancy" (W3, 10:18–10:30). Level 5 is for study and small sandboxed experiments. The skills it needs come from years of running systems in production (W3, 10:08–10:18).

<a id="level-rules"></a>
### Rules that apply at every level

1. **One repository, tagged releases.** Tag `v1-api`, `v2-rag`, `v3-agent`, `v4-multi`. The git history *is* the story you tell in interviews.
2. **Evals before features.** You can't move to a new level until the current one has an eval suite that runs with one command and in CI. See the [evaluation harness](../coursepages/m24-mlops-llmops-agentops/README.md#evaluation-harness).
3. **Simplest version first.** Write a raw loop before adopting a framework, use simple search before a vector DB, and use one agent before several. Adopt a framework only when you can say what it saves you (Marina Wyss, [*SWE → AI Engineer roadmap*](https://www.marinawyss.com/blog/software-engineer-to-ai-engineer-roadmap)).
4. **Meet the [Minimum Production Bar](../curriculum/6-frontier-production.md#production-bar).** Items 1–4 always apply; items 5–12 apply from L2 onwards.
5. **Keep a `DECISIONS.md`.** This is mandatory. Use the template below.

---

<a id="decisions-template"></a>
## 📝 The mandatory `DECISIONS.md`

Video W2 (07:21–08:05): *"as you build things, write up the trade-offs as you go: why this database and not that one, why this model, how would you calculate costs and what would happen to those costs if you got way more users."* This file is how you build that judgment, and it gives you something concrete to talk through in interviews.

**Copy the template:** [`resources/templates/DECISIONS.md`](../resources/templates/DECISIONS.md). Each entry follows the [Architecture Decision Record](https://adr.github.io/) pattern: context, options, decision and consequences. Add one entry each time you make a choice you could defend in an interview.

**Required entries by level:**

| Level | You must record |
|---|---|
| L1 | Model tier (accuracy vs latency vs price), output schema and validation strategy, retry/fallback policy |
| L2 | Database or vector store (e.g. pgvector vs Qdrant vs LanceDB vs "none, BM25 is enough"), chunking strategy, embedding model, why RAG instead of prompting or fine-tuning |
| L3 | Tool list and **which tools are read-only**, step limit, approval gate for writes |
| L4 | Agent topology, what each agent can see (context isolation), guardrail placement, deployment target |
| L5 | The metric, what makes it hard to game, what a human still approves |

<a id="cost-math"></a>
### The cost and latency calculation (every level from L1)

Write this out with **your own measured numbers** and **current list prices**. Prices change, so record the date you looked them up.

```
tokens_per_request  = input_tokens + output_tokens          (measure from logs; agents: sum over all steps)
cost_per_request    = input_tokens  × price_in_per_token
                    + output_tokens × price_out_per_token
                    + retrieval/tool/infra cost per request
cost_per_user_month = cost_per_request × requests_per_user_per_day × 30
monthly_cost(N)     = cost_per_user_month × N_users
```

Then fill in the scaling table and state **what changes your design** at each step:

| Users | Requests/day | Monthly LLM cost | p95 latency | What breaks or changes first |
|---|---|---|---|---|
| 1× (today) | | | | |
| 10× | | | | e.g. rate limits → add a queue and caching |
| 100× | | | | e.g. cost → route easy queries to a smaller model, cache embeddings, batch |

**Worked shape (made-up numbers, not real prices):** 3,000 input + 500 output tokens per request, at a hypothetical $1 and $4 per million tokens, gives ≈ $0.005 per request. At 10 requests per user per day that is ≈ $1.50 per user per month. At 100× users the *design* question becomes whether a cache hit rate of 40 % or a smaller model on easy queries keeps the unit cost flat. A multi-agent L4 can multiply tokens per task several times over; Anthropic reports its multi-agent research system used about 15× the tokens of chat ([source](https://www.anthropic.com/engineering/built-multi-agent-research-system)). Put that multiplier in the table before you choose L4.

---

[🏠 Roadmap home](../README.md) · [📝 DECISIONS template](../resources/templates/DECISIONS.md) · [🔬 v2026.7 research findings](../audit/v2026.7-research-findings.md#portfolio)
