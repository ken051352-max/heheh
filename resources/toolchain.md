[Home](../README.md) · [Module defaults](../guides/how-to-read-a-module.md#pick-one)

<a id="toolchain"></a>
# Tools by learning stage

Install tools when a project needs them. The default is a local, reproducible project with a small dependency set. Free lectures do not require paid APIs, cloud subscriptions or a guaranteed free GPU. Books are selected separately in the [catalogue](books.md).

**Compatibility policy:** use Python 3.12 or a newer version supported by all selected dependencies. Pin the interpreter and resolved packages in each project; do not interpret a major-version family below as a tested combination. Follow the documentation for the installed release, record the environment and upgrade deliberately. Course notebooks can need a separate environment.

## Start small, then add one capability

| Stage | Default tools | What earns completion; alternatives and boundaries |
|---|---|---|
| M1 Python | Python standard library, an editor, Git when ready; `uv`, `pytest`, Ruff | Write the starter CLI before adding frameworks. Use fixtures and mocked failures, format/lint, and explain the code. `venv` + pip is a valid fallback. A paid editor or coding assistant is unnecessary. |
| M1 HTTP and typed data | HTTPX, Pydantic v2, `asyncio` | Validate data at the boundary, define explicit connect/read/write/pool timeouts, and bound concurrent work with `asyncio.Semaphore`. A semaphore limits concurrency, not requests per second; total deadlines and bounded retries are separate. Test offline with mock responses. Pydantic coercion is configurable: validate strictness, ranges and business rules deliberately. |
| M2–M5 numerical foundations | NumPy, Matplotlib; notebooks as scratch space | Compare numerical results with derivations and small analytic examples. Keep reusable functions and tests outside the notebook. Jupyter is sufficient; reactive notebooks are optional. |
| M6/M6½ inference and causality | NumPy/SciPy where needed; the [stdlib causal lab](local-labs/README.md) first | Define the estimand and identification assumptions before using an estimator. DoWhy/EconML are optional extensions, not substitutes for identifying confounding and testing design assumptions. |
| M7 wrangling | pandas, NumPy, Matplotlib/seaborn | Explicit types, missingness, joins, duplicate handling and data tests. Add Polars or DuckDB only for a stated query/performance question and measure against a baseline. |
| M8a SQL and warehouses | SQLite for initial queries; local PostgreSQL for the full SQL project | Submit DDL/migrations, integrity/data tests and before/after query plans. PostgreSQL `EXPLAIN ANALYZE` executes the statement: use disposable data, especially for writes. dbt Core adds tested transformations later; managed dbt services are optional. |
| M8b data pipelines | [SQLite event-replay lab](local-labs/README.md), optional DuckDB backend | Start with keys, replay, late data and quarantine. Then choose Spark with Iceberg **or** Delta Lake for a separate systems experiment; consult that release's Python/JVM/Scala/table-format matrix. Spark 3.5+ describes the curriculum's API family, not a claim that all newer releases or connectors interoperate. |
| M8b interoperability/streaming | Arrow, then Kafka and **one** of Dagster/Airflow when the lab needs them | Arrow is an interchange/columnar-memory layer; a table format, query engine, broker and scheduler solve different problems. A local broker or Docker Compose exercise demonstrates its configured failure model; SQLite replay does not establish distributed exactly-once behavior. |
| M9–M12 classical ML | scikit-learn `Pipeline`, NumPy reference exercises | Fit preprocessing on training folds only; compare dummy/heuristic baselines, retain a final holdout and report task-aligned metrics/error slices. Choose one boosting library if needed. Framework or leaderboard popularity is not an evaluation result. |
| M13 Bayesian modeling | PyMC 5.x + ArviZ | Prior/posterior predictive checks, multiple chains, rank-normalized R-hat, ESS and divergences. NumPyro/JAX or Stan is an alternative implementation route. A diagnostic threshold alone does not establish a valid model. |
| M14 forecasting | Transparent seasonal-naive baselines and a compatible forecasting library | Rolling-origin backtests, interval coverage and reconciliation. FPP3 teaches with R; preserve the statistical design when implementing in Python. Conformal coverage depends on assumptions and does not automatically transfer to arbitrary drifting series. |
| M15–M17 DL/RL | PyTorch 2.x, CPU-sized data/models first | Autograd, `gradcheck` for custom operations, controlled seeds and held-out evaluation. Use `torch.autocast`/`torch.amp` only where supported; bf16 is hardware-dependent. Add fast.ai as an applied course, or JAX/Keras as a chosen alternative, not another required framework. |
| M18 adaptation | Transformers + PEFT + TRL in a mutually compatible environment | Record the exact base model, tokenizer, adapter and dataset revisions. Compare SFT/LoRA/QLoRA or preference methods with a baseline and held-out eval. Hardware, model licenses and quantization support vary. Small-model experiments and mocks must be labeled accurately. |
| M18-app structured outputs | Local constrained decoding such as Outlines, plus application validation | JSON-schema conformance does not establish factual truth, authorization or safe actions. OpenAI/Anthropic structured-output APIs are optional paid-provider routes; consult model-specific support, refusal and truncation handling. |
| M21 retrieval | Lexical baseline, then local embeddings + LanceDB **or** PostgreSQL/pgvector | Freeze 20–50 evaluation cases; compare retrieval and no-retrieval baselines, hit@k, context precision and faithfulness. CPU feasibility depends on corpus/model size. A cross-encoder or visual-document retriever is an evaluated extension. |
| M22 agents/MCP | A bounded Python loop and the [offline contract lab](agent-lab/README.md) before a framework | Explicit tool allowlists, typed errors, trusted approvals, idempotency and isolated memory. MCP baseline: released **2026-07-28** specification and a compatible SDK; current Python SDK v2 documentation describes stateless operation. Record negotiated revisions. Tool-search and small schemas are design choices; annotations are hints, not authorization. |
| M23 safety/evals | Ordinary automated tests plus adversarial fixtures | Include prompt injection, poisoned retrieval and privilege escalation; maintain expected outcomes and failure regressions. OWASP/NIST guide coverage. Choose an evaluation framework only if it helps reproduce these checks. |
| M24 production | Container recipe, CI, artifact manifest/versioning, evaluation gates and rollback procedure | Follow the [12-item production bar](../curriculum/6-frontier-production.md#production-bar). Local logs/metrics are enough to begin; add MLflow/DVC/OpenTelemetry for a demonstrated need. GenAI semantic conventions are **Development**: pin their revision and isolate naming changes. Local reviewable demos are valid; public hosting and Kubernetes are optional. |
| M25/M26 communication | Markdown, charts and a decision memo; optional Zotero/LaTeX/Typst | State the decision, evidence, uncertainty and next action. Use the selected capstone rubric rather than collecting tooling badges. |

## A reproducible Python project

The following is a recipe for a **new learner project**, after Python/uv installation. It is not an instruction to initialize this documentation repository:

```text
uv init --python 3.12 my-project
cd my-project
uv add --dev pytest ruff
uv lock
uv sync --locked
```

Add your implementation and at least one meaningful test in `tests/` before verification. A newly initialized project has no tests yet; pytest reports that rather than a passing suite. Then run:

```text
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pytest
```

Add HTTPX/Pydantic or numerical dependencies only when needed. Commit `pyproject.toml`, `uv.lock`, the interpreter selection and any tool configuration. `--locked` fails if the lockfile needs updating; it does not mean dependencies are already cached or no network is needed. uv's lockfile documents resolution, while the installed environment still depends on the platform. See the [uv project guide](https://docs.astral.sh/uv/guides/projects/) and [locking/syncing](https://docs.astral.sh/uv/concepts/projects/sync/). This recipe was documentation-checked; this pass did not install every tool in the table.

For this repository's own checks, use [tools/README.md](../tools/README.md#install-ci). Reference tests and learner starter tests have different expectations.

## Record enough to reproduce the result

Include the code commit, interpreter/dependency lock, OS/CPU/RAM/GPU, random seeds, data provenance/license/split, model/tokenizer revision, command and evaluation configuration. Record throughput/latency together with workload, batch size, concurrency and warm-up; small runs cannot support precise tail-latency claims. Report failed attempts and uncertainty alongside successful runs.

Distinguish **measured local results**, **mock/fixture tests**, and **capacity estimates**. Prices and hosted free tiers change: record a dated price source only when calculating a real paid deployment. Use the [decision template](templates/DECISIONS.md) to explain why the next tool is justified.

## Documentation behind the choices

- [Pydantic strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/) and [HTTPX timeout types](https://www.python-httpx.org/advanced/timeouts/).
- [Spark installation/runtime compatibility](https://spark.apache.org/docs/latest/), [scikit-learn leakage guidance](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage) and [Stan diagnostic warnings](https://mc-stan.org/learn-stan/diagnostics-warnings.html).
- [PyTorch AMP](https://docs.pytorch.org/docs/stable/amp.html), [PEFT](https://huggingface.co/docs/peft/index) and [TRL](https://huggingface.co/docs/trl/index).
- [MCP tools specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) and [GenAI telemetry conventions/status](https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/README.md).

The [research record](../audit/research-2026-11-05.md) separates live source inspection from code executed locally. No version snapshot or product claim here is a permanent industry standard.
