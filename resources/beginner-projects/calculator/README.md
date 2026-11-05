[Project kit and setup](../README.md#setup) · [M1 starter milestone](../../../curriculum/1-foundations.md#m1-starter-project)

<a id="start"></a>
# Calculator: your first original program

**User:** someone who wants one calculation and a clear explanation when input is unusable. **Prerequisites:** functions, variables, conditionals, loops and exceptions from CS50P Lectures 0–3 or equivalent. No maths placement score is required.

**First task:** open [`starter.py`](starter.py), find `calculate`, and make addition work for `2 + 3`. Keep the supplied command-line shell. This is your original roadmap exercise, not a CS50P problem-set solution.

The scoped program accepts two finite decimal numbers and one of `+`, `-`, `*`, `/`. It returns a finite numeric result or raises `ValueError`; the CLI prints a useful message to stderr and returns a nonzero exit status on invalid input. Do not evaluate arbitrary Python expressions. Money, arbitrary-precision arithmetic, a GUI and scientific functions are outside this brief.

**Lecture default:** [CS50P Lecture 3: Exceptions](https://cs50.harvard.edu/python/weeks/3/). Revisit only the relevant section. Use the semester plan for scheduled book reading; no purchase is required to begin.

<a id="stages"></a>
## Build in three stages

1. **Small working version:** convert two inputs and implement addition. Predict the output before running it, then change one operand to a negative decimal. Save the normal transcript.
2. **Assessed starter:** implement the other operations; handle a typo, unsupported operator and zero divisor. Save a bad-input transcript and explain the difference between a return value and printing.
3. **After Lecture 5:** read [the behavioral tests](../tests/test_calculator.py), run the calculator suite, then add a case of your own. The test contract also rejects `NaN`, infinity and a result outside the finite float range. Learn `math.isfinite` from the [Python math reference](https://docs.python.org/3.12/library/math.html#math.isfinite) when you reach that test; it is not an unexplained Week 4 prerequisite.

From the repository root, using the [isolated interpreter](../README.md#setup):

```text
python resources/beginner-projects/calculator/starter.py 2 + 3
python resources/beginner-projects/calculator/starter.py 7 / 0
python resources/beginner-projects/calculator/starter.py 2 "*" 4
python -m pytest resources/beginner-projects/tests/test_calculator.py -q
```

Quote `*` so shells do not expand it as filenames. Before implementation, the TODO exception is expected. In an implemented starter, the second command should fail usefully; the failure exit is correct behavior. The automated suite can wait until testing is taught.

<a id="assessment"></a>
## Demonstrate and explain

- **Recall:** explain why the CLI's string `"2"` and number `2` need different handling.
- **Read:** predict `calculate("7", "/", "2")` and explain why integer truncation would be wrong here.
- **Debug:** investigate why checking `if right == 0` before converting a string misses a zero divisor.
- **Change:** add one normal and one invalid case not shown above, then explain the result without opening a reference.

Apply the [shared rubric and submission checklist](../README.md#one-shared-submission-and-assessment-pattern) and the [loops/errors readiness check](../../../guides/readiness-checks.md#loops-and-errors). At the Week 4 milestone, a normal run, bad-input run and explanation are sufficient evidence of the starter; do not claim full M1 completion. Later, retain automated evidence as well.

**If stuck:** reduce the program to a function converting one string to a float, try `"3.5"` and `"oops"`, and catch the conversion exception. Then put the operation back. If the zero case fails, trace the types before and after conversion. Recheck with `"-0.0"` instead of memorizing `"0"`.

**Next:** study [CS50P Lecture 4: Libraries](https://cs50.harvard.edu/python/weeks/4/), then [Lecture 5: Unit Tests](https://cs50.harvard.edu/python/weeks/5/). Start the [Weather project](../weather/README.md#start) after testing and files; return to the [tracker](../../../guides/progress-tracker.md#resume) with one exact next task.

<details>
<summary>Reviewer material: open after a serious attempt</summary>

The [worked reference](reference.py) and [reviewer notes](../REVIEWER.md#calculator) show one implementation, not the only acceptable design. After consulting them, close the file and solve a changed case yourself.

</details>
