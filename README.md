# Data Science & AI Roadmap

**Free lectures, carefully chosen books, and practical projects - from mathematics and Python to production AI.**

[Start here](START-HERE.md) · [Browse all modules](curriculum/README.md#all-modules) · [Resume studying](guides/progress-tracker.md#resume) · [FAQ](FAQ.md)

**First-year CSE/AI in India, aiming for international companies and still choosing a role?** Follow the [undergraduate route](guides/india-undergraduate-path.md): shared foundations, small role experiments, stage-appropriate internships and a semester review of actual employer requirements.

[![Version](https://img.shields.io/badge/version-2026.11%20Curriculum%20Overhaul-blue)](CHANGELOG.md#refresh-log)
[![Modules](https://img.shields.io/badge/modules-27-6f42c1)](curriculum/README.md#all-modules)
[![Policy](https://img.shields.io/badge/policy-free%20lectures%20%2B%20best%20books-1a7f37)](FAQ.md#cost-and-access)
[![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-lightgrey)](LICENSE.md)

<a id="read-these-first"></a>
## Where to go next

| Your next step | Open this |
|---|---|
| **I'm new. Help me start.** | [Start Here](START-HERE.md#first-step): open Week 0 and begin the first small Python exercise. |
| **I know what I want to learn.** | [Curriculum index](curriculum/README.md#all-modules): jump directly to any of the 27 modules. |
| **I'm returning to my studies.** | [Resume checklist](guides/progress-tracker.md#resume): reopen your module and find the next unfinished task. |
| **I'm a CS undergrad planning four years of study.** | [Four-Year Plan](guides/four-year-plan.md#four-year-plan): eight adaptable semesters, coherent prerequisites, evolving projects and an opportunity directory. |

## What this is (in 30 seconds)

Read the roadmap on GitHub without installing or cloning it. When you reach the practical modules, use the included NumPy harness, local causal/data labs and agent-contract lab, or build the stated equivalent in your own repository. Courses and projects explain their own tools and accounts.

Each module brings together prerequisites, learning resources, and practical work. Start with its recommended resource, then follow the **module's actual reading and project requirements**. A short resource table is a starting point, not a promise that one course covers everything.

**Lectures are free; books are selected on merit regardless of price.** Module defaults name principal recommended books, with a topic-specific choice for M26, and label paid, authorized free-text and code/sample access. Core projects use small local routes. Certificates, hosted APIs and larger GPU experiments have separate costs. Start Week 0 without buying a book.

## How to use this roadmap

1. **Choose a starting module.** New to Python? Open [Week 0](guides/week-0.md#week-0). Otherwise use [Start Here](START-HERE.md#first-step), or the [track chooser](#choose-your-track) if you already have a goal.
2. **Check prerequisites and the deliverable.** The [module guide](guides/how-to-read-a-module.md#reading-order) shows what to read first.
3. **Study, practise, and build.** Use the [resource defaults](guides/how-to-read-a-module.md#pick-one) without treating alternatives as extra compulsory courses. Keep explicit required work in view.
4. **Record your next task.** Bookmark the module heading in your [progress tracker](guides/progress-tracker.md#resume). Check its definition of done and the [project policy](curriculum/README.md#module-projects) before moving on.

<a id="start-here"></a>
## Entry points by experience

- **New to Python:** open [Week 0](guides/week-0.md#week-0), then the [first 30 days](guides/first-30-days.md#first-30-days). Together they are the gentle start of [M1: Programming Foundations](curriculum/1-foundations.md#module-1).
- **Already programming:** choose a target below, then check that module's prerequisites. Python fluency alone does not establish calculus, probability, or ML readiness.
- **Returning after a break:** use [Resume](guides/progress-tracker.md#resume), not another full tour of the repository.

## Choose your track

**Not sure yet? Start with [Week 0](guides/week-0.md#week-0); you can choose a destination later.** Use the [complete role sequences and prerequisite inventory](guides/practitioner-track.md#role-pathways). They are checked against one module map, and distinguish full modules from application subsets.

| Your goal | Where to explore |
|---|---|
| **Data Analyst** — analysis and communication | [Statistics & Data](curriculum/README.md#statistics-and-data), then [M25: Product DS](curriculum/6-frontier-production.md#module-25). |
| **Data Scientist** — inference and predictive modelling | [Foundations](curriculum/README.md#foundations), [Statistics](curriculum/README.md#statistics-and-data), and [Classical ML](curriculum/README.md#classical-ml). |
| **Data Engineer** — databases and data systems | [M4: Algorithms](curriculum/1-foundations.md#module-4), [M8a: SQL](curriculum/2-statistics-and-data.md#module-8a), and [M8b: Distributed Data](curriculum/2-statistics-and-data.md#module-8b). |
| **ML Engineer** — model training and serving | [Classical ML](curriculum/README.md#classical-ml), [Deep Learning](curriculum/README.md#deep-learning), and [M24: MLOps](curriculum/6-frontier-production.md#module-24). |
| **AI Engineer, Applications** — products using existing models | [Practitioner track](guides/practitioner-track.md#practitioner-track) for scope, then grow one evaluated system with the [Portfolio Spine](guides/portfolio-spine.md#portfolio-spine). Multiple agents and self-improvement are optional extensions. |
| **AI Engineer, Systems** — model internals and infrastructure | [Deep Learning](curriculum/README.md#deep-learning) and [Frontier & Production](curriculum/README.md#frontier-and-production). |
| **Research / PhD preparation** — mathematical and research depth | [Full curriculum index](curriculum/README.md#all-modules) and [M26: Research capstone](curriculum/6-frontier-production.md#module-26). |

The [role guide](guides/practitioner-track.md#role-pathways) contains the complete ordered sequences. It also states the missing depth of application-only study and the evidence needed to waive prior competencies. The [learning contract](curriculum/README.md#learning-contract) keeps project requirements consistent across paths.


<a id="the-curriculum-itself"></a>
## Curriculum at a glance

Six subject groups, called **strata**, organise the module pages. Numbers are stable identifiers, not a requirement to take every module in numerical order. [Why M19/M20 are absent](FAQ.md#structure).

| Browse | Modules | Focus |
|---|---|---|
| [Foundations](curriculum/README.md#foundations) | M0–M5 | Proofs, Python, calculus, linear algebra, algorithms, probability |
| [Statistics & Data](curriculum/README.md#statistics-and-data) | M6, M6½, M7, M8a, M8b | Inference, causal reasoning, data analysis, SQL, distributed systems |
| [Classical ML](curriculum/README.md#classical-ml) | M9–M12 | Regression, classification, clustering, ensembles |
| [Probabilistic ML](curriculum/README.md#probabilistic-ml) | M13–M14 | Bayesian inference, MCMC, time series |
| [Deep Learning](curriculum/README.md#deep-learning) | M15–M17 | Neural networks, transformers, generative models, reinforcement learning |
| [Frontier & Production](curriculum/README.md#frontier-and-production) | M18, M21–M26 | LLMs, retrieval, agents, safety, MLOps, product work, capstone |

<details>
<summary>Visual overview (optional)</summary>

<img src="assets/hero-banner.jpg" alt="Data Science and AI Roadmap, from foundations to production AI" width="720">

<img src="assets/roadmap-overview.jpg" alt="Overview of the six curriculum strata; the text table above provides their module ranges and topics" width="720">

</details>

<a id="roadmap"></a>
<a id="a-rigorous-free-first-path-from-foundations-to-production-ai"></a>
<a id="-where-everything-lives"></a>
<a id="guides-and-reference--when-you-need-them"></a>
## Useful links

- **Study help:** [Read a module](guides/how-to-read-a-module.md#reading-order) · [Choose a resource](guides/how-to-read-a-module.md#pick-one) · [Optional guided companions](guides/companion-curricula.md) · [Get unstuck](guides/how-to-read-a-module.md#common-ways-people-get-stuck).
- **Building AI systems:** [Portfolio Spine: one system, five levels](guides/portfolio-spine.md#portfolio-spine) · [`DECISIONS.md` template](resources/templates/DECISIONS.md) · [NumPy From Scratch harness](resources/numpy-from-scratch/README.md#numpy-from-scratch) · [Agent labs (M22)](coursepages/m22-agentic-ai/README.md#labs) · [Evaluation harness (M24)](coursepages/m24-mlops-llmops-agentops/README.md#evaluation-harness).
- **References, when needed:** [Books](resources/books.md) · [Toolchain](resources/toolchain.md) · [Citation key](guides/sources.md#citation-key) · [Career planning](guides/career-operations.md). Supporting course pages are linked beside their modules in the [index](curriculum/README.md#all-modules).
- **Career evidence:** [India undergraduate and international options](guides/india-undergraduate-path.md) · [Employer research and eligibility limits](audit/career-research-2026-11-05.md) · [Opportunity log template](resources/templates/OPPORTUNITIES.md).
- **Report a problem:** [Confusing instructions or a broken link](https://github.com/akazadivu-design/data-sci/issues/new/choose) · [Contribution guide](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md).

<details>
<summary>About the roadmap and maintenance</summary>

## Goal

Develop mathematical and programming foundations, apply them to data and ML problems, and build documented projects. Study duration depends on prior knowledge, chosen scope, practice, and available time—not a promised hiring date. See [planning estimates and their limits](FAQ.md#how-long).

## Who this is for

Beginners, returning learners, analysts, engineers, and research-oriented learners. Choose the depth your goals require; this independent roadmap does not award a university credential or imply institutional affiliation.

### Maintainer material — safe to ignore as a learner

[Changelog](CHANGELOG.md#refresh-log) · [Current overhaul audit](audit/overhaul-2026-11-05.md) · [Foundations improvement proposal](audit/Foundations_M0-M5_Improvement_Plan.md) · [Repository tools](tools/README.md).

Earlier improvement proposals and verification logs are historical. The current modules and learning contract govern study; the active maths placement is optional and the older diagnostic tables are non-operational. See the [research record](audit/research-2026-11-05.md) for the current evidence and limitations.

</details>

<a id="acknowledgements"></a>
<a id="-acknowledgements--attribution"></a>
## Acknowledgements & Attribution

<details>
<summary>University sources and artwork attribution</summary>

The roadmap draws on public courses, syllabi, books and documentation. Degree/program pages provide context; they are not free lecture routes or institutional endorsements. The [default-resource table](guides/how-to-read-a-module.md#pick-one) identifies the selected learning route and its access conditions.

* **IIT Madras** — [study.iitm.ac.in/ds](https://study.iitm.ac.in/ds/) (BS in Data Science and Applications, 2025–26).
* **Harvard University** — [CS50P](https://cs50.harvard.edu/python/), [CS50 SQL](https://cs50.harvard.edu/sql/), [Stat 110](https://stat110.hsites.harvard.edu/) and [CS109A public materials](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html).
* **Massachusetts Institute of Technology** — [OCW](https://ocw.mit.edu/) for calculus, linear algebra, algorithms and statistics; [6.7960 Fall 2024](https://ocw.mit.edu/courses/6-7960-deep-learning-fall-2024/) for public deep-learning lectures; [6.S191](https://introtodeeplearning.com/) for an applied companion. The inaccessible Spring 2026 introductory-ML page is no longer a lecture default.
* **University of Cambridge** — [cl.cam.ac.uk/teaching/2526](https://www.cl.cam.ac.uk/teaching/) (Part IA/IB/II), [mlmi.eng.cam.ac.uk](https://www.mlmi.eng.cam.ac.uk/) (MPhil MLMI 2026 entry).
* **Stanford University and ISLP authors** — [ISLP free recordings](https://www.statlearning.com/online-courses), [CS336](https://cs336.stanford.edu/) and [CS246 public notes](https://web.stanford.edu/class/cs246/). CS246's current recordings are enrollment-only; M8b uses a separate free video route.
* **UC Berkeley** — selected [Spring 2024 safety/evaluation/security lectures](https://rdi.berkeley.edu/understanding_llms/s24), plus [CS285](https://rail.eecs.berkeley.edu/deeprlcourse/) and [LLM Agents MOOC](https://llmagents-learning.org/) as scoped companions.
* **CMU / UMich (Product-DS anchors)** — [heinz.cmu.edu](https://www.heinz.cmu.edu/programs/public-policy-management-master/data-analytics) (MSPPM-DA) · [si.umich.edu](https://www.si.umich.edu/programs/master-applied-data-science) (MADS).
* **Hugging Face** — [huggingface.co/learn](https://huggingface.co/learn) (Agents Course, Smol Course, Smol Training Playbook).
* **Microsoft** — [Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) and [ML for Beginners](https://github.com/microsoft/ML-For-Beginners), used as project-based companion curricula with quizzes, assignments, and guided lesson navigation.
* **Independent teaching communities and authors** — [Data School](https://www.dataschool.io/easier-data-analysis-with-pandas/), [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp), [FSDL](https://fullstackdeeplearning.com/course/2022/), and the authors cited in the [book catalogue](resources/books.md).
* **Model Context Protocol project** — [released 2026-07-28 specification](https://modelcontextprotocol.io/specification/2026-07-28). Mechanistic-interpretability sources are credited separately at [Transformer Circuits](https://transformer-circuits.pub/).

All university material remains © their respective institutions; this repository only cites and organises publicly‑disclosed syllabi.

**Images.** Artwork provenance is recorded in [`assets/README.md`](assets/README.md). `hero-banner.jpg` and `roadmap-overview.jpg` are AI-generated originals; the six `stratum-*.jpg` section banners are drawn programmatically by [`assets/make_banners.py`](assets/make_banners.py) (Pillow only, deterministic — re-run it to regenerate or restyle them). No stock photography, no commercially-licensed imagery, and no images scraped from third-party pages are used anywhere in this repository. See [`assets/README.md`](assets/README.md).


</details>

---

**Start small. Practise deliberately. Build and explain your work.**

[Start here](START-HERE.md#first-step) · [All modules](curriculum/README.md#all-modules) · [Resume](guides/progress-tracker.md#resume)
