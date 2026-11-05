[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [← 🟩 Foundations (M0–M5)](1-foundations.md) · [🟧 Classical ML (M9–M12) →](3-classical-ml.md)

---

# 🟨 CORE STATISTICS STRATUM (Modules 6–8)

[M6: Inference](#module-6) · [M6½: Causal inference](#module-6-half) · [M7: Data investigation](#module-7) · [M8a: SQL](#module-8a) · [M8b: Distributed data](#module-8b)

**Do now:** select one module whose strict prerequisites you can demonstrate. **Next:** its core project and [readiness pattern](../guides/readiness-checks.md#how-to-check). **Later depth:** the expanded topic maps and optional systems/tool comparisons. First-semester learners follow the [conditional SQL preview](../guides/first-semester.md#week-15) after M1, not this entire stratum.

<img src="../assets/stratum-2-statistics.jpg" alt="Statistics and data stratum, modules 6 to 8" width="100%">

> **Reading this page:** each module lists many resources — that is a menu, not a to-do list. Take **one** primary course; see the [resource defaults](../guides/how-to-read-a-module.md#pick-one). Citations like *"Video 1 (05:05)"* are resolved in [sources](../guides/sources.md#citation-key).

---

<a id="module-6"></a>
## Module 6: Statistical Inference

**Recommended principal reading:** Larry Wasserman, **All of Statistics** (Springer, paid): estimation, uncertainty and inference. Work selected inference chapters alongside free MIT 18.650 lectures; Casella and Berger is graduate-theory depth.

**Core outcome:** define an estimand; implement an estimator and interval; test calibration by simulation; write an effect-size/uncertainty decision memo. Percentile bootstrap, Welch test, permutation test and one multiplicity correction are core. BCa/asymptotic proofs are optional depth.

* **The Tutor's "Why":** Inference turns sample evidence into estimates and decisions with stated uncertainty. Learn when an estimator, interval or test answers the actual question and when its assumptions fail.

* **Strict Prerequisites:** Module 5 core (conditional probability, expectation/variance, sampling and CLT). MGFs and asymptotic proofs are optional mathematical depth.

<details>
<summary>Topic map and later depth — use the core outcome above to choose scope</summary>

* **Topic map (core plus optional depth; roadmap synthesis):**
  * Statistical models (parametric, non-parametric, semi-parametric); estimators and their properties — unbiasedness, consistency, efficiency, sufficiency (Neyman-Fisher factorisation), completeness, Rao-Blackwell theorem, Lehmann-Scheffé theorem; Cramér-Rao lower bound.
  * **Maximum Likelihood Estimation** — construction, invariance, asymptotic normality, Fisher information, observed vs expected information; **Method of Moments**; delta method.
  * **Parametric hypothesis testing** — null vs alternative, Type I / Type II errors, power, size, Neyman-Pearson lemma, Likelihood Ratio Test (Wilks' theorem), Wald test, score test.
  * Confidence intervals — construction by pivoting, Wald CIs, likelihood-based CIs, bootstrap CIs.
  * Goodness-of-fit tests — chi-squared test, Kolmogorov-Smirnov test, Anderson-Darling.
  * Linear regression inference — Gauss-Markov theorem proof, sampling distribution of β̂, ANOVA decomposition (SST = SSR + SSE), F-test for nested models.
  * Review of Stat 110 concepts in regression context.
  * t-tests for regression coefficients, confidence vs prediction intervals, multiple testing issues (Bonferroni, Holm, Benjamini-Hochberg FDR).
  * Randomisation, blocking, factorial designs, power analysis (a priori sample size computation), **causal inference preview** (ATE, ATT), Simpson's paradox revisited.
  * **Bayesianism** vs **frequentism** — epistemic vs aleatory uncertainty. Frequentist confidence intervals construction. Hypothesis testing as decision rule. **Bootstrap resampling** (non-parametric bootstrap, parametric bootstrap, block bootstrap for time series).
  * Sampling distributions (χ², t, F); estimation (point and interval); tests for one/two means/proportions/variances; paired t-test; McNemar's test; non-parametric tests (sign, Wilcoxon, Mann-Whitney, Kruskal-Wallis); contingency tables (χ² test of independence); ANOVA (one-way, two-way, with and without interaction); simple and multiple linear regression hypothesis testing.
  * Estimators — **Maximum a Posteriori (MAP)** as the Bayesian regularised counterpart to MLE.

</details>

* **Courses and references:**
  * **Primary Course Link:** [MIT OCW 18.650 Statistics for Applications (free lectures and notes)](https://ocw.mit.edu/courses/18-650-statistics-for-applications-fall-2016/) · [Harvard STAT 111 course description](https://qrd.college.harvard.edu/directory/stat-111/) (comparison, not the free default)
  * **Reading shelf (principal book above; alternatives and depth):**
    * _All of Statistics_ (**2nd printing, Springer 2004**, still canonical) — Larry Wasserman — chapters 6–15.
    * _Statistical Inference_ (**2nd Edition**) — Casella & Berger — the rigorous graduate-level reference.
    * _An Introduction to Statistical Learning with Python (ISLP)_ (**2023, 2025 reprint**) — James, Witten, Hastie, Tibshirani, Taylor — Chapters 2-3.
  * **Practical Implementation:** **`statsmodels` 0.14+** for classical inference (OLS, GLM, ANOVA), **`pingouin`** for modern stats API, **`scipy.stats`** for tests. Use **R 4.4+** with `{tidyverse}`, `{broom}`, `{infer}` for when you need publication-grade stats.

* **➡️ Cross-ref note (NEW v2026.2):** A/B testing, experimental design, and causal inference have been promoted out of this module into a **dedicated Module 6½ — Causal Inference & Experimentation** (directly below) because these skills are especially valuable in product-DS and experimentation roles.

* **📦 Module Project (mandatory) — Inference toolkit from scratch**
  * **Deliverable:** A package implementing, without `scipy.stats` doing the work for you: percentile-bootstrap confidence intervals (BCa optional), a permutation test, a two-sample t-test, and a multiple-comparison correction (Bonferroni + Benjamini–Hochberg). Then run all four on one real dataset and write up what they disagree about.
  * **Definition of done:** (1) `pytest` suite checking exact tiny cases, simulation coverage/type-I error and agreement with SciPy/statsmodels where an equivalent exists; state resampling seeds and tolerances; (2) `README.md` stating each test's assumptions and what happens when they are violated; (3) a results memo explaining one assumption failure or disagreement, using a labeled synthetic example if needed. A significant result is not a completion condition.
  * **Required design note:** before inference, state the target effect, uncertainty level and a prospective sample-size/power calculation for a simple two-arm experiment. Avoid interpreting retrospective power as additional evidence. **Stretch:** BCa intervals and simulation-based power for non-normal outcomes.
  * **Anti-goal:** Do not produce a notebook full of p-values. The deliverable is a tested library plus a document about uncertainty.

---

<a id="module-6-half"></a>
## Module 6½: Causal Inference & Experimentation

**Recommended principal reading:** Hernán and Robins, **Causal Inference: What If** (free author text), for identification; Kohavi, Tang and Xu, **Trustworthy Online Controlled Experiments** (Cambridge, paid), for experiment operations. These cover complementary halves of this module.

**Core outcome:** distinguish estimation from identification; state consistency, exchangeability and positivity assumptions; pre-specify an experiment and evaluate a confounded counterexample. Synthetic controls, IV and causal forests are optional depth, each requiring its own identification argument.

* **The Tutor's "Why":** Causal inference is especially valuable for product-DS, experimentation, policy, and other roles where decisions must be defended—not a universal interview requirement. Berkeley MIDS dedicates an entire course to it ([DATA 241 · Causal Inference](https://www.ischool.berkeley.edu/courses/datasci/241) ✅), and MIT 14.387 *Mostly Harmless Big Data* covers the econometric half. An association alone does not identify an intervention effect. State the estimand and identification assumptions before selecting an estimator.

* **Strict Prerequisites:** Module 5 (joint distributions, conditional expectation), Module 6 (hypothesis testing, CIs, bootstrap).

<details>
<summary>Topic map and later depth — use the core outcome above to choose scope</summary>

* **Topic map (core plus optional depth; roadmap synthesis):**
  * **A/B Testing Foundations:** Randomisation as the identification strategy, potential outcomes framework (Rubin/Neyman), ATE / ATT / CATE / LATE estimands, sample-size and MDE (minimum detectable effect) calculations, one-sided vs two-sided tests, Type I/II control, **sequential testing & always-valid p-values** (Howard et al. 2021), **group-sequential designs** with O'Brien-Fleming/Pocock boundaries, **CUPED variance reduction** using a pre-treatment covariate (Deng et al., 2013), stratified randomisation, cluster-randomised experiments.
  * **Interference & Network Effects:** **SUTVA violations**, switchback experiments (Uber/Lyft), **spillover** in social networks, ego-cluster randomisation, graph-cluster randomisation, synthetic control for marketplace platforms.
  * **Multiple Testing:** Bonferroni, Holm-Bonferroni, Hochberg, **Benjamini-Hochberg FDR control**, Storey's q-values, sequential multiple testing.
  * **Resampling-Based Inference:** Non-parametric bootstrap (Efron), parametric bootstrap, block bootstrap for time-series, **permutation tests** (exact inference under the null), conformal inference preview (M9).
  * **Bayesian A/B Testing:** Beta-Binomial for conversion rates, Normal-Normal for continuous metrics, **expected loss / expected regret stopping rules**, multi-armed bandits (Thompson sampling, UCB) for adaptive allocation; their regret objective and inference requirements differ from a fixed-horizon experiment.
  * **Causal Graphs & do-Calculus:** Directed Acyclic Graphs (DAGs), **d-separation** criterion, Markov equivalence classes, **Pearl's do-operator** and the three rules of do-calculus, confounders / mediators / colliders, **M-bias** and **butterfly-bias** (colliders you didn't know you conditioned on), identifiability.
  * **Adjustment Strategies:** **Backdoor criterion** (sufficient-adjustment sets), **frontdoor criterion**, **instrumental variables (IV)** and the LATE theorem (Imbens-Angrist), **2SLS**, **Difference-in-Differences (DiD)** and parallel-trends assumption, **Regression Discontinuity Design (RDD)** sharp and fuzzy, **Synthetic Control Method** (Abadie et al.), **matching** (exact, Mahalanobis, propensity-score, CEM).
  * **Modern Causal ML:** **Double/Debiased ML** (Chernozhukov et al. 2018) as the bridge to high-dimensional confounders, **Causal Forests** (Wager & Athey) for heterogeneous treatment effects, **doubly-robust estimators** (AIPW, TMLE), **meta-learners** (S-, T-, X-, R-, DR-learner), **uplift modelling** for marketing.
  * **Python Stack:** [DoWhy](https://github.com/py-why/dowhy) ✅ (end-to-end causal workflow), [EconML](https://econml.azurewebsites.net/) ✅ (Microsoft, heterogeneous TE), [CausalML](https://causalml.readthedocs.io/) ✅ (Uber, uplift), [Pyro](https://pyro.ai/) (probabilistic programming for causal models), `statsmodels` IV/2SLS, `linearmodels` (panel/IV).

</details>

* **Courses and references:**
  * **Primary Course (free):** [Brady Neal — *Introduction to Causal Inference*, Fall 2020 (YouTube + lecture notes; free introductory course)](https://www.bradyneal.com/causal-inference-course) ✅
  * **Econometric track:** [MIT 14.387 — *Applied Econometrics (Mostly Harmless Big Data)*, Fall 2014 OCW](https://ocw.mit.edu/courses/14-387-applied-econometrics-mostly-harmless-big-data-fall-2014/) ✅
  * **Harvard CAUSALab** — [course materials + *What If* book](https://www.hsph.harvard.edu/causal/) ✅
  * **Practical book (free):** [Matheus Facure — *Causal Inference for the Brave and True*](https://matheusfacure.github.io/python-causality-handbook/landing-page.html) ✅ — every chapter is a runnable notebook.
  * **Reading shelf (principal book above; alternatives and depth):**
    * Hernán & Robins — [*Causal Inference: What If* (free author-hosted text; record the downloaded revision)](https://miguelhernan.org/whatifbook) ✅
    * Pearl, Glymour & Jewell — *Causal Inference in Statistics: A Primer* (Wiley 2016).
    * Pearl — *Causality: Models, Reasoning, and Inference* (Cambridge 2e, 2009) — the reference.
    * **Kohavi, Tang & Xu** — [*Trustworthy Online Controlled Experiments*](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59) ✅ (Cambridge 2020) — **a recommended experimentation reference**.
  * **Communities / living resources:** [exp-platform.com](https://exp-platform.com/) ✅ (Ron Kohavi's blog + papers from Microsoft ExP platform), [Statistical Modeling, Causal Inference & Social Science (Gelman blog)](https://statmodeling.stat.columbia.edu/), Pearl's *UCLA Causality Blog*.

* **📋 Core projects and optional depth:**
  1. **Core:** design and simulate an A/B test: estimand, assignment unit, MDE, power/sample size, stopping rule, SRM and guardrails. Compare randomized and confounded estimates on [the local lab](../resources/local-labs/README.md); quantify uncertainty. CUPED is an extension with pre-treatment covariates and a separately estimated coefficient.
  2. **Optional econometric depth:** fit an IV regression on a realistic dataset (e.g., [NLSY or Angrist-Krueger 1991 compulsory-schooling](https://www.nber.org/papers/w3572)) — reproduce the returns-to-education estimate.
  3. **Core identification exercise:** use DoWhy or the local lab end-to-end: model → identify → estimate → refute — on a confounded synthetic dataset; show refutation tests (placebo, random common cause, unobserved-confounder sensitivity).
  4. **Optional heterogeneous-effects depth:** Causal Forest on lalonde / criteo-uplift: estimate CATEs, plot HTE heatmap, produce a targeting policy + its evaluation via doubly-robust off-policy estimation.

---

<a id="module-7"></a>
## Module 7: Data Wrangling, EDA & Visualisation

**Recommended principal reading:** Wes McKinney, **Python for Data Analysis**, third edition ([free author-hosted text](https://wesmckinney.com/book/), paid print), for pandas and data transformations; Wilke’s free visualization text supplies chart design.

**Core outcome:** preserve raw data, validate a schema, make reproducible transformations and answer three pre-written questions with labelled figures. Explain missingness, selection bias and cleaning choices without causal claims from EDA.

**Start and assess:** demonstrate [M1 competence](../guides/readiness-checks.md#m1-ready), then attempt the [data-readiness check](../guides/readiness-checks.md#data-ready). The [beginner SQL/data investigation](../resources/beginner-projects/sql/README.md#start) offers a small shared fixture after M1; it is practice in keys, missing values and reconciliation, not full M7 completion. For M7, extend a permitted dataset to the three-question pipeline and figures below.

* **The Tutor's "Why":** Data collection and cleaning decisions determine what an analysis can support. Preserve raw inputs, document transformations and inspect missingness before interpreting a model.

* **Strict Prerequisites:** Module 1 (Python).

<details>
<summary>Topic map and later depth — use the core outcome above to choose scope</summary>

* **Topic map (core plus optional depth; roadmap synthesis):**
  * The data-science life-cycle (CRISP-DM revisited for 2026), question framing, translating business problems into statistical ones.
  * `DataFrame` / `Series` model, indexing (`.loc`, `.iloc`), filtering, `groupby`-`apply`-`combine`, `merge`/`join`/`concat`, `melt`/`pivot`/`stack`/`unstack`, datetime handling, categorical dtype, missing-value representations.
  * Web scraping with BeautifulSoup, Requests session management, handling JS-rendered pages with Playwright, API consumption (REST, GraphQL, OAuth), handling CSV/TSV/JSON/JSONL/Parquet/Arrow/Avro.
  * Outlier detection (z-score, IQR rule, isolation forest preview), distributional plots (histogram binning strategies — Freedman-Diaconis, Sturges, Scott), QQ plots, log-transforms, Box-Cox transforms.
  * MCAR / MAR / MNAR taxonomy (Rubin 1976), listwise/pairwise deletion, mean/median/mode imputation, **k-NN imputation**, **MICE (Multivariate Imputation by Chained Equations)**, multiple imputation, domain-specific imputation.
  * Grammar of graphics (Wilkinson), Cleveland-McGill perceptual hierarchy (position > length > angle > area > colour), Tufte's principles (data-ink ratio, small multiples), choropleth vs cartogram, interactive dashboards.
  * Fairness in data collection, selection bias, survivorship bias, historical bias, measurement bias, informed consent, differential privacy preview.
  * Real-world data in business context, Excel-to-Python migration, data warehousing vs data lakes, ETL vs ELT, slowly-changing dimensions.
  * Descriptive / diagnostic / predictive / prescriptive analytics framework, KPIs, dashboarding, **Tableau / PowerBI** vs **Streamlit / Dash / Plotly**.
  * Data-centric AI — **data augmentation**, weak supervision, active learning preview, label noise.

</details>

* **Courses and references:**
  * **Primary Course Link:** [Data School's free pandas video course](https://www.dataschool.io/easier-data-analysis-with-pandas/) — public videos, notebooks and datasets; also listed in the [pandas tutorial index](https://pandas.pydata.org/docs/getting_started/tutorials.html). Pair it with McKinney's book and current pandas docs for API changes. [Harvard CS109A 2021](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html) supplies archived notebooks/slides; public recordings are not assumed.
  * **Reading shelf (principal book above; alternatives and depth):**
    * _Python for Data Analysis_ (**3rd Edition, 2022**) — Wes McKinney (pandas creator) — chapters 5–10.
    * _Storytelling with Data_ — Cole Nussbaumer Knaflic — communication principles.
    * _Fundamentals of Data Visualization_ — Claus Wilke — [free online](https://clauswilke.com/dataviz/).
  * **Practical Implementation:** pandas plus Matplotlib/Seaborn for the default course-aligned route. Polars and DuckDB are optional performance comparisons; choose one validation method (explicit assertions or Pandera). Pin a compatible environment and measure the actual workload.

* **🔧 Modern Data Tooling:**
  * **[Polars 1.40+](https://pola.rs/)** ✅ — an alternative DataFrame engine with expressions, lazy frames and query optimization. Learn `pl.LazyFrame`, `pl.col`, `pl.Expr`, expression-based group-by, streaming engine.
  * **[DuckDB 1.5+](https://duckdb.org/)** ✅ — "SQLite for analytics." In-process OLAP over Parquet/Arrow; useful for local analytical SQL. Performance and feasible dataset size depend on memory, query shape and storage; benchmark your own data.
  * **[Great Expectations](https://greatexpectations.io/)** ✅ + **[Pandera](https://pandera.readthedocs.io/)** ✅ — schema + data-quality validation; declarative expectations; catch data drift before it reaches models.
  * **Optional visualization alternatives:** [Plotly](https://plotly.com/python/) for interactive Python figures or [Altair](https://altair-viz.github.io/) for declarative Vega-Lite charts. [Observable Plot](https://observablehq.com/plot/) is a **JavaScript** alternative with local HTML/npm use; it is not another required Python package or hosted subscription. Keep the default Matplotlib/Seaborn route unless a project needs an alternative, and pin the version you actually use.
  * **Dashboards:** **[Streamlit](https://streamlit.io/)** ✅ for ML demos, **[Gradio](https://www.gradio.app/)** ✅ for HF-style model UIs, **[Evidently](https://www.evidentlyai.com/)** ✅ for data-drift dashboards.
  * **Feature Engineering Discipline:** Target encoding with K-fold smoothing, **train-test leakage** (temporal, group, target-leak from future aggregates), time-based features (lag, rolling, expanding windows), cyclical encoding (sin/cos of hour/month), **sklearn Pipelines + ColumnTransformer** as the default implementation pattern for keeping learned preprocessing inside training folds. Reference: [*Feature Engineering for Machine Learning* — Zheng & Casari (O'Reilly 2018)](https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/).

* **📦 Module Project (mandatory) — End-to-end EDA with documented data-quality problems**
  * **Deliverable:** Pick a permitted dataset with inspectable missingness, duplicates, schema errors or inconsistent values; a labeled synthetic corruption fixture is acceptable. Preserve the original inputs. Produce a reproducible pipeline that ingests raw files, validates and cleans them, and emits a tidy Parquet file and clearly labeled figures answering three questions written before the analysis.
  * **Definition of done:** (1) A data-validation layer (`pandera` or explicit assertions) that fails loudly on schema drift, plus a `pytest` suite over your transform functions; (2) `README.md` with the three questions, the three figures, and a data dictionary; (3) a results memo listing every judgement call you made while cleaning — dropped rows, imputed values, outliers kept or removed — because that list is what a reviewer will actually interrogate.
  * **Stretch:** Re-run the same pipeline in Polars and report the wall-clock difference on the full dataset.
  * **Anti-goal:** No `df.describe()` dumps. Every figure must answer a stated question.

<a id="analyst-reconciliation"></a>
**Analyst role extension — spreadsheet, SQL and decision report:** after M8a's SQL basics, reuse this dataset in a workbook and independently computed SQL queries. This is targeted analyst practice, not an extra prerequisite for the M7 core.

- Clean types and missing values explicitly; use a lookup/join and pivot/grouped summary. Include a duplicate-key or missing-value fixture that exposes a wrong total.
- Define each KPI's grain, numerator, denominator and date range. Reconcile row counts and totals between workbook and SQL, explaining rounding and filter differences.
- Produce a small filtered dashboard/report, a metric dictionary and a one-page decision memo. Check that totals and denominators remain meaningful when filters change.
- Retain the workbook, SQL, fixture and reconciliation results. [LibreOffice Calc](https://www.libreoffice.org/discover/calc/) provides a free local spreadsheet option; [Microsoft Learn Power BI](https://learn.microsoft.com/en-us/training/powerplatform/power-bi) supplies self-paced product training when relevant. Instructor-led classes, certification and hosted sharing have separate terms. A local report is sufficient; generic spreadsheet experience is not a claim of Excel/Power BI fluency.

This exercise responds to observed analyst tasks in the [dated employer sample](../audit/career-research-2026-11-05.md); it is not a universal hiring checklist.

---

<a id="module-8a"></a>
## Module 8a: Databases, SQL & Warehouses

**Recommended principal reading:** Silberschatz, Korth and Sudarshan, **Database System Concepts** (paid), for relational systems; Kimball and Ross, **The Data Warehouse Toolkit**, third edition (paid), for optional dimensional-model depth. CS50 SQL lectures remain the free default.

**Core outcome:** design keys/constraints, query joins/windows, migrate a schema, validate data and explain a measured execution plan. Start after M1; index internals do not gate SQL.

**First small step:** after [M1 evidence](../guides/readiness-checks.md#m1-ready), use the [local SQL investigation](../resources/beginner-projects/sql/README.md#start) and [SQL readiness check](../guides/readiness-checks.md#sql-ready). The [semester plan](../guides/first-semester.md#week-15) makes this a conditional two-week preview. SQLite practice does not complete the PostgreSQL migrations, windows and measured-plan requirements below.

* **The Tutor's "Why":** Data systems must preserve correctness as data volume and concurrent use grow. IITM dedicates a full diploma-level course (BSCS2001) plus specialisation courses to this area. SQL is a common requirement across analyst, data-science, and engineering roles, but no universal percentage is established here. **Module 8 has been split in v2026.2** into **M8a (Databases, SQL & Warehouses)** here, and **M8b (Distributed Data & Streaming)** directly below — because the 2026 production data stack (Spark + Iceberg + Airflow + Kafka + dbt) is a full module in its own right and cannot share airtime with SQL fundamentals.

* **Strict Prerequisites:** Module 1 (Python for writing database migration scripts and running tests).
* **Recommended Prerequisites:** Module 4 (Algorithms — trees and hashing help understand index internals like B-Trees and Hash Indexes, but are not a gating blocker for learning SQL queries, joins, and relational schema design).
* **Prior Competency:** Prior study can waive a prerequisite when you demonstrate the corresponding outcome. Basic SQL familiarity alone does not establish the Python/test skills needed for this module's project.

<details>
<summary>Topic map and later depth — use the core outcome above to choose scope</summary>

* **Topic map (core plus optional depth; roadmap synthesis):**
  * Relational model (tuples, relations, schemas, keys — super/primary/candidate/foreign), relational algebra (selection σ, projection π, union, intersection, difference, Cartesian product, join variants, division), **SQL DDL** (CREATE, ALTER, DROP), **SQL DML** (SELECT/INSERT/UPDATE/DELETE), JOINs (inner, left/right/full outer, cross, self, lateral), subqueries (correlated vs uncorrelated), CTEs (recursive and non-recursive), window functions (`OVER`, `PARTITION BY`, `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `SUM() OVER`), set operations (UNION, INTERSECT, EXCEPT), views, indexes (B-tree, hash, bitmap, covering), transactions and **ACID properties**, isolation levels (read uncommitted/committed, repeatable read, serialisable), concurrency control (two-phase locking, MVCC), recovery (WAL, ARIES), normalisation (1NF/2NF/3NF/BCNF/4NF/5NF), functional dependencies, Armstrong's axioms.
  * **Advanced SQL and engine-specific depth:** Query plans (EXPLAIN ANALYZE), cost-based optimisation, partitioning (range/list/hash), bitmap indexes, covering indexes, **recursive CTEs** for hierarchical data, **LATERAL joins**, **PIVOT / UNPIVOT**, **MERGE / UPSERT**, JSON/JSONB queries (Postgres), array types, `PERCENTILE_CONT`, `QUALIFY` clause (Snowflake/BQ), approximate aggregations (`APPROX_COUNT_DISTINCT` powered by HyperLogLog).
  * Data warehouse concepts (star schema, snowflake schema, fact/dimension tables), OLAP cubes, slice/dice/drill-down/roll-up, **SCD Type 0/1/2/3/6**, ETL vs ELT pipeline design, **Kimball dimensional modelling**, Data Vault 2.0 (preview).
  * **Hosted warehouses and local analytical engines:** **Snowflake** (virtual warehouses, time travel, zero-copy clone), **BigQuery** (slot-based pricing, BI-engine, materialised views), **Amazon Redshift**, **Databricks SQL Warehouse**, **DuckDB** (single-node), **ClickHouse** (OLAP, real-time). Compare a relevant option only; no paid warehouse is required.
  * **[dbt — Data Build Tool](https://docs.getdbt.com/)** ✅: models, sources, tests (`unique`, `not_null`, `accepted_values`, relationships), **macros** (Jinja templating), **incremental models** (with `unique_key`, late-arriving facts), **snapshots** (SCD Type 2 automation), **packages** (`dbt_utils`, `dbt_expectations`), exposures, metrics, MetricFlow integration.
  * Document databases, BSON, sharding, replica sets, aggregation pipeline ($match, $group, $project, $lookup, $unwind), indexing strategies.

</details>

* **Courses and references:**
  * **Primary Course Link:** [Harvard CS50 SQL](https://cs50.harvard.edu/sql/) (free default: SQLite, relational design, queries, views and indexes, with PostgreSQL/MySQL introductions) · [Stanford CS145, Fall 2020 archive](https://cs145-fa20.github.io/) (optional public slides for database theory/systems) · [IITM BSCS2001 course page](https://study.iitm.ac.in/ds/course_pages/BSCS2001.html) · [Kaggle Intro to SQL](https://www.kaggle.com/learn/intro-to-sql) (short free syntax primer) · [dbt Learn](https://learn.getdbt.com/) ✅ (free dbt Fundamentals course).
  * **Access Status (Nov 2026):**
    * The CS145 Fall 2020 archive has public slides; its SQL and design-theory slide exports were retrieved. Recordings are listed on Stanford Canvas, so this is **not a verified public video route**. Use selected slides after the relevant CS50 SQL lessons; the archive's fuller CS prerequisites and cloud-credit projects are not extra M8a entry requirements. The local project below replaces those hosted assignments for this roadmap.
    * CS50 SQL lecture videos, notes, and problem sets are free to study; the official route uses a free edX account for feedback/submission, and its CS50 Certificate is free after the course requirements. An edX verified certificate is optional and paid.
    * Kaggle Intro to SQL is 100% free with a Kaggle account.
    * PostgreSQL 17, DuckDB, SQLite, and dbt-core are open-source and run locally at zero cost.
  * **Outcome-to-Resource Mapping:**
    * Relational modeling and normalization → CS50 SQL Relating/Designing; CS145 for additional systems theory.
    * Filtering and joins → CS50 SQL Querying/Relating; optional Kaggle SQL practice.
    * Window functions and recursive CTEs → PostgreSQL tutorials; do not attribute unverified coverage to CS50 SQL.
    * Indexes → CS50 SQL Optimizing. PostgreSQL `EXPLAIN ANALYZE` → [official EXPLAIN guide](https://www.postgresql.org/docs/current/using-explain.html); dbt models and data tests → [dbt Learn](https://learn.getdbt.com/).
  * **Reading shelf (principal book above; alternatives and depth):**
    * _Designing Data-Intensive Applications_ — Martin Kleppmann (first edition) or Martin Kleppmann and Chris Riccomini (second edition) — select the storage, data-model and batch/streaming chapters from the edition you use; see the [canonical shelf](../resources/books.md).
    * _Database System Concepts_ (**7th Edition, 2019**) — Silberschatz, Korth, Sudarshan.
    * **The Kimball Group** — [*The Data Warehouse Toolkit* (3e)](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/) ✅ — a dimensional-modeling reference.
    * Reis & Housley — [*Fundamentals of Data Engineering*](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ✅ (O'Reilly 2022) — Chapters 5–8 for the DB/warehouse half.
  * **Practical Implementation:** local PostgreSQL for the assessed schema/query-plan project; SQLite for early CS50 SQL exercises. DuckDB/dbt-core are optional warehouse extensions. Hosted warehouses and paid accounts are never required.

* **📦 Module Project (mandatory) — Relational investigation → warehouse → decision report**
  * **Deliverable:** Extend the beginner fixture or choose a permitted public export/open dataset with a meaningful relationship between entities. Preserve its provenance and label generated data. Create a normalized PostgreSQL schema with justified keys/indexes, transform it into a small star schema and explain three defined metrics in a readable table or chart; a dashboard is optional. An official API is an optional source only after checking access terms, rate limits and privacy/deletion obligations. Keep any credentials outside code and document retention handling.
  * **Definition of done:** (1) Schema DDL committed as migrations, not typed into a client by hand; a `pytest` suite over the extraction and transform layers with external calls mocked when used; (2) `README.md` containing your ER diagram and the `EXPLAIN ANALYZE` output before/after an index, query/data parameters, and repeated timings; tests for keys, nulls, relationships and expected aggregates; (3) a findings/results memo on what you learned about the data that you did not expect.
  * **Stretch:** Add incremental loading with a watermark column so a re-run does not re-ingest history, and schedule it.
  * *The prior Reddit-dashboard archetype remains a valid source-specific option. The core assesses schema, query and validation evidence rather than API access or interface decoration. Use the [career guide](../guides/career-operations.md#skills-checklist) for your target-role sample; this roadmap does not claim a representative hiring-frequency ranking.*

---

<a id="module-8b"></a>
## Module 8b: Distributed Data & Streaming Systems

**Recommended principal reading:** Joe Reis and Matt Housley, **Fundamentals of Data Engineering** (O’Reilly, paid), for lifecycle and architecture decisions; **Designing Data-Intensive Applications** adds distributed-systems depth.

**Core outcome:** explain partitions, replay/idempotency, event time, schema evolution and delivery boundaries; demonstrate local failure recovery and a small Spark comparison. Kafka/Flink, a lakehouse table format and orchestrator are selectable extensions, not four mandatory stacks.

* **The Tutor's "Why":** Spark, Kafka, Airflow, and lakehouse concepts are important extensions for data-engineering, platform, and some MLE roles; they are not universal senior-DS interview requirements. Closing this role-dependent gap is useful for the data-systems path. Joe Reis (*Fundamentals of Data Engineering*) and the DataExpert free bootcamp are practical on-ramps.

* **Strict Prerequisites:** Module 1 and Module 8a (Python, SQL and relational keys).
* **Recommended Prerequisites:** Module 4 for partitioning/hash trade-offs; async Python for service integrations, not for starting local batch pipelines.

<details>
<summary>Topic map and later depth — use the core outcome above to choose scope</summary>

* **Topic map (core plus optional depth; roadmap synthesis):**
  * **Storage & File Formats:** **Parquet** (columnar, predicate pushdown, row-groups, page-level statistics), **Apache Arrow** (in-memory columnar, zero-copy IPC), **ORC**, **Avro** (schema evolution), object storage (S3 / GCS / Azure Blob), **lakehouse table formats** — [Apache Iceberg](https://iceberg.apache.org/) ✅ (hidden partitioning, snapshot isolation, time travel, MERGE INTO), [Delta Lake](https://delta.io/) ✅ (ACID on data lake, Z-ordering, vacuum), [Apache Hudi](https://hudi.apache.org/) (streaming upserts).
  * **Distributed Compute:** **Apache Spark 3.5+** — RDDs, DataFrames, Dataset API, Catalyst optimiser, Tungsten execution, **Adaptive Query Execution (AQE)**, broadcast joins vs sort-merge, skew-handling, partitioning and bucketing, caching strategies, PySpark idioms, Spark SQL, MLlib (legacy), **Structured Streaming** (micro-batches, triggers, watermarks). **[Ray Data](https://docs.ray.io/en/latest/data/data.html)** ✅ + **[Dask](https://www.dask.org/)** ✅ as Python-native alternatives. **[Apache Beam](https://beam.apache.org/)** as the portable API.
  * **Orchestration:** **[Apache Airflow](https://airflow.apache.org/)** ✅ — DAGs, operators, sensors, XComs, task groups, dynamic task mapping, backfills, SLAs. **[Dagster](https://dagster.io/)** ✅ — asset-oriented orchestration, software-defined assets, declarative scheduling. **[Prefect](https://www.prefect.io/)** ✅ — Pythonic flows, deployments, agents.
  * **Streaming:** **[Apache Kafka](https://kafka.apache.org/)** ✅ — brokers, topics, partitions, consumer groups, offsets, ISR, **exactly-once semantics**, Kafka Streams, Kafka Connect, Schema Registry (Avro/Protobuf). **[Redpanda](https://redpanda.com/)** ✅ (Kafka-compatible, C++). **[Apache Flink](https://flink.apache.org/)** ✅ (true-streaming, event-time, watermarks, windowing — tumbling/sliding/session, stateful functions). **[Materialize](https://materialize.com/)** / **[RisingWave](https://risingwave.com/)** (streaming SQL).
  * **CAP, Consensus & Consistency:** CAP theorem, PACELC, consensus (Paxos, Raft), eventual consistency, **CRDTs** for collaborative systems, idempotency, exactly-once vs at-least-once vs at-most-once.
  * MapReduce algorithms (word count, inverted index, joins), **LSH** (MinHash, random projections), PageRank as eigenvector of stochastic matrix, recommendation systems at scale, frequent itemsets (A-Priori, PCY, Multistage), streaming algorithms (reservoir sampling, Bloom, Count-Min Sketch, HyperLogLog), AdWords / online bipartite matching.

</details>

* **Courses and references:**
  * **Primary Course Link:** [DataTalks.Club Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) — select its free public batch-processing/Spark and streaming videos. Replace cloud tasks with the local project below; cloud credits are not assumed. [Stanford CS246](https://web.stanford.edu/class/cs246/) supplies public slides/assignments and partitioned-algorithm depth, but its current lecture recordings require enrolled-student Canvas access.
  * **Community handbook:** [DataExpert-io / data-engineer-handbook (free, curated)](https://github.com/DataExpert-io/data-engineer-handbook) ✅ — the 2026 community-maintained DE roadmap.
  * **Reading shelf (principal book above; alternatives and depth):**
    * Kleppmann (first edition) or Kleppmann and Riccomini (second edition) — *Designing Data-Intensive Applications* — select the distributed-systems, replication, partitioning and consistency chapters for your edition.
    * Reis & Housley — [*Fundamentals of Data Engineering*](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ✅ — the full data-engineering lifecycle.
    * *Mining of Massive Datasets* (3e, [free online](http://www.mmds.org/)) — Leskovec, Rajaraman, Ullman — chapters 2–7.
    * [*Streaming Systems*](https://www.oreilly.com/library/view/streaming-systems/9781491983867/) — Akidau, Chernyak, Lax (O'Reilly 2018).
  * **Blogs / Newsletters:** [Joe Reis Substack](https://joereis.substack.com/) ✅, [Kimball Group Tips](https://www.kimballgroup.com/) ✅, [High-Scalability](http://highscalability.com/).
  * **Practical Implementation:** **Apache Spark** via **PySpark** with an explicit runtime matrix, **Apache Iceberg** or **Delta Lake** on Parquet, **one tested Airflow or Dagster release**, **Apache Kafka 3.8+** (local via `kraft` mode), **DuckDB** for local SQL and file-format experiments. It does not emulate network partitions or prove distributed delivery guarantees.

* **📋 Project sequence (one core, optional systems extensions):**
  1. **Core local pipeline:** run and extend the [event-replay lab](../resources/local-labs/README.md) (standard-library SQLite default, DuckDB option), proving duplicate handling, schema validation and late-event policy. **Optional lakehouse depth:** use a supported Spark/Iceberg or Spark/Delta integration with local Parquet; exercise upserts, snapshots and time-travel. Check connector compatibility rather than assuming DuckDB can write every table-format feature.
  2. **Optional orchestration extension:** an Airflow or Dagster workflow that ingests an open API (e.g., NYC Taxi) → stores Parquet on S3/minio → transforms via dbt → serves to a Streamlit dashboard.
  3. **Optional streaming extension:** Kafka + Flink streaming word-count over a simulated tweet stream; exercise watermarks and late data.
  4. **Core comparison:** Spark local mode vs DuckDB on a small generated Parquet dataset; optionally increase toward 10 GB — measure wall-clock, peak RAM, and lines-of-code.

  **Shared definition of done:** Complete the core replay pipeline and small Spark/DuckDB comparison
  in one artifact. Optional orchestration, streaming and lakehouse branches do not need separate
  submissions. Include runnable validation, a recovery transcript, topology, environment/resource
  budget and a memo recording measured throughput, failure handling and local-experiment limits.
  The 10-GB benchmark is optional; do not extrapolate laptop throughput to a cluster.

---

[🏠 Roadmap home](../README.md) · [📚 Curriculum index](README.md) · [← 🟩 Foundations (M0–M5)](1-foundations.md) · [🟧 Classical ML (M9–M12) →](3-classical-ml.md)
