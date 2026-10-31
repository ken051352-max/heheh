# DECISIONS.md: <project name>

> Copy this file into the root of your project repository. Add one entry per decision you'd defend in an interview, newest at the top. Never delete an entry; if you reverse a decision, add a new one that supersedes it.
> Template from the [Portfolio Spine](../../guides/portfolio-spine.md#decisions-template). Pattern: [Architecture Decision Records](https://adr.github.io/).

**Current level:** L1 / L2 / L3 / L4 / L5 · **Last updated:** YYYY-MM-DD

---

## Budgets (fill in before L1 ships, revisit at every level)

| Budget | Target | Measured (date) | How measured |
|---|---|---|---|
| p95 latency per task | e.g. < 4 s | | traces / logs |
| Cost per successful task | e.g. < $0.01 | | token logs × price sheet dated ____ |
| Eval pass rate (N runs per case) | e.g. ≥ 90 % over 5 runs | | `make eval` |
| Max agent steps (L3+) | e.g. 8 | | step counter |

## Cost and scaling calculation

```
input_tokens  = ____   output_tokens = ____   (per request; agents: summed over all steps)
price_in      = $____ / 1M tokens   price_out = $____ / 1M tokens   (looked up: YYYY-MM-DD, source: ____)
cost_per_request    = ____
requests/user/day   = ____
cost_per_user_month = ____
```

| Users | Requests/day | Monthly cost | p95 latency | What breaks first and what I'd change |
|---|---|---|---|---|
| 1× | | | | |
| 10× | | | | |
| 100× | | | | |

---

## D-001 · <short title, e.g. "Vector store: pgvector instead of Qdrant">

- **Date / level:** YYYY-MM-DD · L2
- **Context:** What problem forced a choice? What constraints apply (data size, budget, latency, privacy, skills)?
- **Options considered:**
  1. Option A: pros / cons
  2. Option B: pros / cons
  3. The "do nothing / simplest thing" option: pros / cons
- **Decision:** What you chose.
- **Evidence:** A number, not a feeling. For example: eval pass rate, recall@5, p95 latency or cost per task, before vs after.
- **Consequences:** What gets easier, what gets harder, and what would make you revisit this decision.

<!--
Required entries by level (see the Portfolio Spine):
L1  model tier · output schema + validation · retry/fallback policy
L2  database / vector store · chunking · embedding model · RAG vs prompting vs fine-tuning
L3  tool list + which are read-only · step limit · approval gate for writes
L4  agent topology · per-agent context · guardrail placement · deployment target
L5  the metric · what makes it hard to game · what a human still approves
-->
