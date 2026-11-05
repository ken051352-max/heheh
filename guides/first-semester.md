[Home](../README.md) · [Start here](../START-HERE.md) · [Progress tracker](progress-tracker.md#resume)

<a id="semester-plan"></a>
# First semester: one task at a time

**Start with [Week 0](week-0.md#week-0), then use the milestone below that matches your demonstrated skills.** Already programming? Try the [readiness checks](readiness-checks.md#how-to-check), save evidence and skip the material you can already use. Returning? Use [recovery](#recovery).

[Find this week's milestone](#milestones) · [Workload and scope](#workload-and-scope) · [Missed-week recovery](#recovery)

This is the **single first-semester schedule**. [Week 0](week-0.md) and the [first 30 days](first-30-days.md) supply its opening lesson instructions; they are not extra courses. The [four-year plan](four-year-plan.md#s1) places this sequence in your degree.

## Workload and scope

**Planning assumption:** a short orientation followed by 16 study weeks, usually 5–7 hours a week outside college. This is a budget to try, not a measured completion time. Reserve roughly half of each available week for doing and checking; adjust that split if the lecture, project or a prerequisite needs longer. Spread a lecture across sessions. Weeks 7 and 14 are buffers, movable to your exam dates. At 2–3 hours a week, spread each milestone over multiple calendar weeks. At a higher budget, deepen the current project before adding another subject.

- **Do now:** one Python learning spine, small programs, tests, file handling, explanation and an offline Weather CLI. College maths and CS remain the main parallel courses; save relevant work as [equivalence evidence](readiness-checks.md#college-equivalence).
- **Next:** after demonstrated [M1 competence](readiness-checks.md#m1-ready), a small SQL/data investigation. The final two weeks are movable introductory M8a work, **not M7 or M8a completion**. If M1 needs the whole semester, defer SQL.
- **Later depth:** M4 algorithms after M1, fuller M7/M8a projects, M2/M3 gaps identified from college, then route-specific prerequisites. Async, agents, cloud accounts, distributed systems and multiple frameworks do not belong on this semester's required list.

**Lecture default:** free [Harvard CS50P](https://cs50.harvard.edu/python/), whose numbered course weeks differ from these study weeks. Public video pages also offer notes, transcripts and downloadable recordings. The roadmap selects practice to demonstrate outcomes; a CS50 certificate requires the course's own complete requirements. If a lecture is inaccessible, use its notes and examples temporarily and record the access problem. No purchase, submission account or public repository is a completion gate.

**Book choice:** Eric Matthes, [*Python Crash Course*, third edition](https://nostarch.com/python-crash-course-3rd-edition), is the paid principal beginner reference. Read the selected sections below when an explanation helps; do not buy or finish it to begin. Al Sweigart's [*Automate the Boring Stuff with Python*, third edition](https://automatetheboringstuff.com/3e/), is the legal free-text alternative. Choose one, not both. Chapter mappings below were checked against these editions' contents; they are supplementary readings, not claims that the books cover every project requirement. **PCC** and **ATBS** below refer only to those editions.

<a id="milestones"></a>
## Find your milestone

[0: Begin](#week-0) · [1: Functions](#week-1) · [2: Conditions](#week-2) · [3: Loops](#week-3) · [4: Starter](#week-4) · [5: Libraries](#week-5) · [6: Tests](#week-6) · [7: Buffer](#week-7) · [8: Files](#week-8) · [9: Validation](#week-9) · [10: Classes](#week-10) · [11: Reading code](#week-11) · [12: Weather](#week-12) · [13: Failures](#week-13) · [14: Review](#week-14) · [15: SQL](#week-15) · [16: Reconciliation](#week-16)

Each section has one main objective. Keep only its task active; the next link tells you where to resume. Try the [six-week study pilot](study-pilot.md) during any six calendar weeks, for example beginning with Week 1, to test these planning assumptions against your experience. Pilot weeks record observations, not a requirement to finish one milestone each week.

<a id="week-0"></a>
## Week 0 — Run and change a program

- **Learn:** the opening `print`, variables and input examples in [CS50P Lecture 0](https://cs50.harvard.edu/python/weeks/0/), following the [Week 0 instructions](week-0.md#week-0-plan).
- **Read if useful:** PCC chapter 2, Variables and Simple Data Types; or ATBS chapter 1, Python Basics.
- **Practise and save:** change a greeting, predict its output and save code plus one output. This is enough orientation; three finished apps are not required.
- **Ready when:** you can change the name and explain which text is literal and which comes from a variable. Help is allowed; record the part you need to revisit.
- **Next:** [Week 1](#week-1), skipping the Lecture 0 examples you can already explain.

<a id="week-1"></a>
## Week 1 — Turn input into a returned result

- **Learn:** [CS50P Lecture 0, Functions and Variables](https://cs50.harvard.edu/python/weeks/0/); use [the detailed Week 1 task](first-30-days.md#week-1).
- **Read if useful:** PCC chapters 2 and 8 (function arguments and return values); or ATBS chapters 1 and 4 (the corresponding sections).
- **Practise and save:** a two-input bill-share function for valid numeric inputs, its output and a short README in your private `python-journey` folder/repository. Invalid input is a later extension.
- **Check:** [Python basics](readiness-checks.md#python-basics), tasks 1–2. Conditions arrive next week; do not require that check's condition task yet.
- **Next:** [Week 2](#week-2).

<a id="week-2"></a>
## Week 2 — Explain a boundary decision

- **Learn:** [CS50P Lecture 1, Conditionals](https://cs50.harvard.edu/python/weeks/1/); follow [Week 2 practice](first-30-days.md#week-2).
- **Read if useful:** PCC chapter 5, if Statements; or ATBS chapter 2, if-else and Flow Control.
- **Practise and save:** reject a non-positive group size before dividing a bill. Save the outcomes for `-1`, `0`, `1` and `2` and explain the boundary.
- **Check:** finish [Python basics](readiness-checks.md#python-basics). Optional [maths placement](../curriculum/1-foundations.md#math-diagnostic) only chooses a topic to revisit; it never stops Python.
- **Next:** [Week 3](#week-3).

<a id="week-3"></a>
## Week 3 — Trace a loop before running it

- **Learn:** [CS50P Lecture 2, Loops](https://cs50.harvard.edu/python/weeks/2/); follow [Week 3 practice](first-30-days.md#week-3).
- **Read if useful:** PCC chapters 3–4 (lists and iteration), chapter 6 (dictionary basics); or ATBS chapters 3 and 6 (loops and lists).
- **Practise and save:** sum a list of expenses, then count entries meeting a threshold. Save a hand trace for an empty list and a three-item list.
- **Check:** [Loops and errors](readiness-checks.md#loops-and-errors), tasks 1–2. Leave exception handling for Week 4.
- **Next:** [Week 4](#week-4).

<a id="week-4"></a>
## Week 4 — Finish a small original program

- **Learn:** [CS50P Lecture 3, Exceptions](https://cs50.harvard.edu/python/weeks/3/); follow [Week 4](first-30-days.md#week-4).
- **Read if useful:** PCC chapter 10, Exceptions section; or ATBS chapter 4, Exception Handling section.
- **Practise and save:** implement the [calculator starter](../resources/beginner-projects/calculator/README.md#start). Keep a normal run, divide-by-zero run and malformed-input run. A distinct guessing game with the same reasoning/error-handling evidence is an alternative.
- **Check:** finish [Loops and errors](readiness-checks.md#loops-and-errors) and the calculator's [starter assessment](../resources/beginner-projects/calculator/README.md#assessment), or the equivalent game evidence below. Automated tests can wait until Week 6.
- **Next:** [Week 5](#week-5). This is the M1 starter milestone, not full M1 completion.

**If you chose the guessing game:** carry it through Weeks 5–6. Separate deterministic guess evaluation from input/output, then test guesses below, equal to and above a fixed target plus malformed input. If attempts are limited, test the final allowed attempt and state whether invalid input consumes one. Introduce a boundary bug, show a test catching it and repair it. Change the target or limit for your independent explanation. Calculator commands and arithmetic examples apply only to that project; you do not need to build both.

<a id="week-5"></a>
## Week 5 — Separate program logic from its entry point

- **Learn:** [CS50P Lecture 4, Libraries](https://cs50.harvard.edu/python/weeks/4/), especially imports, command-line arguments, JSON and `__name__`.
- **Read if useful:** PCC chapter 8, Storing Your Functions in Modules; ATBS chapter 12, Designing and Deploying Command Line Programs, only the relevant command-line sections.
- **Practise and save:** separate your starter's logic from its entry point (arithmetic for the calculator, guess evaluation for the game). If you used the supplied calculator, inspect and explain its existing separation instead of repeating the edit. Import it without triggering a prompt and compare a function call with a CLI run. Use the [isolated project setup](../resources/beginner-projects/README.md#setup); environment isolation is supplied project guidance, not an assumed topic in Lecture 4.
- **Check:** show a function call and a CLI run that agree. Explain why an import should not request input.
- **Next:** [Week 6](#week-6).

<a id="week-6"></a>
## Week 6 — Make a useful test fail, then fix the cause

- **Learn:** [CS50P Lecture 5, Unit Tests](https://cs50.harvard.edu/python/weeks/5/).
- **Read if useful:** PCC chapter 11, Testing Your Code; or ATBS chapter 5, Debugging. ATBS debugging is reinforcement, not a replacement for the pytest lesson.
- **Practise and save:** run the supplied calculator tests, or write tests for your game's cases listed in Week 4. Implement remaining behavior and add a changed boundary example. Break the calculation or comparison deliberately, observe a relevant failure and restore it. Save the failure and passing run with explanations.
- **Check:** [Testing and files](readiness-checks.md#testing-and-files), tasks 1–2. Review the [six-week pilot](study-pilot.md) and change the remaining schedule using actual effort and difficulty, not imagined progress.
- **Next:** [Week 7](#week-7).

<a id="week-7"></a>
## Week 7 — Catch up or protect exam time

- **Learn:** no new lecture; revisit the specific example in [CS50P Lecture 5](https://cs50.harvard.edu/python/weeks/5/) if a test is still confusing.
- **Read:** no new reading assigned.
- **Practise and save:** repair one earlier readiness gap; if exams take the week, write a resume note and stop. If ready and available, improve your starter's explanation instead of starting another course.
- **Check:** reproduce the last successful result and name the next unfinished capability.
- **Next:** [Week 8](#week-8); use [recovery](#recovery) if the earlier work needs more time.

<a id="week-8"></a>
## Week 8 — Read data without losing the original

- **Learn:** [CS50P Lecture 6, File I/O](https://cs50.harvard.edu/python/weeks/6/), especially `with`, CSV and dictionaries.
- **Read if useful:** PCC chapter 10, Files and Exceptions; or ATBS chapter 10, Reading and Writing Files.
- **Practise and save:** read a small local file into values, write a separate summary file and test a missing file. Start from the Weather project's [fixtures and stages](../resources/beginner-projects/weather/README.md#stages); JSON is introduced in Lecture 4 and the project instructions.
- **Check:** complete [Testing and files](readiness-checks.md#testing-and-files). Explain what remains unchanged when parsing fails.
- **Next:** [Week 9](#week-9).

<a id="week-9"></a>
## Week 9 — Validate a small input contract

- **Learn:** [CS50P Lecture 7, Regular Expressions](https://cs50.harvard.edu/python/weeks/7/). Learn the simple validation examples; complex regex is later depth.
- **Read if useful:** ATBS chapter 9, Text Pattern Matching with Regular Expressions. PCC is not assigned for regex; the lecture notes suffice.
- **Practise and save:** accept a bounded identifier such as `campus-12`; reject an empty value and whitespace in the middle. Explain why a JSON number or date needs its own validation rather than one large regex.
- **Check:** [Input contracts](readiness-checks.md#input-contracts): explain a pattern, predict matches, debug substring acceptance and test changed input.
- **Next:** [Week 10](#week-10).

<a id="week-10"></a>
## Week 10 — Read a class and its state

- **Learn:** [CS50P Lecture 8, Object-Oriented Programming](https://cs50.harvard.edu/python/weeks/8/), focusing on instances, attributes, methods and validation.
- **Read if useful:** PCC chapter 9, Classes. No second book assignment is needed.
- **Practise and save:** a small `Reading` class with a temperature attribute and a display method; compare it with a dictionary and function. Prefer the simpler design in the actual Weather CLI if a class adds no value.
- **Check:** [Objects and data flow](readiness-checks.md#objects-and-data-flow): explain separate instances and one invalid input. Inheritance hierarchies are not needed for this project.
- **Next:** [Week 11](#week-11).

<a id="week-11"></a>
## Week 11 — Read unfamiliar Python and explain a choice

- **Learn:** selected examples in [CS50P Lecture 9, Et Cetera](https://cs50.harvard.edu/python/weeks/9/): unpacking and comprehensions; use notes to locate the examples.
- **Read if useful:** PCC chapter 4, List Comprehensions section, or revisit the functions chapter for a specific gap.
- **Practise and save:** rewrite one short comprehension as a loop, explain equality of results and test an empty list. Trace an unfamiliar function in the supplied project without copying its solution into your own work.
- **Check:** explain a function's input, output, mutation and failure path; apply it to changed data. Record any assistance used.
- **Next:** [Week 12](#week-12).

<a id="week-12"></a>
## Week 12 — Build the Weather CLI in small stages

- **Learn:** revisit the APIs/JSON portion of [CS50P Lecture 4](https://cs50.harvard.edu/python/weeks/4/); the [Weather README](../resources/beginner-projects/weather/README.md#start) supplies the specific adapter/cache contract.
- **Read if useful:** PCC chapter 17, Working with APIs, for the request/response idea; its example service is not the Weather project's API contract. ATBS chapter 18 has JSON sections.
- **Practise and save:** complete the fixture parser and readable output first, then the cache stage. Keep synthetic fixture output clearly labeled. Save the code and one reproducible offline run.
- **Check:** show that malformed data is rejected and a cached result is accepted only within its stated lifetime. Use an injected clock in tests, not a long sleep.
- **Next:** [Week 13](#week-13).

<a id="week-13"></a>
## Week 13 — Explain and test Weather failure paths

- **Learn:** revisit [CS50P Lecture 5](https://cs50.harvard.edu/python/weeks/5/), then follow the project's [assessment](../resources/beginner-projects/weather/README.md#assessment).
- **Read if useful:** PCC chapters 10–11, the relevant exception/testing sections only.
- **Practise and save:** finish mocked request failures, unknown input, malformed data, cache expiry and write-failure cases. Finish the README and results memo. A live free-service experiment is optional and recorded separately from fixtures.
- **Check:** attempt [M1 readiness](readiness-checks.md#m1-ready) without generated solutions. Green reference tests do not demonstrate your own understanding; use your implemented starter and explain changed cases.
- **Next:** [Week 14](#week-14).

<a id="week-14"></a>
## Week 14 — Review M1, or use the second exam buffer

- **Learn:** no new lecture; [CS50P Lecture 6](https://cs50.harvard.edu/python/weeks/6/) is the default revisit for file-handling gaps; substitute the exact lesson named by your failed check.
- **Read:** no new reading assigned.
- **Practise and save:** reproduce your CLI from its README in a clean environment. Explain one design trade-off and one remaining limitation. Use the week for college exams if needed and move this demonstration forward.
- **Check:** all [M1 core evidence](readiness-checks.md#m1-ready), with targeted remediation for any gap. Mark M1 complete only when the evidence exists; otherwise keep it active.
- **Next:** [Week 15](#week-15) if ready; otherwise the next unfinished Weather stage, with SQL deferred.

<a id="week-15"></a>
## Week 15 — Ask a precise question of a small database

- **Before starting:** demonstrated M1 or [equivalent prior work](readiness-checks.md#college-equivalence). This is introductory M8a work; M4 is recommended later for index internals, not required for SQL.
- **Learn:** [CS50 SQL Lecture 0, Querying](https://cs50.harvard.edu/sql/weeks/0/).
- **Read if useful:** ATBS chapter 16, SQLite Databases, for Python/SQLite orientation. M8a's paid principal systems book remains [Database System Concepts](../curriculum/2-statistics-and-data.md#module-8a); no full systems chapter is required for this preview.
- **Practise and save:** open the [supplied SQL query sandbox](../resources/beginner-projects/sql/README.md#query-preview), which loads clean synthetic data for you. Describe its tables' grain and keys; write one read-only filtered query and compare its count with the fixture by hand. Implementing ingestion is later M8a work.
- **Check:** [SQL readiness](readiness-checks.md#sql-ready), tasks 1–2. A count without a defined population is not yet a decision metric.
- **Next:** [Week 16](#week-16).

<a id="week-16"></a>
## Week 16 — Reconcile a join and choose the next term's priority

- **Learn:** [CS50 SQL Lecture 1, Relating](https://cs50.harvard.edu/sql/weeks/1/), especially keys, joins and grouping.
- **Read if useful:** the SQL project's schema/data dictionary; defer detailed system design until [M8a](../curriculum/2-statistics-and-data.md#module-8a).
- **Practise and save:** finish the [read-only query preview](../resources/beginner-projects/sql/README.md#query-preview): reconcile a join at the required grain, retain an entity with no matching rows and explain a bad join. Save your query, expected/actual totals and a short findings note. You are not completing the kit's ingestion, transaction or plan-analysis stages this week.
- **Check:** finish the query-preview tasks in [SQL readiness](readiness-checks.md#sql-ready); use [Data readiness](readiness-checks.md#data-ready) before M7. Schema implementation, inserts/constraints, quarantine/replay, transaction rollback and plan analysis follow CS50 SQL Designing/Writing in later M8a work. A supplied schema and tiny fixture do not demonstrate full M8a migrations, windows or PostgreSQL measured plans.
- **Next:** [semester exit](#semester-exit).

<a id="semester-exit"></a>
## Finish with evidence and one next priority

Record your M1 status, the exact scope of any SQL/data preview, an artifact you can explain, a gap and the next task in the [tracker](progress-tracker.md#full-tracker). Keep a maths/CS equivalence note for material your college already assessed. If SQL has not started, that is a pacing observation, not failure.

Choose **one** next priority using the [India undergraduate path](india-undergraduate-path.md): M4 and college CS fundamentals, M7 data investigation, M8a relational systems, or a specific maths gap. Try a small role experiment later; do not enroll in all six [role pathways](practitioner-track.md#role-pathways). You can remain undecided while building shared foundations.

<a id="recovery"></a>
## Missed a week or failed a check?

1. Open the last saved artifact. Reproduce one successful example; note whether the problem is access, instructions, knowledge or available time.
2. Use the relevant [readiness section](readiness-checks.md#how-to-check) to choose **one** repair task. A syntax gap needs a short example, not a new semester plan.
3. Work for the available session, even 15 minutes. Record what worked and the exact next edit, input or lesson section.
4. Shift all later milestone dates. Use the exam buffers and defer SQL before doubling your workload. Do not restart Week 0 if you can already demonstrate its outcome.

If repeated sessions exceed your budget, reduce the next task or split the milestone. If a resource fails, use its official notes or the selected book and log the access issue. If you are moving easily, try a changed example and explain it before skipping. The [pilot review](study-pilot.md) makes these choices explicit.

[Home](../README.md) · [Week 0](week-0.md) · [Readiness and recovery](readiness-checks.md) · [Record next task](progress-tracker.md#resume)
