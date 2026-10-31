[🏠 Roadmap home](../README.md) · [All modules](../curriculum/README.md#all-modules) · [Progress tracker](progress-tracker.md#progress-tracker)

---

<a id="four-year-plan"></a>
# 🗓️ The Four-Year Plan — 8 Semesters + 3 Summers to a Top-Tier New-Grad Offer

**Who this is for:** a first-year CS undergraduate, starting as a Python beginner, studying **20–25 h/week** in term and **35–40 h/week** in summers. Graduation is **May/June 2030**. The target is an **entry-level or new-grad offer** at a top-tier company: big tech, AI labs, quant firms or well-funded scale-ups. Roles in order of preference: **ML Engineer → Data Scientist → Data Engineer**, with **SWE (ML-adjacent)** as the default title you enter through.

**What this page changes:** the 27 modules stay exactly as written. This page decides **when** you do each one, **how deep** you go, and **what you build**, measured against what new-grad hiring actually screens for. The [curriculum](../curriculum/README.md#all-modules) remains the syllabus; this page is the schedule.

[The bar](#the-bar) · [Four tracks](#four-tracks) · [Module map](#module-map) · [Semester plan](#semester-plan) · [Flagship projects](#flagship-projects) · [DSA ladder](#dsa-ladder) · [CS core](#cs-core) · [Opportunity calendar](#opportunity-calendar) · [Checkpoints](#checkpoints)

---

<a id="the-bar"></a>
## 1. The bar you are training for

Top-tier new-grad hiring is a **funnel**, and each stage tests something different. Everything else on this page is built backwards from this table.

| Funnel stage | What it actually tests | What gets you through it | Where this plan builds it |
|---|---|---|---|
| **Resume screen** | Signals in about 10 seconds: internships, shipped projects with numbers, ratings, open source | 1 page. 2 internships or equivalents. 3 flagship projects with users/metrics. Codeforces rating. Merged PRs | [Flagship projects](#flagship-projects), [opportunity calendar](#opportunity-calendar) |
| **Online assessment (OA)** | 2–3 algorithm problems (medium, sometimes hard) in 60–90 min | Speed on standard patterns; about 400 solved problems | [DSA ladder](#dsa-ladder) |
| **Technical interviews** (2–4 rounds) | Coding while talking; clean code; edge cases; complexity | Mock interviews from S4; explaining out loud | [DSA ladder](#dsa-ladder) |
| **ML round** (MLE/DS roles) | Fundamentals: bias–variance, metrics, overfitting, regularisation, trees vs nets, backprop, transformers, evaluation design | Modules M9–M12, M15–M16, M21/M23 done *from scratch*, not via tutorials | [Module map](#module-map) |
| **Design round** (some new-grad loops, more after the master's) | Low-level design, basic system design, ML system design for RAG/recommendation | DDIA + 10 written designs | [CS core](#cs-core) |
| **CS fundamentals** (common in India, some EU loops) | OS, networks, DBMS internals | College courses plus targeted revision | [CS core](#cs-core) |
| **Behavioural** | Ownership, conflict, failure, impact (e.g., Amazon's Leadership Principles) | 8 STAR stories drawn from **your own projects and internships** | [Semester plan](#semester-plan) S5–S7 |

> **The three facts that shape the whole plan.**
> 1. **Interviews test DSA, not curriculum completion.** Nobody asks whether you finished M13. Interview-style DSA runs every week from S2 to graduation and is never paused.
> 2. **Internships are the strongest resume line.** The plan is built to get an Indian internship in summer 2028 and an international or research internship in summer 2029. Applications for both open in **Aug–Oct of the previous year**.
> 3. **Projects are judged on production evidence, not topic.** Every flagship project needs real users or a real stakeholder, an evaluation, tests, CI and a deployed URL. This matches the repo's own [job-posting survey](career-operations.md#skills-checklist): evaluation was named in 6/7 AI-engineer postings, and communication in 15/16 postings overall.

---

<a id="four-tracks"></a>
## 2. Four tracks run in parallel every semester

Do not do the modules one after another and leave interview prep to the end. Every week has four tracks with a fixed share of your hours.

| Track | What | Share of weekly hours (term) | Why it is a separate track |
|---|---|---|---|
| **A. Interview DSA** | LeetCode/Codeforces ladder | **25–30%** (5–7 h) | It's the skill most often tested, and it decays fast if you stop |
| **B. Curriculum** | Modules from this repo, in the [order below](#module-map) | **35–40%** (8–10 h) | Depth for ML rounds and project quality |
| **C. Flagship project** | One hiring-grade project per term | **20–25%** (4–6 h) | The resume line and the interview stories |
| **D. Career ops** | Open source, applications, contests, writing | **10%** (2–3 h) | The funnel you enter offers through |

**Exception, your first five weeks:** the four tracks start gradually. Weeks 0–4 are Python only ([Week 0](week-0.md#week-0), then the [first 30 days](first-30-days.md#first-30-days)). Track A begins in week 5, and tracks C and D grow from there.

**Summers change the mix:** 35–40 h/week, split 15% A, 25% B, 50% C/internship, 10% D. If you have an internship, it *is* tracks C and D. Keep track A at 5 h/week minimum regardless.

**Exam weeks:** drop B and C to zero. Keep A at 3 h/week (one contest plus 5 problems). Never drop A to zero for more than one week.

---

<a id="module-map"></a>
## 3. Module map: what to do when, and how deep

Each module gets one decision: **CORE** (full depth, project mandatory), **COMPRESS** (essentials only, project mandatory but smaller), **COLLEGE** (count your college course as the main resource; do only the gap list and the project), **DEFER** (after graduation or during a master's) or **OPTIONAL** (only if ahead of schedule).

| Module | Decision | Semester | What to keep | What to skip for now |
|---|---|---|---|---|
| **Week 0** (Scrimba) | Do it | S1, week 0 | [Week 0](week-0.md#week-0): 7 days, Scrimba *Learn Python* only | Everything else in this table |
| **Math placement** | Do it once, **non-gating** | S1, week 2 | Khan Academy Precalculus course challenge ([placement guide](../curriculum/1-foundations.md#math-diagnostic)). Results pick resources; they never block M1 | Any timed or multi-part diagnostic |
| **M0a** Pre-calculus | Only the topics your placement flags | S1–S2 | Functions, exponentials/logs, trig identities | Everything else |
| **M0b** Logic & proof | COMPRESS · 15 min/day | S1–S2 | *Book of Proof* ch. 1–4 alongside college maths. Induction and contradiction are needed for M4 correctness proofs | Lean 4, full Velleman, a fixed exercise quota |
| **M1** Python | **CORE** | **S1** | [First 30 days](first-30-days.md#first-30-days), then CS50P in full: OOP, testing, files, APIs | — |
| **M2** Calculus + optimisation | COLLEGE + COMPRESS | S2–Summer 1 | Derivatives, chain rule, gradients, Jacobians, **matrix calculus**, gradient descent, convexity intuition | Boyd EE364A in full (DEFER) |
| **M3** Linear algebra | COLLEGE + COMPRESS | S2–Summer 1 | MIT 18.06 lectures 1–25 + 3Blue1Brown; eigen/SVD; least squares | Axler abstract track, Trefethen–Bau (DEFER) |
| **M4** Algorithms & DSA | **CORE** | **S2–S3** | Full MIT 6.006 plus the [DSA ladder](#dsa-ladder) | Randomised/streaming extras until S6 |
| **M5** Probability | **CORE** | Summer 1–S3 | Stat 110 in full (also the quant-interview base) | Measure theory, Vershynin (DEFER) |
| **M6** Inference | COMPRESS | S3 | CIs, hypothesis tests, bootstrap, MLE, regression inference | Asymptotic theory proofs |
| **M6½** Causal / A/B testing | COMPRESS | S4 | A/B design, power, CUPED, pitfalls (asked in DS interviews) | Synthetic control, interference designs |
| **M7** EDA & visualisation | **CORE** | **S2** | pandas, plotting, data validation, messy real data | — |
| **M8a** SQL & warehouses | **CORE** | **S2** | SQL to window functions + CTEs; indexes; schema design | Warehouse internals until S6 |
| **M8b** Distributed data | COMPRESS | S6 | Spark, Kafka basics, Airflow/Dagster, lakehouse pattern | Flink, deep streaming theory |
| **M9** Regression | **CORE** | **S3** | From scratch + sklearn; regularisation; diagnostics | — |
| **M10** Classification | **CORE** | **S3** | Logistic regression from scratch, metrics, **calibration**, class imbalance | Kernel theory beyond SVM intuition |
| **M11** Unsupervised | COMPRESS | S3 | k-means, PCA via SVD, GMM intuition | Spectral/manifold methods |
| **M12** Ensembles & boosting | **CORE** | **S3** | Trees from scratch, random forest, XGBoost/LightGBM, tuning | — |
| **M13** Bayesian / MCMC | **DEFER** | S8 optional | — | All (rarely tested for new grads) |
| **M14** Time series | OPTIONAL | S6 or S8 | Forecasting + backtesting only | HMM/Kalman theory |
| **M15** Deep learning foundations | **CORE** | **S4** | NumPy MLP with manual backprop; PyTorch; CNN basics; training tricks | — |
| **M16** Transformers & generative models | **CORE** (transformers) / COMPRESS (generative) | **S4** | Attention, transformer from scratch, tokenisation, Hugging Face fine-tuning | GAN math, diffusion derivations (survey only) |
| **M17** Reinforcement learning | OPTIONAL | S8 | Q-learning + DQN if ahead | Hierarchical RL, theory |
| **M18** LLMs & RLHF | **CORE** | **S5** | Pretraining/fine-tuning pipeline, LoRA/QLoRA, inference/serving, RLHF/DPO concepts | Frontier architecture reading lists |
| **M21** RAG & vector DBs | **CORE** | **S5** | Chunking, embeddings, hybrid search, re-ranking, **retrieval evals** | — |
| **M22** Agentic AI | COMPRESS | S7 | Tool use, one framework, MCP basics, agent evals | Multi-framework tours |
| **M23** Safety & evals | **CORE (evals)** / OPTIONAL (rest) | S5 | Eval design, LLM-as-judge pitfalls, red-teaming basics | Policy and interpretability deep dives |
| **M24** MLOps | **CORE** | **S6** (lite version from Summer 1) | Docker, CI, model registry, monitoring, the [Minimum Production Bar](../curriculum/6-frontier-production.md#production-bar) | Kubernetes depth |
| **M25** Product DS & communication | **CORE** | S7 (practised every term) | Metrics, writing memos, presenting results | — |
| **M26** Capstone | **CORE** (Applied/Systems track) | **S7–S8** | One upgraded flagship project | Research track, unless a lab invites you |

**New items the curriculum does not cover, added to this plan:**

| Added skill | Semester | Resource (free) | Why |
|---|---|---|---|
| Git, Linux shell, editor, debugging | S1 | MIT *The Missing Semester* | Every internship assumes it on day 1 |
| Web backend (FastAPI/Flask + PostgreSQL + auth) | Summer 1 | FastAPI docs + one deployed app | New-grad SWE resumes need a full-stack project; every ML service needs an API |
| Docker + GitHub Actions | Summer 1 | Docker docs, GitHub Actions docs | From here on, every flagship project ships with them |
| Cloud basics (one provider) | S5 | Free-tier docs | 3/7 AI-engineer postings in the repo survey named cloud deployment |
| Operating systems, networks, DBMS internals | S3–S5 | See [CS core](#cs-core) | Common interview topics, especially in India |
| System design + ML system design | S6–S7 | See [CS core](#cs-core) | Design rounds |

---

<a id="semester-plan"></a>
## 4. Semester-by-semester plan

Each block has the same five fields: **Modules** (track B), **DSA** (track A, cumulative problems solved), **Flagship** (track C), **Opportunities** (track D, detailed in the [opportunity calendar](#opportunity-calendar)) and **Exit check**. A term is complete only when its exit check is met.

### Year 1 — Foundations and first shipped work

<a id="s1"></a>
#### S1 · Oct–Dec 2026 (the rest of semester 1)
- **Start here:** [Week 0](week-0.md#week-0) (Scrimba only, 7 days), then the [first 30 days](first-30-days.md#first-30-days). Nothing else in this block starts before its week below.
- **Modules:** Week 0 Scrimba → **Weeks 1–10: M1** (CS50P, all problem sets) → *The Missing Semester* (shell, Git, editor) after CS50P → M0b (*Book of Proof* ch. 1–4, 15 min/day) alongside your college maths.
- **Math placement (week 2, non-gating):** take the Khan Academy Precalculus course challenge once. Your score routes you to resources in the [placement guide](../curriculum/1-foundations.md#math-diagnostic). It never delays M1.
- **DSA (from week 5, after CS50P Lecture 3):** **30** easy problems in Python (arrays, strings, hash maps). No timing yet. The goal is fluency in Python itself.
- **Projects:** week 4: [M1 starter project](../curriculum/1-foundations.md#m1-starter-project) (calculator or guessing game). End of term: **P0, M1 weather CLI** capstone ([spec](../curriculum/1-foundations.md#m1-capstone)). First public repo with tests + README.
- **Opportunities:** GitHub account in week 1 (CS50P needs it). LinkedIn and Codeforces/LeetCode accounts in **week 4**. Read the contributing guide of 2 open-source projects you use, after CS50P.
- **Exit check:** **Week 0 done** · CS50P finished · P0 public with green tests · 30 problems · college CGPA ≥ 8.5 target.

<a id="s2"></a>
#### S2 · Jan–May 2027
- **Modules:** **M4** (alongside your college DSA course; add MIT 6.006 lectures) · **M7** · **M8a** · M3 computational part (18.06 lectures 1–14) · M2 single-variable review via college.
- **DSA:** **100** cumulative. Topics: arrays, two pointers, sliding window, stacks, binary search, linked lists, recursion. **Weekly Codeforces Div 3/4 contests from February.**
- **Flagship:** **P1, data pipeline for a real stakeholder** (merges the M7 and M8a projects; see [flagship projects](#flagship-projects)).
- **Opportunities:** first issues (labelled "good first issue") in 2 target open-source orgs. One beginner hackathon.
- **Exit check:** P1 used by its stakeholder · 100 problems · CF rated · SQL window functions solved without notes.

<a id="summer-1"></a>
#### Summer 1 · Jun–Jul 2027 (35–40 h/week)
- **Modules:** **M5** first half (Stat 110 lectures 1–17) · M2 multivariable + **matrix calculus** · M3 lectures 15–25 (eigen, SVD) · web backend + Docker + GitHub Actions.
- **DSA:** **160** cumulative. Adds trees, BFS/DFS, heaps, intervals. Codeforces every week.
- **Flagship:** **P2, full-stack product with real users** (the SWE-signal project).
- **Opportunities:** **first merged PR** in a GSoC-participating org. One LFX/MLH program if timing allows.
- **Exit check:** P2 deployed with ≥ 20 real users · 1+ merged PR · CF ≈ 1300 · M5 halfway.

### Year 2 — ML core and the first internship

<a id="s3"></a>
#### S3 · Aug–Dec 2027
- **Modules:** **M9 → M10 → M12** (CORE), M11 (COMPRESS), **M6** (COMPRESS), **M5** second half. CS core: **operating systems** with the college course + OSTEP.
- **DSA:** **230** cumulative. Adds graphs (topological sort, Dijkstra, union-find), backtracking, 1-D dynamic programming. **First mock interview in December.**
- **Flagship:** **P3, a deployed ML service** (tabular model + API + monitoring).
- **Opportunities:** **Indian internship applications for summer 2028 (Aug–Oct, 40–80 applications)** · Summer@EPFL / ETH fellowship / Indian Academies' summer fellowship (SRFP) applications (Nov–Dec) · ICPC preliminary (October) · Hacktoberfest-style open-source push · 5 merged PRs.
- **Exit check:** P3 live · 230 problems · CF ≈ 1450 · 5 merged PRs · ≥ 1 internship interview.

<a id="s4"></a>
#### S4 · Jan–May 2028
- **Modules:** **M15 → M16** (transformer core) · **M6½** (COMPRESS: A/B testing) · CS core: **DBMS internals**.
- **DSA:** **300** cumulative. **NeetCode 150 complete.** Adds 2-D DP, tries, advanced graphs. 2 mocks per month.
- **Flagship:** **P4, transformer from scratch, with a research-style report.**
- **Opportunities:** **GSoC proposal (March)**, based on the org where you already have merged PRs · cold emails to Indian professors for summer research (Jan–Feb) · first medal-eligible Kaggle competition.
- **Exit check:** P4 report published · NeetCode 150 done · CF ≈ 1550 · GSoC proposal submitted · a summer 2028 slot secured (internship, GSoC or research).

<a id="summer-2"></a>
#### Summer 2 · Jun–Jul 2028 (35–40 h/week)
- **Priority order:** (1) internship → (2) GSoC → (3) research fellowship → (4) if none: P4 extended into an open-source contribution + Kaggle medal attempt.
- **Modules (around the internship):** start **M18** (fine-tuning half).
- **DSA:** **340** cumulative, 5 h/week minimum. Weekly contests continue.
- **Exit check:** one external reference (manager, mentor or professor) who can write about your work · a written resume entry with a measured result.

### Year 3 — Production AI and the international internship

<a id="s5"></a>
#### S5 · Aug–Dec 2028 (the most important term)
- **Modules:** **M18** (finish) → **M21** → **M23 (evals)** · cloud basics · CS core: **computer networks**.
- **DSA:** **380** cumulative. Company-tagged mediums. **Timed OA practice weekly** (2 problems in 70 min). Mocks every week in Sep–Nov.
- **Flagship:** **P5, LLM/RAG product with an eval suite** (the AI-engineer project).
- **Opportunities:** **international internship applications for summer 2029 (150–250 applications, Aug–Oct) + 30 referral requests per month** · Summer@EPFL / ETH (second attempt) · S.N. Bose (October, department nomination) · Max Planck / European lab cold emails for summer 2029 · ICPC regional (December) · write 8 STAR stories.
- **Exit check:** P5 live with ≥ 50 users and a published eval report · 380 problems · CF ≈ 1650 · ≥ 3 international online assessments taken.

<a id="s6"></a>
#### S6 · Jan–May 2029
- **Modules:** **M8b** → **M24** (full Production Bar) · M14 forecasting (OPTIONAL) · **system design**: DDIA chapters 1–9 + one low-level design problem per week.
- **DSA:** **420** cumulative. Mixed timed sets; 1 hard problem per week.
- **Flagship:** **P6, data/ML platform** (streaming + orchestration + monitoring).
- **Opportunities:** CERN openlab (January) · open-source maintainer-level contribution · second Kaggle medal → **Kaggle Expert** · college research assistantship.
- **Exit check:** P6 live · Kaggle Expert · 10 written system designs · summer 2029 internship or research confirmed.

<a id="summer-3"></a>
#### Summer 3 · May–Jul 2029
- **The internship is the priority.** Aim for a return offer: ship one measurable thing and write it up internally.
- **Modules (evenings):** M25 practice (write a results memo for your internship work, with permission) · ML system design (5 more designs).
- **DSA:** 5 h/week. **Interview season starts in August — arrive sharp.**
- **Exit check:** return offer **or** a strong reference plus a resume line with a measured result.

### Year 4 — Convert skills into offers

<a id="s7"></a>
#### S7 · Aug–Dec 2029
- **Modules:** **M22** (COMPRESS) · **M25** · **M26** begins (Applied/Systems track, built on P5 or P6).
- **DSA:** maintenance + company-specific sets. **2 mocks per week until offers.**
- **Flagship:** **P7, M26 capstone** (upgrade your best project to production-grade with an agent or system extension).
- **Opportunities:** **new-grad applications abroad and in India, filed by 30 September** · campus placements · use internship and GSoC references.
- **Exit check:** ≥ 2 final-round interview loops · capstone v1 live.

<a id="s8"></a>
#### S8 · Jan–May 2030
- **Modules:** finish **M26** · OPTIONAL depth (M13, M17, Boyd optimisation, Axler) only after an offer is signed.
- **DSA:** maintenance until the last interview.
- **Flagship:** P7 v2 · final portfolio clean-up (4 pinned repos, each with a 60-second README).
- **Opportunities:** spring new-grad roles, off-cycle internships, research-fellow roles.
- **Exit check:** **signed offer**, or the backup route active (see [checkpoints](#checkpoints)).

---

<a id="flagship-projects"></a>
## 5. Flagship projects, specified against hiring signals

**Rule:** one flagship per term. A flagship *replaces* the module projects it covers; it doesn't add to them. Each one has to meet the **hiring-grade bar** below, otherwise it's just a coursework repo.

**Hiring-grade bar (every flagship from P2 onward):**
1. **Real usage:** a named stakeholder, or ≥ 20 real users, or a public benchmark. Report the number in the README.
2. **Measured result:** one headline metric (latency, accuracy, hours saved, users, cost) with a baseline to compare against.
3. **Engineering:** tests (≥ 70% coverage of core logic), CI on every push, Dockerfile, deployed URL, a README with an architecture diagram.
4. **Written results memo:** what worked, what failed, what you'd do next. This is what you talk through in interviews.
5. **A resume bullet you can write:** *"Built X with Y, achieving Z (measured how)."* If you can't fill in Z, the project isn't done.

| # | Term | Project | Replaces module projects | What a top-tier screener sees | Stack | Done means |
|---|---|---|---|---|---|---|
| **P0** | S1 (end of term) | Weather CLI (M1 capstone, after the week-4 starter project) | M1 | Clean Python, tests, Git | Python, pytest, requests | [M1 definition of done](../curriculum/1-foundations.md#module-1) |
| **P1** | S2 | **Data pipeline for a real stakeholder**: e.g., your college club's or a local NGO's records → PostgreSQL → SQL transforms → dashboard they actually use | M7 + M8a | SQL depth, data modelling, a real user | Python, pandas, PostgreSQL, dbt-core, Streamlit | Stakeholder uses it weekly; data-validation tests; written schema rationale |
| **P2** | Summer 1 | **Full-stack product with real users**: one tool that solves a problem for your classmates (e.g., a timetable/notes/study-group app), with auth, a database and an API | (new: SWE signal) | You can build and ship software, not only notebooks | FastAPI, PostgreSQL, a simple frontend, Docker, GitHub Actions, a free-tier host | ≥ 20 users · CI green · uptime/error monitoring · p95 latency reported |
| **P3** | S3 | **Deployed ML service**: a tabular prediction problem with a real dataset (e.g., public transport delays, crop prices, student-performance risk with consent), trained with boosting and served behind an API | M9, M10, M12 | ML fundamentals + production: calibration, thresholds, monitoring | scikit-learn, LightGBM, MLflow, FastAPI, Docker, Evidently | From-scratch baseline vs. boosted model compared · calibration plot · drift check · API latency |
| **P4** | S4 | **Transformer from scratch + report**: train a small GPT-style model on a domain corpus; ablate 2 design choices (e.g., positional encoding, depth) | M15, M16 | You understand models internally, not just API calls (MLE/research signal) | PyTorch, Weights & Biases, Hugging Face tokenizers | Loss curves · ablation table · a 4-page report written like a workshop paper |
| **P5** | S5 | **LLM/RAG product with an eval suite**: a question-answering assistant over a real document set for real users (e.g., your university's regulations, an open-source project's docs, or government scheme documents in English + Hindi/Gujarati) | M18, M21, M23 | The current AI-engineer core: retrieval + **evaluation** + cost/latency discipline | Python, an open-weights model or API, a vector DB (pgvector/Qdrant), a re-ranker, an eval harness, tracing | ≥ 50 users · golden eval set (≥ 200 questions) · retrieval recall@k + answer faithfulness tracked in CI · cost per query and p95 latency reported · one LoRA fine-tune compared against prompting |
| **P6** | S6 | **Data/ML platform**: streaming events → orchestrated pipelines → feature tables → retraining job → model monitoring (can extend P3 or P5) | M8b, M24 | Data-engineer/MLOps signal: systems that run without you | Kafka or Redpanda, Airflow/Dagster, Spark or DuckDB, MLflow, Prometheus/Grafana | Meets the [Minimum Production Bar](../curriculum/6-frontier-production.md#production-bar) · alerting demo · runbook |
| **P7** | S7–S8 | **M26 capstone**: upgrade P5 or P6 (e.g., add an agent with tool use + agent evals, or scale to 10× load) | M22, M25, M26 | One deep, polished project, fit for a 20-minute interview discussion | Builds on P5/P6 | Full design doc · load test or eval report · 2-minute demo video |

> **v2026.7 — one evolving AI system.** P5 and P7 are the same repository grown through the [Portfolio Spine](portfolio-spine.md#levels): P5 = L1–L2 (API → RAG + evals), P7 = L3–L4 (read-only-first agent → router/worker/checker). Keep a [`DECISIONS.md`](portfolio-spine.md#decisions-template) from P5 onwards.

**Kaggle fits alongside the projects, not in place of them.** Two medal-eligible competitions a year from S4: one tabular (use M12) and one NLP/LLM (use M16/M18). Getting Started and Playground competitions award no medals. Target **Competitions Expert (2 bronze medals) by end of S6**. Put Kaggle on your resume as one line under "Achievements", never as a project.

---

<a id="dsa-ladder"></a>
## 6. The DSA ladder (track A)

Run it in Python first. **From S3, also solve in C++ or Java** if your target companies or competitive programming need it (C++ is standard for Codeforces).

| Phase | Terms | Cumulative solved | Topics | Weekly cadence | Codeforces target |
|---|---|---|---|---|---|
| 1. Fluency | S1 (from week 5) | 30 | Arrays, strings, hash maps, basic math | 3–4 easy | Account created (week 4) |
| 2. Patterns | S2–Summer 1 | 160 | Two pointers, sliding window, stack/monotonic stack, binary search, linked list, recursion, trees, BFS/DFS, heaps, intervals | 6–8 (mostly medium from April) | **1300** |
| 3. Core interview set | S3–S4 | 300 | Graphs (topo sort, Dijkstra, union-find), backtracking, DP (1-D → 2-D → knapsack/LIS/LCS), tries, greedy, bit manipulation · **NeetCode 150 complete by end of S4** | 6–8 + 1 contest | **1550** |
| 4. Speed + company sets | S5–S6 | 420 | Company-tagged mediums, segment tree/Fenwick (for CP), DP on trees/graphs, hards (1/week) | Timed: 2 problems in 70 min, weekly | **1650–1800** |
| 5. Maintenance | S7–S8 | 450+ | Mixed review, mock loops | 5 + 2 mocks | Keep rating |

**Rules:**
- **Every problem gets a 3-line note:** pattern, key insight, mistake. Re-solve anything you failed after 7 days.
- **45-minute cap** per problem in phases 2–3, then read the solution, then re-solve from scratch the next day.
- **Mock interviews:** first one in **December 2027 (S3)**, 2 per month in S4, weekly in Sep–Nov 2028, 2 per week in S7. Use peer mocks (free) and record yourself explaining.
- **Quant firms** (optional branch from S5): Stat 110 (M5) plus *Heard on the Street* and the "Green Book" (Zhou) for probability puzzles, and mental-arithmetic practice.

---

<a id="cs-core"></a>
## 7. CS core and design (tracked inside track B)

| Topic | Term | Resource (free) | Interview-ready means |
|---|---|---|---|
| Operating systems | S3 | College course + *OSTEP* (Arpaci-Dusseau) | Explain processes vs threads, scheduling, virtual memory/paging, deadlocks, synchronisation; write a producer–consumer with locks |
| DBMS internals | S4 | College course + CMU 15-445 lectures 1–12 | Indexes (B+ tree), transactions/ACID, isolation levels, normalisation, query plans |
| Computer networks | S5 | College course + *Computer Networking: A Top-Down Approach* chapters 1–3 | What happens when you type a URL; TCP vs UDP; HTTP/HTTPS/TLS; DNS; load balancing |
| Object-oriented / low-level design | S6 | 1 problem/week (parking lot, LRU cache, rate limiter, elevator…) | Class diagram + working code in 45 min |
| System design | S6 | *Designing Data-Intensive Applications* chapters 1–9 | Design a URL shortener, chat service or news feed at a basic scale; reason about caching, queues, partitioning |
| ML system design | S6–Summer 3 | Write 10 designs: recommendation, search ranking, fraud detection, RAG assistant, content moderation, ETA prediction… | Problem framing → data → features → model → offline/online evaluation → serving → monitoring, in 45 min |

**Revision sheets:** for OS, DBMS and networks, keep a 30-question self-quiz each. Re-take all three before every application season (Aug 2028, Aug 2029).

---

<a id="opportunity-calendar"></a>
## 8. Opportunity calendar: funded programs mapped to semesters

Every program below **pays you, or covers your travel and living costs**, and builds a skill or resume line. Each one is mapped to the exact term you should apply in. Dates are from the 2026–27 cycle as checked in October 2026. **Always confirm the current cycle on the official page**, since dates shift by 1–3 weeks each year.

**Before investing time:** some programs only accept students from listed Indian institutions (e.g., **Mitacs Globalink** uses an AICTE list, and **DAAD WISE** is limited to partner institutions). Check that your college is listed before you start. The programs marked **Open** judge you as an individual, so put most of your effort into those.

### 8a. Master list

| Program | What you get | Apply window (last cycle) | Eligible from | Your apply term → program dates | Skill it builds | Official page |
|---|---|---|---|---|---|---|
| **Google Summer of Code (GSoC)** | Paid open-source project, 12+ weeks | Mid–late March (2026: 16–31 Mar) | 18+, any student. **Open** | **S4 (Mar 2028)** → Summer 2. Retry S6 (Mar 2029) | Real code review, large codebases | [summerofcode.withgoogle.com](https://summerofcode.withgoogle.com/) |
| **LFX Mentorship** (Linux Foundation, incl. CNCF) | Paid mentorship, 12 weeks; 3 terms a year | Spring: ~late Jan–mid Feb · Summer: ~May · Fall: ~Aug | Any. **Open** | **Summer 1 (Aug 2027 fall term)** or S4 (Feb 2028 spring term) | Cloud-native/infra code | [mentorship.lfx.linuxfoundation.org](https://mentorship.lfx.linuxfoundation.org/) |
| **MLH Fellowship** | Paid remote program, 12 weeks, 30 h/week | Rolling batches (spring, summer, fall) | 18+. **Open** | **Summer 1 (2027)** or Summer 2 (2028) if no internship | Team open-source work | [fellowship.mlh.com](https://fellowship.mlh.com/) |
| **Outreachy** | Paid internship, 13 weeks | Indian students: **May cohort only**, initial application ~Feb | Identity-based eligibility; **past GSoC participants are ineligible** | S4 (Feb 2028), only if eligible and not doing GSoC | Open source | [outreachy.org](https://www.outreachy.org/apply/eligibility/) |
| **Summer@EPFL** (Switzerland, CS) | CHF 1,800/month + travel, 2–3 months | Deadline: Sunday nearest 1 Dec | Must be in 2nd year or above at application. **Open** | **S3 (Nov 2027)** → Summer 2 · retry **S5 (Nov 2028)** → Summer 3 | Research in a top lab | [summer.epfl.ch](https://summer.epfl.ch/) |
| **ETH Student Summer Research Fellowship** (Switzerland) | CHF 4,000 + travel/visa; July–August | ~1 Nov–mid Dec | 2 years of study completed by July. **Open** | **S3 (Nov 2027)** → Summer 2 if eligible by date, else **S5 (Nov 2028)** → Summer 3 | Research in a top lab | [inf.ethz.ch](https://inf.ethz.ch/studies/summer-research-fellowship.html) |
| **EPFL E3** (engineering) | Funded summer research, 8–12 weeks | Opens Oct, closes **1 Nov** | Check FAQ for year level | **S3 (Oct 2027)**, S5 (Oct 2028) | Research | [eee.epfl.ch](https://eee.epfl.ch/) |
| **Indian Academies' Summer Research Fellowship (SRFP)** (IASc–INSA–NASI) | 2 months with a scientist at IISc/IITs/labs; fellowship + train fare | Opens ~Sep, closes **30 Nov** | **Explicitly open to private universities**; check year rules | **S3 (Nov 2027)** → Summer 2 · retry S5 → Summer 3 | First research + IIT/IISc reference | [webjapps.ias.ac.in](https://webjapps.ias.ac.in/fellowship2027/index.html) |
| **S.N. Bose Scholars Program** (USA) | US research internship: stipend, airfare, insurance | ~Oct (via department nomination, 2 per stream) | Bachelor's/Master's at a recognised Indian institution | **S5 (Oct 2028)** → Summer 3 | US research + reference | [iusstf.org](https://iusstf.org/s-n-bose-scholars-program) |
| **Charpak Lab Scholarship** (France) | €700/month, 1–2 months, May–Aug | Typically early in the year; needs an invitation from a French lab | Indian students, ≤ 30 | **S5–S6 (outreach Oct 2028, apply early 2029)** → Summer 3 | European research | [inde.campusfrance.org](https://www.inde.campusfrance.org/france-excellence-charpak-summer-training-scholarship) |
| **Max Planck institutes** (CS internships) | Paid internships | Rolling; apply ≥ 5 months ahead | Strong students. **Open** | **S5 (Nov–Dec 2028)** → Summer 3 | European research | [cis.mpg.de/internships](https://www.cis.mpg.de/internships/) |
| **CERN openlab Summer Student** | Paid, ~9 weeks in Geneva | Deadline end of January | ~6 semesters completed by start | **S6 (Jan 2029)** → Summer 3 | Large-scale computing | [openlab.cern](https://openlab.cern/cern-openlab-summer-student-programme/) |
| **Mitacs Globalink Research Internship** (Canada) | Fully funded 12 weeks | Aug–mid Sep | **Only listed AICTE institutions** · 2nd year+ · 70% | S5 (Sep 2028) **only if your college is on the list** | Research in Canada | [mitacs.ca](https://www.mitacs.ca/our-programs/globalink-research-internship-students/) |
| **DAAD WISE** (Germany) | €831/month + travel, 2–3 months | ~Oct–Nov; needs a German professor's invitation | **Partner institutions only**, 5th–6th semester | S5 (Nov 2028) **only if your college is eligible** | Research in Germany | [daad.in](https://www.daad.in/en/find-funding/scholarship-database/) |
| **Company internships (India)** — big tech, product startups, quant firms' India offices | Paid | **Aug–Oct**, a year ahead; plus campus drives | 2nd–3rd year | **S3 (Aug–Oct 2027)** → Summer 2 | Production engineering | Company career pages |
| **Company internships (international)** | Paid + relocation | **Aug–Oct**, a year ahead | Penultimate year | **S5 (Aug–Oct 2028)** → Summer 3 | Production engineering + sponsorship pipeline | Company career pages |
| **Google SWE internships** (STEP was the old 1st/2nd-year track) | Paid | Listings typically open mid-year/Aug | Check each listing | **S3 (2027)** and **S5 (2028)** | Big-tech engineering | [Google internships](https://www.google.com/about/careers/applications/internships) |
| **Amazon ML Summer School** (India) | Free ML training, a strong resume line, interview access | Registration ~May–June | Restricted by graduation year (typically pre-final/final year) | **Summer 2 or Summer 3**, whichever matches your graduation year | Applied ML | [amazon.science](https://www.amazon.science/academic-engagements/amazon-launches-annual-ml-summer-school-in-india) |
| **ICPC (Asia regionals)** | Team contest; regional finalists get noticed by recruiters | Online preliminary ~Oct; regionals ~Dec | Team of 3 from your college | **S3 (Oct 2027)**, **S5 (Oct 2028)** | Competitive programming | [icpc.global](https://icpc.global/) |
| **Kaggle competitions** | Prize money in some; medals | Year-round | Open | From **S4**, 2 per year | Applied ML under a benchmark | [kaggle.com/competitions](https://www.kaggle.com/competitions) |
| **BlueDot Impact courses** (AI safety) | Free cohort-based courses | Rolling cohorts | Open | **S5** alongside M23 (optional) | Evals/safety literacy | [bluedot.org](https://bluedot.org/courses) |
| **SPAR** (AI safety research, part-time, remote) | Mentored research | Spring cycle opens ~Dec; fall ~Sep | Mostly students with ML background | **S6 (Dec 2028)** or S7 | Research with mentors | [sparai.org](https://sparai.org/) |
| **MATS / ML summer schools (MLSS, ELLIS)** | Funded | Varies | **Mostly master's/PhD** | After graduation | — | [matsprogram.org](https://matsprogram.org/apply) |
| **Microsoft Research India Research Fellow** | Paid 1–2 year research role | ~Feb–Mar | **Bachelor's completed** | **S8 (2030)**, a backup route after graduation | Research engineering | [microsoft.com/research](https://www.microsoft.com/en-us/research/academic-program/research-fellows-program-at-microsoft-research-india/) |
| **Hackathons** (MLH-member events, Smart India Hackathon, company hackathons) | Prizes, interview fast-tracks | Year-round | Open | **S2 onward**, 1 per term | Shipping under pressure | [mlh.io](https://mlh.io/) |

### 8b. Month-by-month calendar (repeats each year)

| Month | Do this |
|---|---|
| **Jan** | CERN openlab deadline (S6) · LFX spring applications · cold emails to Indian professors for summer research (S4) |
| **Feb** | Outreachy May cohort (if eligible) · SPAR/LFX results · pick the GSoC org's project ideas as soon as orgs are announced |
| **Mar** | **GSoC proposal** (S4, S6) · Kaggle competition #1 |
| **Apr–May** | End-of-term exams (track A at minimum) · confirm summer plans |
| **Jun** | Amazon ML Summer School registration (final-year eligible) · summer begins |
| **Jul** | Prepare resume v(n+1) · internship listings start appearing |
| **Aug** | **Internship applications open** (S3, S5) · new-grad applications (S7) · LFX fall term · Mitacs (only if eligible) |
| **Sep** | Applications at full volume · referral outreach · Kaggle competition #2 |
| **Oct** | ICPC online preliminary · S.N. Bose (S5) · EPFL E3 opens · SPAR fall |
| **Nov** | **E3 (1 Nov) · SRFP (30 Nov) · ETH fellowship opens · Summer@EPFL (~1 Dec)** |
| **Dec** | ETH fellowship closes · ICPC regionals · SPAR spring cycle opens · write the year's results memo |

### 8c. Top 10 by expected value (probability × impact) for a student outside IIT/NIT

| Rank | Program | Apply | Why it ranks here |
|---|---|---|---|
| 1 | **Company internships (India)** | S3 | Highest-signal resume line; feeds the next internship |
| 2 | **GSoC** | S4 | Judged on your code, not your college; about 7.5% base acceptance (1,141 of 15,245 applicants in 2026), much higher with prior merged PRs |
| 3 | **Company internships (international)** | S5 | The direct pipeline to a new-grad offer |
| 4 | **SRFP** | S3 | Explicitly open to private universities; gives you an IIT/IISc reference |
| 5 | **Summer@EPFL** | S3, S5 | Open to any college; Swiss lab reference |
| 6 | **ETH summer fellowship** | S3/S5 | Same |
| 7 | **ICPC + Codeforces 1700+** | S3, S5 | A rating can be compared across colleges |
| 8 | **S.N. Bose** | S5 | US research reference (needs top departmental rank) |
| 9 | **LFX / MLH** | Summer 1 | First paid open-source line on your resume, earlier than GSoC |
| 10 | **Max Planck / Charpak / CERN** | S5–S6 | European research line for summer 2029 |

---

<a id="checkpoints"></a>
## 9. Checkpoints and switch rules

| Checkpoint | On track | If behind, do this |
|---|---|---|
| **End of S2 (May 2027)** | 100 problems · CF rated · P1 used by its stakeholder | Cut M2/M3 to the college course only; protect DSA and P1 |
| **End of Summer 1 (Jul 2027)** | 160 problems · P2 with ≥ 20 users · 1 merged PR | Skip LFX/MLH; spend the rest of the summer finishing P2 + PRs |
| **End of S4 (May 2028)** | 300 problems · NeetCode 150 · a summer 2028 slot (internship/GSoC/research) | **No slot:** run Summer 2 as an open-source + Kaggle + P4-extension summer, and push international applications harder in S5 |
| **End of S5 (Dec 2028)** | ≥ 3 international OAs · P5 live with an eval report | **Zero OAs:** resume problem; rewrite it and get 3 reviews. **OAs but no interviews:** speed problem; double timed practice |
| **End of Summer 3 (Jul 2029)** | Internship done with a measured result | No internship: make P7 your main story; apply to 300+ new-grad roles + campus drives |
| **Mar 2030** | Signed offer | No offer: off-cycle roles + MSR India Research Fellow + top-tier India roles, then reapply in the next cycle with a year of experience |

**Funnel health ranges** (heuristics; track your own numbers in a spreadsheet):

| Stage | Healthy range | If below for 20+ attempts, the problem is… |
|---|---|---|
| Application → OA | 10–25% | Your resume |
| OA → interview | 30–50% | DSA speed |
| Interview → offer | 15–30% | Communication or design |
| Referral → interview | 25–40% | Outreach quality |

---

<a id="weekly-template"></a>
## 10. A default week during term (22 h)

| Day | Slot | Track |
|---|---|---|
| Mon–Fri | 1 h/day DSA (5 h) | A |
| Mon, Wed, Fri | 2 h curriculum (6 h) | B |
| Tue, Thu | 1.5 h flagship (3 h) | C |
| Sat | 3 h flagship + 2 h curriculum | C, B |
| Sun | Codeforces contest (2 h) + 1 h career ops (PRs, applications, one LinkedIn post about what you shipped) | A, D |

Log each week in your [progress tracker](progress-tracker.md#progress-tracker): problems solved, module section finished, commits to your flagship, applications sent.

---

[🏠 Roadmap home](../README.md) · [All modules](../curriculum/README.md#all-modules) · [Career operations](career-operations.md#career-operations) · [Practitioner fast lane](practitioner-track.md#practitioner-track)
