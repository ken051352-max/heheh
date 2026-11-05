[Home](../../README.md) · [Curriculum index](../../curriculum/README.md) · [Resume](../../guides/progress-tracker.md#resume)

# Module 8b — Distributed Data & Streaming Systems

**First task:** Run the SQLite replay fixture, predict the total after replay, and compare your prediction with the output.

[Check prerequisites](#entry-prerequisites) · [Start the lab](#start-lab) · [Completion evidence](#completion)

This page supports the linked module; it is not an additional course to finish. Optional extensions come after the core artifact.

[Curriculum specification](../../curriculum/2-statistics-and-data.md#module-8b) · [Learning contract](../../curriculum/README.md#learning-contract)

**Goal:** preserve correct results across replay, late data, schema changes and failures, then explain the guarantee at each boundary. A local exercise teaches contracts; it does not prove behavior under network partitions.

## One free route

Use the [DataTalks.Club Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) public videos for batch processing/Spark and streaming. Follow the local labs below instead of its cloud tasks; free cloud credits are not assumed. [Stanford CS246](https://web.stanford.edu/class/cs246/) provides public slides/assignments, while current recordings require enrolled-student Canvas access. Its free [*Mining of Massive Datasets*](http://www.mmds.org/) text adds partitioned-algorithm depth. Official [Spark](https://spark.apache.org/docs/latest/), [DuckDB](https://duckdb.org/docs/) and [Kafka](https://kafka.apache.org/documentation/) docs explain system behavior; they are references, not lecture courses. The [DataExpert handbook](https://github.com/DataExpert-io/data-engineer-handbook) is an optional community index, not evidence of industry consensus.

**Recommended principal book:** Reis and Housley's *Fundamentals of Data Engineering* (paid), for lifecycle and architecture decisions. Kleppmann/Riccomini's *Designing Data-Intensive Applications* and Akidau, Chernyak and Lax's *Streaming Systems* add systems depth. Match chapters to your edition; see the [book shelf](../../resources/books.md). Lecture access remains free.

<a id="start-lab"></a>
## Core lab: replayable local event pipeline

Start with the standard-library backend; no installation is needed. The [lab README](../../resources/local-labs/README.md) also documents DuckDB installation and `--backend duckdb`:

```bash
python resources/local-labs/distributed_data.py --backend sqlite
```

The generated fixture contains repeated event IDs, a late event and a malformed row. The local ledger validates input, quarantines invalid rows, detects conflicting duplicates, commits accepted events transactionally and produces a deterministic aggregate. Replaying a batch must leave row count and totals unchanged. It uses in-memory SQLite by default or DuckDB when installed, with the selected backend/version in its output. It needs no server, Docker, account or GPU. Matching these contracts does not imply equivalent query plans or performance between engines.

**Extend it into your artifact:** persist the database in a temporary directory; save output as Parquet; interrupt loading before/after commit and restart. Separate raw input, accepted rows, quarantine and aggregates. Record checksums, schema version and row counts. Never silently drop late events: choose retain/recompute, correction records or quarantine, and test that policy.

## Core comparison: local Spark

Choose a documented compatible runtime. For example, [Spark 4.0.1](https://spark.apache.org/docs/4.0.1/) documents Java 17/21, Scala 2.13 and Python 3.9+; this is a compatibility example, not a newest-release claim. Record actual Spark/Python/Java and storage-connector versions. Do not combine Spark and Iceberg/Delta releases by guessing.

Run Spark as `local[2]` on the same small Parquet fixture and compute the same per-key totals. Assert parity with DuckDB, then compare wall time, peak memory, partitions and startup overhead. Start with data that fits in memory; 10 GB is optional. One laptop result does not establish cluster scalability.

## Optional: choose one systems extension

| Extension | Local route | Failure evidence |
|---|---|---|
| Orchestration | One Dagster or Airflow workflow over local files | Failed task, retry, idempotent rerun and backfill |
| Lakehouse | Spark plus one supported Iceberg or Delta connector; local disk or MinIO | Upsert, schema evolution, snapshot/time-travel query and retention |
| Streaming | Kafka KRaft and a local consumer; Flink optional | Consumer restart/replay, duplicate input, late event, poison message and lag |

Use the project's official local quickstart or Docker Compose example and pin images. Document CPU/RAM, ports, volumes and cleanup; the core lab does not require these services. Distinguish Arrow's in-memory interchange from Parquet storage and Iceberg/Delta metadata.

For streaming, distinguish event time from processing time and explain the watermark policy. Kafka transactions do not make arbitrary database/API side effects exactly-once; state source, processor and sink guarantees separately. Use idempotent keys/transactions and inject faults at the sink boundary.

<a id="completion"></a>
## Done when

Keep runnable assertions for schema rejection, duplicate conflicts, replay invariance and late data. Compare Spark/DuckDB results; include a failure/recovery transcript. Submit topology, resource budget, pinned environment, README and a memo explaining local-experiment limits. A private artifact is sufficient.

<a id="entry-prerequisites"></a>
## Prerequisites

M1 and M8a. M4 helps with hashing/partitioning; async is useful for services but does not gate batch SQL/file pipelines.


---

**After the core:** record the artifact, remaining gap and next task in the [tracker](../../guides/progress-tracker.md#resume), then return to your [chosen route](../../guides/practitioner-track.md#role-pathways). Revisit only the missing skill with the [readiness pattern](../../guides/readiness-checks.md#how-to-check).
