[Home](../README.md) - [Start here](../START-HERE.md)

# How to read a module

Read the outcome, check the prerequisites, choose the default lectures and principal book, then build the project. The additional references are a library to consult when you need them.

<a id="reading-order"></a>
## The learning loop

| Part | What to do |
|---|---|
| Core outcome | Say what you will be able to explain, implement and evaluate. |
| Prerequisites | Demonstrate the needed skills; equivalent prior work counts. Check the [complete inventory](practitioner-track.md#prerequisites). |
| Lecture route | Follow one free course. Use a second explanation for a specific gap. |
| Principal book | Read the relevant sections and solve selected exercises. Paid and free books are selected on quality and labeled by access. |
| Extended topics | Choose depth that serves your goal; do not treat every listed architecture or framework as compulsory. |
| Project | Meet the [learning contract](../curriculum/README.md#learning-contract): reproducible work, validation, README and an honest results memo. |

A module may combine topics from several courses. The roadmap's topic list is its own synthesis; a university name is not evidence that one lecture teaches every bullet. Full-course prerequisites can be stronger than the roadmap's selected core. Read the scope notes before opening an advanced course.

## Choosing books and lectures

**Lectures must have a free route. Books may be paid.** The principal book is the recommended reference for that module, not an instruction to buy the whole catalogue. Consult the [book guide](../resources/books.md#books) for why each title was chosen, which sections matter and when another book is better suited.

For a costly book, use a library, an authorized open edition or the free lecture notes while deciding whether to buy it. Free code, a sample chapter and a full legal ebook are different access categories. A commercial book does not lose its recommendation merely because it costs money.

<a id="pick-one"></a>
<a id="module-default-1"></a>
## One default route and principal book per module

These defaults and the prerequisite inventory come from [the module map](../curriculum/modules.json). The checker detects drift between them. M0 includes free Khan videos and Hammack's proof text; M14's FPP3 includes the authors' embedded lecture videos. M26 is a project, not a lecture course.

<!-- BEGIN MODULE DEFAULTS -->

| Module | Free lecture / course route | Principal recommended book |
| :--- | :--- | :--- |
| [M0 — Maths bridge](../curriculum/1-foundations.md#module-0) | [Free course / lecture route](https://www.khanacademy.org/math/precalculus) | [Book of Proof - Hammack (free)](https://richardhammack.github.io/BookOfProof/) |
| [M1 — Python](../curriculum/1-foundations.md#module-1) | [Free course / lecture route](https://cs50.harvard.edu/python/) | [Python Crash Course - Eric Matthes, 3rd edition (paid)](https://nostarch.com/python-crash-course-3rd-edition) |
| [M2 — Calculus and optimisation](../curriculum/1-foundations.md#module-2) | [Free course / lecture route](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/) | [Calculus: Early Transcendentals - Stewart, Clegg and Watson, 9th edition (paid)](https://www.cengageasia.com/title/default/detail?isbn=9781337613927) |
| [M3 — Linear algebra](../curriculum/1-foundations.md#module-3) | [Free course / lecture route](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) | [Introduction to Linear Algebra - Strang (paid)](https://math.mit.edu/~gs/linearalgebra/) |
| [M4 — Algorithms](../curriculum/1-foundations.md#module-4) | [Free course / lecture route](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | [Introduction to Algorithms - CLRS (paid)](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/) |
| [M5 — Probability](../curriculum/1-foundations.md#module-5) | [Free course / lecture route](https://stat110.hsites.harvard.edu/) | [Introduction to Probability - Blitzstein and Hwang (free online; paid print)](https://stat110.hsites.harvard.edu/) |
| [M6 — Statistical inference](../curriculum/2-statistics-and-data.md#module-6) | [Free course / lecture route](https://ocw.mit.edu/courses/18-650-statistics-for-applications-fall-2016/) | [All of Statistics - Wasserman (paid)](https://link.springer.com/book/10.1007/978-0-387-21736-9) |
| [M6½ — Causal inference and experimentation](../curriculum/2-statistics-and-data.md#module-6-half) | [Free course / lecture route](https://www.bradyneal.com/causal-inference-course) | [Causal Inference: What If - Hernan and Robins (free)](https://miguelhernan.org/whatifbook) |
| [M7 — Wrangling and visualisation](../curriculum/2-statistics-and-data.md#module-7) | [Free course / lecture route](https://www.dataschool.io/easier-data-analysis-with-pandas/) | [Python for Data Analysis - McKinney (free web; paid print)](https://wesmckinney.com/book/) |
| [M8a — SQL and warehouses](../curriculum/2-statistics-and-data.md#module-8a) | [Free course / lecture route](https://cs50.harvard.edu/sql/) | [Database System Concepts - Silberschatz, Korth and Sudarshan (paid)](https://www.db-book.com/) |
| [M8b — Distributed data](../curriculum/2-statistics-and-data.md#module-8b) | [Free course / lecture route](https://github.com/DataTalksClub/data-engineering-zoomcamp) | [Fundamentals of Data Engineering - Reis and Housley (paid)](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) |
| [M9 — Regression](../curriculum/3-classical-ml.md#module-9) | [Free course / lecture route](https://www.statlearning.com/online-courses) | [An Introduction to Statistical Learning with Python (free PDF; paid print)](https://www.statlearning.com/) |
| [M10 — Classification](../curriculum/3-classical-ml.md#module-10) | [Free course / lecture route](https://www.statlearning.com/online-courses) | [An Introduction to Statistical Learning with Python (free PDF; paid print)](https://www.statlearning.com/) |
| [M11 — Unsupervised learning](../curriculum/3-classical-ml.md#module-11) | [Free course / lecture route](https://www.statlearning.com/online-courses) | [An Introduction to Statistical Learning with Python (free PDF; paid print)](https://www.statlearning.com/) |
| [M12 — Ensembles](../curriculum/3-classical-ml.md#module-12) | [Free course / lecture route](https://www.statlearning.com/online-courses) | [An Introduction to Statistical Learning with Python (free PDF; paid print)](https://www.statlearning.com/) |
| [M13 — Bayesian modelling](../curriculum/4-probabilistic-ml.md#module-13) | [Free course / lecture route](https://github.com/rmcelreath/stat_rethinking_2024) | [Statistical Rethinking - McElreath (paid)](https://xcelab.net/rm/) |
| [M14 — Time series](../curriculum/4-probabilistic-ml.md#module-14) | [Free course / lecture route](https://robjhyndman.com/hyndsight/fpp3_videos.html) | [Forecasting: Principles and Practice - Hyndman and Athanasopoulos (free web)](https://otexts.com/fpp3/) |
| [M15 — Deep learning](../curriculum/5-deep-learning.md#module-15) | [Free course / lecture route](https://ocw.mit.edu/courses/6-7960-deep-learning-fall-2024/) | [Deep Learning: Foundations and Concepts - Christopher and Hugh Bishop (free web; paid print)](https://www.bishopbook.com/) |
| [M16 — Transformers and representations](../curriculum/5-deep-learning.md#module-16) | [Free course / lecture route](https://ocw.mit.edu/courses/6-7960-deep-learning-fall-2024/) | [Deep Learning: Foundations and Concepts - Christopher and Hugh Bishop (free web; paid print)](https://www.bishopbook.com/) |
| [M17 — Reinforcement learning](../curriculum/5-deep-learning.md#module-17) | [Free course / lecture route](https://www.davidsilver.uk/teaching/) | [Reinforcement Learning: An Introduction - Sutton and Barto (free draft; paid print)](http://incompleteideas.net/book/the-book-2nd.html) |
| [M18 — LLMs and post-training](../curriculum/6-frontier-production.md#module-18) | [Free course / lecture route](https://cs336.stanford.edu/) | [Build a Large Language Model (From Scratch) - Raschka (paid; free code)](https://www.manning.com/books/build-a-large-language-model-from-scratch) |
| [M21 — Retrieval and RAG](../curriculum/6-frontier-production.md#module-21) | [Free course / lecture route](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/) | [AI Engineering - Huyen (paid)](https://huyenchip.com/books/) |
| [M22 — Agents and MCP](../curriculum/6-frontier-production.md#module-22) | [Free course / lecture route](https://huggingface.co/learn/agents-course/) | [AI Engineering - Huyen (paid)](https://huyenchip.com/books/) |
| [M23 — Safety and evaluations](../curriculum/6-frontier-production.md#module-23) | [Free course / lecture route](https://rdi.berkeley.edu/understanding_llms/s24) | [AI Engineering - Huyen, evaluation chapters (paid)](https://huyenchip.com/books/) |
| [M24 — Production operations](../curriculum/6-frontier-production.md#module-24) | [Free course / lecture route](https://fullstackdeeplearning.com/course/2022/) | [Designing Machine Learning Systems - Huyen (paid)](https://huyenchip.com/books/) |
| [M25 — Product data science](../curriculum/6-frontier-production.md#module-25) | [Free course / lecture route](https://www.storytellingwithdata.com/videos) | [Trustworthy Online Controlled Experiments - Kohavi, Tang and Xu (paid)](https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/D97B26382EB0EB2DC2019A7A7B518F59) |
| [M26 — Capstone](../curriculum/6-frontier-production.md#module-26) | Use your chosen capstone topic | Choose the reference for your capstone topic |

<!-- END MODULE DEFAULTS -->

**Companions with a clear job:** [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) supplies applied ML practice; [fast.ai](https://course.fast.ai/) supplies applied deep-learning practice; [Microsoft's beginner curricula](companion-curricula.md) provide guided exercises. They supplement selected outcomes rather than add another compulsory course.

<a id="access-audit-table"></a>
## Access and compute

| Route | Lectures/materials | Practice and accounts | Cost boundary |
|---|---|---|---|
| MIT OCW, archived university course pages | Use the selected OCW recording archive; slides or a current syllabus alone do not establish video access | Public exercises where supplied; institutional grading is not included | Self-study notes and projects replace unavailable course grading |
| ISLP, Data School, Data Engineering Zoomcamp | Follow the public video links from the author/course page | ISLP Python labs and local data exercises; substitute local labs for Zoomcamp cloud tasks | Associated edX enrollment and cloud credits are not assumed free |
| CS50P / CS50 SQL | Free public lectures and notes | Course submission tools can require free accounts; local project work is supported | A verified edX certificate is optional and separate |
| McElreath / Silver / Hyndman | Public author lecture links | Local exercises and code; no course enrollment required | Rethinking's main book is paid; Silver and FPP3 have free texts |
| FSDL / Hugging Face | Public lecture/course materials | Some original labs use service accounts or hosted APIs | Follow this roadmap's local lab route; hosted services and credits are not assumed free |
| Berkeley safety lectures / BlueDot / Storytelling with Data | Berkeley has selected public lecture videos; Storytelling with Data links public videos | BlueDot's full course materials require a free account; facilitated cohorts, premium archives and feedback have separate terms | The default uses selected public videos and requires no paid lecture or cohort |
| Recommended books | Author/publisher links and access labels in the catalogue | Editions can use different exercise numbers and software | Paid print/ebook, authorized free text and sample/code-only access are labeled separately |

Provider access can change. A successful page fetch verifies the content visible to the research tool, not enrollment, every exercise, a regional entitlement or a live GPU allocation. The [evidence policy](sources.md#evidence-policy) records these distinctions.

**Compute rule:** required projects have a small local route. Mocked provider responses test engineering contracts; they do not prove model quality. Training, retrieval and answer-quality outcomes require a real, suitably small model or dataset. Report platform, versions, seeds, workload and runtime. Larger GPU experiments and paid API comparisons are extensions.

## A worked example: M9

1. Check Python, gradients, linear algebra and probability. Review inference before interpreting coefficient uncertainty.
2. Follow ISLP's public regression/resampling/regularization videos and corresponding Python chapter labs.
3. Implement a small regression solver and verify it against known data and a numerical library.
4. Use the [leakage-safe rubric](../curriculum/3-classical-ml.md#leakage-safe-rubric) to compare a baseline and fitted pipeline on untouched data.
5. Save the evaluation, limitations, README and results memo. The project can reuse your EDA data pipeline.

<a id="stuck-or-unmotivated"></a>
## A useful 15-minute restart

| Situation | Next action |
|---|---|
| Hard to start | Open the current [Week 0](week-0.md#week-0-plan) task and do one example. |
| Too tired | Use the [bad-day version](week-0.md#week-0-bad-day); stop when it is done. |
| Missed several sessions | Follow the [resume checklist](progress-tracker.md#resume). |
| Code fails | Write expected versus actual behavior and reduce it to a small example. |
| Lecture makes no sense | Identify the missing term; revisit its prerequisite or try one companion explanation. |
| Watched but cannot implement | Close the lesson and rebuild one small example, then compare. |
| Comparing yourself with others | Look at your own earlier work and record one improved capability. |

<a id="common-ways-people-get-stuck"></a>
## Common traps

Collecting courses is not progress on an unfinished project. A fixed problem quota, a paid certificate, public posting and a hiring outcome are not module exit criteria. Choose one next artifact and make its quality reviewable. A partial route is legitimate when its missing competencies are recorded; it is not completion of the full module.
