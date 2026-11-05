# Module 21 — RAG, Vector DBs & Retrieval Systems

[Full module](../../curriculum/6-frontier-production.md#module-21) ·
[Learning contract](../../curriculum/README.md#learning-contract)

Retrieval helps when a task needs evidence outside the model's prompt or training. This lab asks
whether it helps **your** task, at what cost, and with which failures. Enterprise surveys, including
[Menlo's 2025 U.S. sample](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/),
are context rather than universal adoption statistics.

## Prerequisites and default route

M1 + M8a + [M18-app competence](../../curriculum/6-frontier-production.md#application-foundations)
(full M18 also covers it). M11 is recommended for vector geometry; study cosine similarity before
implementing dense retrieval.

| Resource | Role and access |
|---|---|
| [FSDL — Augmented Language Models](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/augmented-language-models/) | Free lecture; durable retrieval concepts, dated 2023 tooling |
| [Pinecone Learn](https://www.pinecone.io/learn/) | Free reference explanations; using Pinecone's service is unnecessary |
| [LlamaIndex docs](https://developers.llamaindex.ai/python/framework/) | Implementation companion when a framework becomes useful |
| [AI Engineering](https://huyenchip.com/books/) — Chip Huyen | Recommended main text, retrieval and evaluation chapters; paid book |
| [BGE model card](https://huggingface.co/BAAI/bge-small-en-v1.5) | CPU embedding baseline; read preprocessing and license |
| [pgvector](https://github.com/pgvector/pgvector) / [LanceDB](https://lancedb.com/) | Local storage choices; choose one |
| [ColBERT](https://github.com/stanford-futuredata/ColBERT) / [ColPali](https://github.com/illuin-tech/colpali) | Depth: text late interaction / visual document retrieval |
| [Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) | Source-specific experiment to reproduce, not a universal SOTA claim |

Start with 10–30 small, licensed text/Markdown documents and stable IDs. PDF parsing is a later
extension if the task needs it. Local BM25, BGE-small CPU embeddings, exact search or LanceDB, and a
small BGE cross-encoder provide the baseline. PostgreSQL/pgvector is the SQL alternative. No cloud
account is required. Cache downloaded model weights for offline runs and record hardware/runtime.

## Before building: choose the failure to address

| Evidence from your baseline | Candidate intervention |
|---|---|
| Wrong format or unclear instructions | Explicit contract, examples, constrained output |
| Missing authorized document evidence | Fixed context for tiny corpora, then retrieval |
| Irrelevant candidates | Ingestion/chunking, lexical/dense retrieval, filtering, reranking |
| Task behavior still poor with correct evidence | Model/prompt comparison or measured adaptation |

Measure each intervention. Fine-tuning and retrieval can complement each other; neither guarantees
truth. A larger model and more chunks can both increase cost without improving the selected task.

<a id="evaluation-harness"></a>
## 📏 Evaluating RAG: component and answer evidence

Use the [shared four-part harness](../m24-mlops-llmops-agentops/README.md#evaluation-harness).
Freeze **20–50 evaluation questions before tuning** and keep separate development questions.
Include exact identifiers, paraphrases, multi-document questions, stale/conflicting sources,
unanswerable questions, and inaccessible tenant documents. Label document IDs first so labels
remain meaningful when chunks change; map chunks back to those documents.

| Measurement | Definition and interpretation |
|---|---|
| Hit@k | Fraction of answerable queries with at least one relevant item in the top k |
| Recall@k | Retrieved relevant items / all labeled relevant items; requires adequate relevance labels |
| Context precision@k | Relevant retrieved items / returned items; report retrieval granularity and k |
| nDCG@k | Ranking quality when graded relevance labels are available; state the gain convention |
| Faithfulness | Supported factual claims / factual claims in the answer, against cited retrieved evidence |
| Answer correctness | Task-specific rubric or exact answer check; unsupported but correct guesses are separate |
| Abstention | Correct abstentions on unanswerable cases and false abstentions on answerable cases |
| Resources | Retrieval/reranker/generation latency, context tokens, peak memory and optional API cost |

Define the zero-denominator cases before scoring; an empty answer does not receive perfect
faithfulness by default. Citation presence is only a structural check: verify the cited passage
supports the claim. Human labels are a valid free grader. If using an LLM judge, reserve labeled
calibration/validation examples and report agreement and errors; do not let the judge see the desired
system identity. A small golden set supports regression work, not a population reliability claim.

## 📦 Required project — one reproducible retrieval comparison

1. **Ingest:** preserve source/license, document ID/version, page/section, and access metadata.
   Test empty input, duplicates, malformed documents, and re-indexing after an update.
2. **Compare:** run no retrieval, BM25, dense, hybrid RRF, and hybrid plus reranker over the same
   corpus and eval questions. Freeze candidate count, k, model, prompt, and decoding settings when
   comparing retrieval changes. Inspect exact search before claiming ANN improvements.
3. **Authorize:** apply access controls before candidates reach reranking, generation, or caches.
   Test that an unauthorized document is absent at every stage and in the final response.
4. **Evaluate:** score retrieval deterministically and answer quality from real model outputs.
   Repeat stochastic generation (start with five runs if feasible), report counts and variability.
   Scripted/mock responses validate integration only; they do not demonstrate RAG answer quality.
5. **Decide:** write a memo recommending the simplest configuration that meets the declared
   quality/resource budget, with concrete failure examples and reasons it might change.

**Done when:** a clean-clone command rebuilds the index and metrics from versioned inputs; tests pass;
the README contains the comparison table and limitations; the memo interprets the results. A result
where hybrid or reranking fails to improve is acceptable. Keep the repository private or share it
selectively if the corpus cannot be published; include a sanitized reproducible fixture.

**Optional depth:** add exactly one of contextual retrieval, query rewriting, GraphRAG,
ColBERT/ColPali, multilingual retrieval, or ANN scaling. Compare against the core baseline. Hosted
Cohere reranking is an optional paid comparison. A GPU or a paid judge must not become a core gate.
