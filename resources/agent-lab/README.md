# Local agent contracts lab

This small, standard-library-only lab demonstrates the application controls behind
[M22](../../coursepages/m22-agentic-ai/README.md),
[M23](../../coursepages/m23-ai-safety/README.md), and
[M24](../../coursepages/m24-mlops-llmops-agentops/README.md).
It makes **no model or network calls**. Refunds change only a temporary SQLite
fixture; no money moves. Scripted requests prove engineering contracts, not a
model's tool-selection accuracy, answer quality, or resistance to every injection.

From the repository root, run:

```bash
python -m unittest discover -s resources/agent-lab/tests -v
```

The tests cover unknown tools and invalid arguments, a trusted tenant boundary,
approval bound to the exact action, durable idempotency after restart, conflicting
replays, concurrent first writes, event-time memory conflicts, expiry, forgetting,
and step/deadline bounds. Every test uses a temporary database.

`contracts.py` is a reference to read and extend, not a complete production agent
or MCP server. `Principal` and approval creation belong to the trusted host;
never construct either from model output. `run_scripted` checks elapsed time
**between** local calls; real model/network adapters also need their own I/O
timeouts and cancellation. SQLite serializes these demonstration transactions;
a real external payment requires the provider's idempotency mechanism and a
transaction/outbox design, not just this database.

Memory here is exact-key storage. Add semantic retrieval only after these
tenant, provenance, event-time and retention contracts pass. An expiry removes a
fact from recall; `forget_tenant` deletes this lab's stored facts. A deployed
system must additionally handle its indexes, logs, caches, and backup policy.
This fixture has no deletion tombstone: a queued older event can recreate a
deleted fact. A real erasure workflow must reject stale ingestion after deletion;
passing this lab is not an erasure-compliance guarantee.

For the MCP exercise, use the official SDK, pin the protocol revision, and test
the real discovery/call wire behavior separately. This harness does not establish
MCP conformance. For the model exercise, run a real local model against frozen
tasks, compare with deterministic routing, and report failures as well as gains.
