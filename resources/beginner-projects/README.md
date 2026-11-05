[Home](../../README.md) · [Semester plan](../../guides/first-semester.md#semester-plan) · [M1 Python](../../curriculum/1-foundations.md#module-1) · [Progress tracker](../../guides/progress-tracker.md)

# Beginner project kit

**Start with the [calculator brief](calculator/README.md#start) after CS50P Lecture 3.** You do not need to understand the other projects yet.

- **Do now:** one small calculator, normal and bad-input runs, and an explanation. Its automated tests can wait until Lecture 5.
- **Next:** the [Weather CLI](weather/README.md#start), after testing and files; finish the remaining M1 outcomes alongside it.
- **Later:** the [SQL/data investigation](sql/README.md#start), after demonstrated M1 competence. This is an introduction to M8a, not the full warehouse project or a substitute for M7 analysis.

Each folder contains `starter.py` with intentional gaps, small fixtures where needed, a brief and a separate worked reference. The command-line shell and data-loading scaffolding are supplied so you can concentrate on the named capabilities. Explain the supplied parts you rely on; running a reference is not your project completion.

<a id="setup"></a>
## Setup once

Use **Python 3.12+**, including its standard-library `sqlite3` module. Run commands from the repository root in an isolated environment. If you already have a working isolated environment for this repository, use it instead of creating another. These examples do not require activation scripts.

```text
python -m venv .venv-beginner
```

**PowerShell:**

```powershell
.venv-beginner\Scripts\python -m pip install -r resources/beginner-projects/requirements.txt
.venv-beginner\Scripts\python --version
.venv-beginner\Scripts\python -m pytest --version
```

**Linux/macOS:**

```bash
.venv-beginner/bin/python -m pip install -r resources/beginner-projects/requirements.txt
.venv-beginner/bin/python --version
.venv-beginner/bin/python -m pytest --version
```

Below, `python` means that environment's interpreter: replace it with the appropriate path above, or activate the environment first. Installing pytest needs an internet connection once; the projects and tests make no network requests. Before Lecture 5 you can run the calculator with Python alone and postpone installing pytest.

Runtime code uses the standard library. [`requirements.txt`](requirements.txt) pins the test runner used for this kit; it is not a complete transitive lock. Record your Python, OS and SQLite versions and save `python -m pip freeze` with your own submission. Do not commit an environment directory. The [toolchain guide](../toolchain.md#toolchain) explains a uv project/lock workflow if you choose it; uv is not an extra prerequisite for these exercises.

<a id="tests"></a>
## Run the tests for your current project

```text
python -m pytest resources/beginner-projects/tests/test_calculator.py -q
python -m pytest resources/beginner-projects/tests/test_weather.py -q
python -m pytest resources/beginner-projects/tests/test_sql.py -q
```

Run only the relevant line. **Starter mode is the default.** Tests reaching unfinished TODO functions initially fail with `NotImplementedError`; supplied Weather-adapter and SQL-preview checks already pass. A failing test is a task to investigate; read its inputs and expected behavior, implement the smallest coherent step, and rerun it. Use `-k arithmetic`, for example, to focus on calculator arithmetic before errors. Do not remove tests or copy the reference merely to turn the output green.

Once you have implemented a project, add at least one justified changed-example test of your own. Explain which mistake it catches. Passing supplied tests covers selected contracts; it cannot establish correctness on all possible inputs.

<a id="reviewer-guide"></a>
## Review without confusing the reference with your work

Reviewers can use the [worked-example notes](REVIEWER.md) and run all supplied reference tests:

```powershell
$env:BEGINNER_IMPL = 'reference'
python -m pytest resources/beginner-projects/tests -q
Remove-Item Env:BEGINNER_IMPL
```

```bash
BEGINNER_IMPL=reference python -m pytest resources/beginner-projects/tests -q
```

**Clear `BEGINNER_IMPL` before assessing the starter.** The environment variable changes test imports; it does not change a command that explicitly names `starter.py` or `reference.py`. CI should select reference mode explicitly. Preserve learner TODOs in the distributed starter.

## One shared submission and assessment pattern

Keep the submission locally, privately or selectively shared. Public hosting, API accounts and certificates are optional. Use the [results-memo template](RESULTS-MEMO.md) and retain:

- Your implementation and any changed fixtures, with the reason for each change.
- Setup instructions, dependency/interpreter record and exact commands.
- One normal run, relevant failure runs and the actual test output.
- A short explanation of a design choice, a diagnosed mistake and a remaining limit.
- A small changed-example demonstration completed independently after assisted practice.

For each dimension, record **demonstrated**, **needs one repair**, or **not yet attempted**, with evidence. There is no universal numeric passing score.

- **Reasoning:** explain the contract, assumptions and why the chosen cases matter.
- **Correctness:** reproduce the stated normal and boundary behaviors, including your added case.
- **Error handling:** fail clearly without a misleading success or silent corrupted total.
- **Reproducibility:** another person can run the local fixtures with the stated environment.
- **Explanation:** separate supplied fixture output, reference output and your own implementation; state what was independently demonstrated.

If one dimension needs repair, do that project's named recovery task and repeat a changed example. AI can explain an error or suggest cases during practice; identify assistance in the memo. Close assistance and reference tabs for the final explanation/debug/change exercise. Follow any stricter course assessment policy for course-owned exercises.

## Fixture rights and limits

All bundled weather and shop data were created for this repository and contain no real observations or personal records. They are covered by the repository [license](../../LICENSE.md). Their expected totals are arithmetic checks, not evidence about real customers, forecast accuracy or production performance. Optional live Open-Meteo data has separate [terms and attribution requirements](https://open-meteo.com/en/terms).

[Choose the calculator task](calculator/README.md#stages) · [Weather stages](weather/README.md#stages) · [SQL stages](sql/README.md#stages)
