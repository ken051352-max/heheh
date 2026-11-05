[Home](../README.md) · [First semester](first-semester.md#semester-plan) · [Tracker](progress-tracker.md#resume)

# Readiness checks: find the next useful practice

These checks help you decide what a dependent task needs. They do not decide who belongs in CS or AI. Optional [maths placement](../curriculum/1-foundations.md#math-diagnostic) remains separate and never blocks Python.

[How to check](#how-to-check) · [Python basics](#python-basics) · [Loops and errors](#loops-and-errors) · [Testing and files](#testing-and-files) · [Validation](#input-contracts) · [Objects](#objects-and-data-flow) · [M1 exit](#m1-ready) · [SQL](#sql-ready) · [Data](#data-ready) · [College equivalence](#college-equivalence)

<a id="how-to-check"></a>
## The same four-part pattern

Spend one short session, roughly 15–25 minutes as an initial planning budget, on the relevant check. Take longer if access or reading is the issue. Write a first attempt before opening reviewer notes.

1. **Explain:** recall the idea and a limitation in your own words.
2. **Read:** predict a small code example, calculation or data transformation before running it.
3. **Debug:** identify the cause of a deliberately wrong result; explain why the repair works.
4. **Transfer:** apply the idea to changed input, including a boundary case.

Record **ready for this next task**, **revisit a named capability**, or **not attempted** with your answer/code, the changed input and next action. There is no total score or pass percentage. A check may establish a narrow capability while a module remains **partial**. Mark full-module completion only against its core outcomes and project rubric.

**Assistance:** use documentation, worked examples, classmates or AI explanations during learning; identify that help in your note. For the final changed example, close generated solutions and work independently, then verify. Requesting hints or feedback is useful; copying an answer and obtaining green tests is not independent evidence. Respect a course's own rules for its assignments, including [CS50's academic honesty policy](https://cs50.harvard.edu/python/honesty/).

**If a check exposes a gap:** use its repair task, then retry with different values on a later session. If the same gap persists, ask for an explanation of the specific failed step. A reviewer can discuss one function or calculation; they need not audit your entire repository.

For later modules, reuse this pattern on the stated strict prerequisites: one relevant explanation, a worked trace, a failure and a changed example. Preserve each module's statistical assumptions, project tests and evaluation rubric; this pattern does not replace them.

<a id="python-basics"></a>
## Python basics — Weeks 1–2

**Needed next:** functions and conditions before multi-step loops or the calculator.

1. Explain the difference between `print(value)` and `return value`. What type does `input()` return?
2. Predict `share(12, 3)` and `share(0, 3)` for `def share(total, people): return total / people`. Identify the two inputs and one result.
3. A learner writes `if people: return total / people` to reject invalid group sizes. Explain the result for `people = -2` and fix the condition for integer group sizes greater than zero. Type conversion comes before this function.
4. Implement the corrected function and show outcomes for `people = 0`, `1` and `4`. For now it can return `None` for an invalid group size; exceptions arrive in Week 4. Explain the contract rather than silently changing it.

**Observable evidence:** correct predictions, a condition that rejects non-positive integers, and a stated invalid-input policy. Tasks 1–2 are sufficient at Week 1; tasks 3–4 follow the conditionals lesson.

<details>
<summary>Reviewer notes and targeted repair</summary>

`input()` returns text. `print` displays; `return` supplies the caller's value. The valid results are `4.0` and `0.0`. Negative integers are truthy, so `if people` is insufficient: check `people > 0`. For total 12, group sizes 0, 1 and 4 give `None`, `12.0` and `3.0` under the stated contract. Returning `None` is a deliberate early contract, not the later calculator's error contract.

If values/types are confused, trace [CS50P Lecture 0](https://cs50.harvard.edu/python/weeks/0/) with the literal text `"12"` and numeric `12`. If the condition fails, replay the comparison examples in [Lecture 1](https://cs50.harvard.edu/python/weeks/1/) and write a three-row truth table for `-1`, `0`, `1`. Retry with total 20 and people 5; do not restart all of Week 0.

</details>

**Next:** [Week 3](first-semester.md#week-3).

<a id="loops-and-errors"></a>
## Loops and errors — Weeks 3–4

**Needed next:** accumulate values and report malformed input before automating larger workflows.

1. Explain an accumulator and why its initial value depends on the operation.
2. Trace this function for `[2, 5]` and `[]`. What is wrong with it?

```python
def total(values):
    for value in values:
        result = 0
        result += value
    return result
```

3. Repair the loop. Then explain why wrapping the entire program in `except Exception: return 0` would hide useful information when converting the text `"oops"` to a number.
4. Use your calculator to handle `7 / 2`, `7 / 0` and a nonnumeric operand. For the permitted guessing-game alternative, demonstrate guesses below, equal to and above a fixed target plus malformed input; if attempts are limited, check the final allowed attempt under your stated policy. Add one changed input or target and explain whether it should succeed or fail.

**Observable evidence:** an empty input returns the documented neutral total, multiple values accumulate, and invalid input is distinguished from a valid zero result. Tasks 3–4 follow the exception lesson.

<details>
<summary>Reviewer notes and targeted repair</summary>

The original returns 5 for `[2, 5]` and raises `UnboundLocalError` for `[]`. Initialize `result = 0` before the loop, giving 7 and 0. Catch the expected conversion error near the conversion and report invalid input; a broad exception returning 0 can turn failure into apparently valid data. A calculator may raise documented exceptions at its function boundary and show a friendly message at its CLI boundary. Do not require one exact message wording.

If accumulation is unclear, step through [CS50P Lecture 2](https://cs50.harvard.edu/python/weeks/2/) and trace `result` after each item of `[3, 0, -1]`. If failure paths are unclear, use [Lecture 3](https://cs50.harvard.edu/python/weeks/3/) and implement one conversion with a specific exception. Retry your chosen starter with a changed input, using the calculator's [assessment](../resources/beginner-projects/calculator/README.md#assessment) or the game cases above. For a fixed target of 5, guesses 4, 5 and 6 should follow lower, correct and higher branches; malformed input must follow the declared error policy. Keep a fixed target in tests so randomness cannot hide a comparison bug.

</details>

**Next:** [libraries](first-semester.md#week-5), then tests.

<a id="testing-and-files"></a>
## Testing and files — Weeks 6 and 8

**Needed next:** meaningful automated checks and reproducible local I/O before Weather caching.

1. Explain why a test needs an expected result determined independently of the implementation.
2. A supposed test is `assert total(values) == total(values)`. Replace it with a hand-checkable multi-item case and an empty-input case. Deliberately reset the accumulator inside the loop and show which assertion catches the bug.
3. Explain the difference between an absent file, malformed JSON and a missing required JSON field. What should remain unchanged if parsing fails?
4. Read a small fixture, write a summary to a different temporary path, and show a missing-file failure. Repeat with changed fixture data; verify the original bytes are unchanged.

**Observable evidence:** the mutation is detected, outputs match independently calculated expectations, failure categories remain visible, and tests use temporary paths rather than modifying the fixture. Tasks 1–2 follow Lecture 5; 3–4 follow Lecture 6 and the JSON examples from Lecture 4.

<details>
<summary>Reviewer notes and targeted repair</summary>

For example, `total([3, -1, 2])` should equal 4 and `total([])` should equal 0. Calling the same function twice only checks equality of its outputs and may accept the same wrong answer. Missing files are I/O failures; malformed JSON cannot be decoded; valid JSON may still violate the application's schema. Preserve the original fixture and avoid overwriting a previously valid result with partial output.

For weak tests, revisit [Lecture 5](https://cs50.harvard.edu/python/weeks/5/) and the [beginner test guide](../resources/beginner-projects/README.md#tests), then invent one bug the test should catch. For file confusion, revisit [Lecture 6](https://cs50.harvard.edu/python/weeks/6/) and trace input/output paths on paper before running. Retry with a fresh temporary directory.

</details>

**Next:** [input validation](first-semester.md#week-9) and the [Weather stages](../resources/beginner-projects/weather/README.md#stages).

<a id="input-contracts"></a>
## Input contracts — Week 9

The exercise contract accepts one or more lowercase ASCII letters, one hyphen, and one or more ASCII digits, with no leading/trailing text. It is an identifier example, not a claim about valid city names.

1. Explain why an input contract must state the whole accepted value, not just one matching substring.
2. Predict validity of `campus-12`, `campus-12 extra`, `-12` and `lab-0` under that contract.
3. A program accepts `bool(re.search(r"[a-z]+-[0-9]+", value))`. Find the unwanted acceptance and repair it with a whole-string match.
4. Test one new valid identifier and one new invalid identifier. Explain why a matching identifier says nothing about whether it exists in a database.

**Observable evidence:** accept the first/fourth values, reject the second/third, repair substring matching, and distinguish syntax from existence.

<details>
<summary>Reviewer notes and targeted repair</summary>

Use `re.fullmatch(r"[a-z]+-[0-9]+", value)` for the stated contract. `re.search` accepts a matching substring inside the extra-text input. For example, `hall-203` is valid and `Hall-203` is invalid under this deliberately lowercase contract. Different real applications may choose other contracts; do not silently change this one. Typed JSON numbers, timestamps and domain values still need appropriate type/range/semantic checks.

Repair by marking the exact substring found by `search` in the bad input, then revisit [CS50P Lecture 7](https://cs50.harvard.edu/python/weeks/7/) and compare search with full matching on a new pair of strings.

</details>

**Next:** [objects and data flow](#objects-and-data-flow).

<a id="objects-and-data-flow"></a>
## Objects and data flow — Weeks 10–11

1. Explain instance state and a method. When would a dictionary plus functions be simpler?
2. Predict the final `(a.value, b.value)` below before running it.

```python
class Reading:
    def __init__(self, value):
        self.value = value

a = Reading(12)
b = Reading(20)
a.value = 15
```

3. If instead a class defines `values = []` in its body and each instance appends to `self.values`, explain why two instances may share readings. Repair the design when each should own its own list.
4. Create a third reading with a different value; explain where you would reject invalid data and write a small check for that contract. Do not add inheritance solely to demonstrate syntax.

**Observable evidence:** separate state is understood; a shared mutable attribute is identified; validation is attached to a deliberate boundary.

<details>
<summary>Reviewer notes and targeted repair</summary>

The result is `(15, 20)`. An instance's `self.value` is separate from another instance's. A mutable class attribute is shared unless deliberately shadowed; for independent lists, initialize `self.values = []` in `__init__`. Different architectures may validate at construction or an input parser; require an explicit contract and a test, not a particular class design.

Repair by drawing two boxes for two instances and a separate box for class attributes while replaying [CS50P Lecture 8](https://cs50.harvard.edu/python/weeks/8/). Retry with two empty lists and add one value to only one object. For comprehension/loop confusion, use [Lecture 9](https://cs50.harvard.edu/python/weeks/9/) with three values and an empty list.

</details>

**Next:** [Weather implementation](first-semester.md#week-12).

<a id="m1-ready"></a>
## M1 exit — before SQL, data work or M4

This is a demonstration of [M1 core](../curriculum/1-foundations.md#module-1), not a requirement to finish every Python reference or advanced extension. Complete the starter, the Weather project rubric and the relevant language outcomes from CS50P or equivalent work.

An existing project may replace rebuilding Weather when it demonstrates the same input, API/fixture, file/cache, failure and testing outcomes. Map that evidence using [college/prior-study equivalence](#college-equivalence), then perform the changed-case check. Missing outcomes need targeted work, not a repeat of the whole course.

1. **Explain:** trace city input → validation → fetch/cache decision → JSON validation → displayed result in your own Weather CLI. State what its offline fixture proves and what it cannot establish about live service reliability.
2. **Read:** choose a short unfamiliar function, predict its output for a normal input and its behavior for a boundary input, then run it. Explain imports, return values, local state and any file/API effects. Also retain the [objects check](#objects-and-data-flow) or equivalent class-reading evidence.
3. **Debug:** deliberately introduce one relevant defect in a copy of your work, such as accepting an expired cache or swallowing malformed data. Show that an appropriate test fails, diagnose the cause and repair it. Do not merely edit an expected value to make the test green.
4. **Transfer:** add a changed input/failure case not copied from the supplied fixtures. Reproduce the project from its README in an isolated environment and explain its result without generated code or reviewer prompts.

**Evidence bundle:** your implemented starter and Weather code, normal/invalid-input transcripts, offline and mocked-failure tests, pinned environment instructions, README and honest memo. Include evidence for function/data-structure use, exceptions, modules, file I/O, basic testing, reading a class and simple input validation. The [Weather assessment](../resources/beginner-projects/weather/README.md#assessment) supplies detailed behavioral criteria. Public hosting, live paid APIs, advanced typing, async and CI are not M1 gates.

**Remediation:** choose the failed category: [control flow](#loops-and-errors), [tests/files](#testing-and-files), [objects](#objects-and-data-flow), or the exact [Weather stage](../resources/beginner-projects/weather/README.md#stages). Keep M1 active and defer dependent projects until the missing capability is demonstrated. You may continue unrelated college mathematics while repairing Python.

**Next:** [SQL preview](first-semester.md#week-15), [M7](../curriculum/2-statistics-and-data.md#module-7), or [M4](../curriculum/1-foundations.md#module-4), one chosen priority at a time. The manifest's prerequisites remain unchanged.

<a id="sql-ready"></a>
## SQL investigation — filtering, joins and reconciliation

After M1, this check supports the [read-only query preview](../resources/beginner-projects/sql/README.md#query-preview); it does **not** waive full M8a. The sandbox supplies its schema and clean data. Learners write queries before implementing ingestion or transactions.

Use this tiny hypothetical example, separate from the project fixture:

- `customers`: `(1, "Asha")`, `(2, "Ravi")`, `(3, "Noor")`, with primary key `customer_id`.
- `orders`: `(10, 1, 500)`, `(11, 1, 700)`, `(12, 2, 300)`, with columns `order_id`, `customer_id`, `amount_paise`. Primary key `order_id`; customer ID references customers.

1. Explain each table's row meaning (grain), its primary key and the foreign-key relationship. Why keep the unit in the column name?
2. Predict the number of orders and total paise for customer 1. Write a filtered query and compare it with hand arithmetic.
3. A report groups by customer name after a cross join. Explain the inflated total. Repair it to return **all three customers**, including the one with no orders, and count orders correctly.
4. On paper, add a fourth order for Ravi and recalculate totals. Compare with the same changed data in a disposable reviewer-loaded database when available. Explain why two orders with equal amounts are still two orders. Implementing inserts or transaction handling is not part of this query preview.

**Observable evidence:** 2 orders and 1,200 paise for Asha; correct join keys; zero orders for Noor; and a reconciled total for the changed example. Do not require ingestion or rollback implementation to finish this preview.

<details>
<summary>Reviewer notes and targeted repair</summary>

The original order total is 1,500 paise. Cross joining to three customers produces 9 rows and repeats the amount three times, summing to 4,500. A left join on customer ID preserves Noor; `COUNT(order_id)` counts non-null order IDs, whereas `COUNT(*)` counts the outer row. Use `COALESCE(SUM(amount_paise), 0)` when the report defines no orders as zero. Group by stable customer ID as well as the name; people can share names. A new 200-paise order for Ravi brings the total to 1,700, with 500 for Ravi. That is an example changed case, not an imposed project fixture.

Repair a grain or filtering gap with [CS50 SQL Querying](https://cs50.harvard.edu/sql/weeks/0/). Repair joins by drawing the three relationships and using [Relating](https://cs50.harvard.edu/sql/weeks/1/). For later M8a schema/ingestion stages, continue to [Designing](https://cs50.harvard.edu/sql/weeks/2/) and Writing before implementing inserts and transactions. At that stage, observe the supplied schema rejecting duplicate order IDs and unknown customer IDs under enabled foreign-key constraints; then implement and test your own ingestion contract. SQLite foreign-key enforcement must be enabled on the connection. SQLite `EXPLAIN QUERY PLAN` describes a plan; it is not PostgreSQL's measured `EXPLAIN ANALYZE` output. None of those later implementation tasks is an extra Week 16 requirement.

</details>

**Next:** record the query preview as partial, then choose fuller M8a or M7 at the [semester review](first-semester.md#semester-exit). The kit's [full assessment](../resources/beginner-projects/sql/README.md#assessment), including ingestion, replay and plan evidence, belongs to subsequent M8a study.

<a id="data-ready"></a>
## Before M7 — preserve data and explain a denominator

1. Explain the difference between a missing value and a measured zero. State the population and unit behind a proposed average.
2. Given readings `10`, missing, `20` for three scheduled observations, calculate the mean of observed values and the observation count. State what is unknown about the missing reading.
3. A cleanup fills missing values with zero and reports a mean of 10 without explanation. Identify the assumption and revise the report. Explain why dropping a repeated row without a key might remove a real repeated event.
4. With one additional observed value of 30, update your summary. Save raw inputs separately, a small transform, a check and a two-sentence limitations note. Python's standard library is enough; pandas is learned in M7.

**Observable evidence:** observed-only mean 15 across 2 of 3 observations; no claim that the missing reading is zero; after adding 30 the observed mean is 20 across 3 of 4 scheduled observations; an explicit key/duplicate policy and unchanged raw data.

**Repair:** replay the dictionaries/CSV examples in [CS50P File I/O](https://cs50.harvard.edu/python/weeks/6/) if data access is the gap. For data meaning, draw a four-row table and annotate observed/missing before computing anything. Then read M7's [core outcome and project](../curriculum/2-statistics-and-data.md#module-7). This is introductory data reasoning; statistical missingness mechanisms and inference are later study.

**Next:** start one [M7 question-led investigation](../curriculum/2-statistics-and-data.md#module-7), preserving its full project and visualization requirements.

<a id="college-equivalence"></a>
## Use college or prior study as evidence

Do not repeat a whole course merely because its title differs. Map the prerequisite's **actual capability** to a permitted example from your work, then demonstrate a changed case.

Record: `module/capability → course or prior work → artifact → independent explanation/change → gaps → next task`. A grade or certificate alone is not enough detail to establish an outcome, but it can point you toward assessed work. Keep coursework private and respect its sharing rules.

- **Programming:** a college assignment plus a fresh failure-case test may satisfy a relevant M1 capability. Map all core outcomes before marking the whole module waived.
- **Mathematics:** explain a derivative and compare it with a numerical difference; solve a small linear system and check substitution; or give a counterexample to a quantified statement. Pick the capability the next module actually needs. Full M2/M3 require their stated broader outcomes and projects or demonstrably equivalent work.
- **CS:** use the [college CS evidence map](four-year-plan.md#cs-core) for algorithms, operating systems, networks, databases and software design. Advanced AI projects do not substitute for those fundamentals.

An unfamiliar notation or one failed exercise calls for targeted practice. Maths placement remains optional; neither a low score nor an unfinished proof course blocks Python. Save **partial**, **waived with evidence**, or **active** accurately in the [tracker](progress-tracker.md#full-tracker).

[Home](../README.md) · [Semester milestones](first-semester.md#semester-plan) · [Recovery](first-semester.md#recovery) · [Record evidence](progress-tracker.md#resume)
