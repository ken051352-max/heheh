# Local causal and data-system labs

Small deterministic fixtures for [M6½](../../coursepages/m6h-causal-inference/README.md) and [M8b](../../coursepages/m8b-distributed-data/README.md). No hosted service, GPU, paid API or dataset download is required. Python 3.12+ is the roadmap baseline.

## Run from the repository root

Both the causal lab and the default SQLite ledger use only the Python standard library:

```bash
python resources/local-labs/causal_inference.py
python resources/local-labs/distributed_data.py --backend sqlite
```

For the DuckDB lab, create an isolated environment and install its single dependency:

```bash
python -m venv .venv-local-labs
```

PowerShell:

```powershell
.venv-local-labs\Scripts\python -m pip install -r resources/local-labs/requirements.txt
.venv-local-labs\Scripts\python resources/local-labs/distributed_data.py --backend duckdb
```

Linux/macOS:

```bash
.venv-local-labs/bin/python -m pip install -r resources/local-labs/requirements.txt
.venv-local-labs/bin/python resources/local-labs/distributed_data.py --backend duckdb
```

The SQLite route needs no installation or network. Installing DuckDB needs network access once. Record `python --version` and the backend/version printed by the lab; requirements express compatibility, not an exact lock. Pin the version you actually test. Identical ledger totals establish these small data contracts, not equivalent SQL dialects, storage engines, query plans or performance.

## What the results mean

- **Causal:** truth is ATE = 2 for a known 50/50 binary-confounder target population. A naive observational contrast is biased; stratified adjustment targets the known effect under the generator's assumptions. Wald coverage and normal-theory sample size are approximations, reported with Monte Carlo uncertainty. The exact noiseless contrast is checked. This is an identification demonstration, not a causal conclusion about real people.
- **Data pipeline:** accepted totals are `A: 400` cents after either the first load or a replay. One malformed row is quarantined; one late event is retained. Identical duplicates are ignored, conflicting IDs roll back the batch, and assertions prove the earlier insert in that failed batch was rolled back. This models an immutable event ledger, not updates to mutable entities.

Both print JSON to stdout and create no output files. Save a transcript in your own artifact. The coursepages specify the extensions and decision memo needed for module completion; running a supplied example alone is not completion.

Run the regression suite from the repository root with `python -m unittest discover -s resources/local-labs/tests -v`. Six causal tests and six SQLite ledger contracts run with the standard library. The same six ledger contracts run against DuckDB when installed; otherwise the output explicitly reports six skips. Skipped DuckDB contracts have not been verified on that machine. CI installs the lab requirements to exercise both backends.

## Limitations to investigate

The causal generator fixes population stratum weights, assumes observed confounding and checks neither real-data exchangeability nor interference. The ledger runs in one in-memory process; process restart, durable checkpoints, Parquet and Spark parity are learner extensions. Event times are normalized to fixed-width UTC ISO strings for this portable contract, not stored in an engine-specific timestamp type. Its late-event count compares arrival order to the current maximum timestamp, not a streaming-engine watermark. Quarantine is reported per run and is not persisted. Explain these boundaries before proposing production use.
