[Project kit and setup](../README.md#setup) · [M1 capstone](../../../curriculum/1-foundations.md#m1-capstone) · [Previous: calculator](../calculator/README.md)

<a id="start"></a>
# Weather CLI: reliable input, files and failures

**User:** someone who wants a temperature for a supported city and needs to know whether it is a fixture, cached response or fresh provider response. **Prerequisites:** the starter, libraries, testing and file I/O (CS50P Lectures 0–6 or equivalent). This project contributes to full M1; finish its other core outcomes too.

**First task:** inspect [`fixtures/current.json`](fixtures/current.json) and sketch the path from raw bytes to the numeric temperature. Then implement `parse_weather` in [`starter.py`](starter.py). The supplied adapter and CLI are scaffolding; four functions intentionally remain unfinished.

**Free lecture default:** [CS50P Lecture 6: File I/O](https://cs50.harvard.edu/python/weeks/6/); revisit [Lecture 5](https://cs50.harvard.edu/python/weeks/5/) for tests. You need no API key, purchase, cloud or live request for assessment.

## Bounded contract

- The local gazetteer accepts **Delhi** and **London**, ignoring case and surrounding spaces. Unknown cities fail usefully. Arbitrary geocoding is later scope.
- Accept a UTF-8 JSON current temperature only when it is a finite number (not a Boolean/string), has Celsius units and a parseable ISO timestamp. The request selects UTC: accept its offset-free UTC representation or an explicit zero offset, and reject a different offset. A malformed body, missing value or wrong unit fails explicitly.
- **Offline is the default.** It reads a synthetic fixture, labels it and never fetches or writes a cache. The fixture's January timestamp and temperature are not today's weather for either city.
- **Live is optional and explicit.** Request one Open-Meteo response with a five-second socket timeout, UTC time and Celsius units. The adapter has a 64 KiB response limit and no retries. A socket timeout is not a guaranteed total wall-clock deadline.
- The single-entry disk cache stores city, receipt time and raw payload. Reuse only the same city's valid payload with age in `[0, TTL)`. Default TTL is 900 seconds; exactly at expiry is a miss. Missing, corrupted or future-dated entries are misses. Do not silently serve expired data as current.
- Cache writes replace a whole entry. An unwritable directory produces a useful error and preserves the previous file. This teaching cache has no concurrency coordination; it is not a multi-user production cache.
- Functions raise `WeatherError` for anticipated data/service/cache failures. The CLI returns zero on success and nonzero on failure, using stderr for errors. Do not put exception traces containing request secrets in user messages.

<a id="stages"></a>
## Build in four stages

1. **Parse offline data.** Implement `parse_weather`. Try the valid, [missing-temperature](fixtures/missing-temperature.json) and [malformed](fixtures/malformed.json) files. The malformed file is intentionally invalid JSON. Start with the parsing tests (`-k "temperature or payloads or units"`).
2. **Assemble one offline run.** Implement the offline portion of `get_weather`, city validation and the returned source label. Run the CLI with `--offline`; use a mock that fails if a network call occurs.
3. **Add fresh-data and caching behavior.** Implement `read_cache`, `write_cache` and the remaining `get_weather` path. Use the injected `fetch` callable and clock value in tests; no live service is needed. The `download` adapter and CLI are supplied. Explain their resource handling.
4. **Assess and communicate.** Run all [Weather tests](../tests/test_weather.py); add one changed case. Write the [results memo](../RESULTS-MEMO.md), including what cache expiry means and what the tests do not establish. Optional provider verification comes only after this works.

From the repository root:

```text
python resources/beginner-projects/weather/starter.py Delhi --offline
python resources/beginner-projects/weather/starter.py Atlantis --offline
python resources/beginner-projects/weather/starter.py Delhi --offline --fixture resources/beginner-projects/weather/fixtures/malformed.json
python -m pytest resources/beginner-projects/tests/test_weather.py -q
```

The first run should eventually print a JSON object marked `"source": "synthetic fixture"`; the other two must fail usefully. Before implementing the TODOs, failures are expected. The supplied test suite injects network errors and permission failures so it behaves consistently across operating systems.

<a id="assessment"></a>
## Demonstrate and explain

- **Recall:** distinguish the observation timestamp, cache receipt time and current clock.
- **Read:** for receipt time 100 and TTL 10, decide whether times 109, 110 and 99 permit reuse.
- **Debug:** explain why `bool` passing an `isinstance(value, int)` test is inappropriate for this temperature contract; why should a malformed response never replace a valid cache?
- **Change:** introduce a cache for the wrong city and an API timeout. Predict which branch runs and show that stale/wrong-city data is not reported as a successful fresh fetch.

Use the [shared rubric](../README.md#one-shared-submission-and-assessment-pattern). Submit your code, normal and failure transcripts, mocked test output, environment record and memo. Tests do not establish real-service availability, temperature accuracy, resistance to arbitrary attacks or a production latency guarantee.

**Recovery:** if parsing fails, inspect one key/value and its type before building a dictionary. If caching fails, write a three-row truth table for age 9, 10 and -1 before editing code. If a mock is confusing, write a function accepting another function and call it once; then return to `fetch`. Repeat with a new TTL and explain the boundary.

**Next:** check the [full M1 outcomes](../../../curriculum/1-foundations.md#module-1) and [M1 exit readiness](../../../guides/readiness-checks.md#m1-ready). After demonstrating them, use the [semester transition](../../../guides/first-semester.md#week-15); the [SQL investigation](../sql/README.md#start) is an available M8a introduction. You do not need async clients, agents or cloud deployment to complete this CLI.

<details>
<summary>Optional live adapter check</summary>

Inspect the [Open-Meteo API documentation](https://open-meteo.com/en/docs) and [current terms](https://open-meteo.com/en/terms) before enabling live mode. The free endpoint's access, permitted use and quotas can change. Attribute any real provider data separately from the bundled synthetic fixture.

```text
python resources/beginner-projects/weather/starter.py Delhi --live --cache weather-cache.json
```

This writes a cache in the current directory. Use a writable disposable location and keep this runtime file out of the submission. Record the date and actual source field: a second call may use the cache. If access fails, record it; the offline assessment remains usable. Consult [urllib requests](https://docs.python.org/3.12/library/urllib.request.html) for adapter behavior.

</details>

<details>
<summary>Reviewer material: open after an attempt</summary>

Read the [worked reference](reference.py) and [reviewer notes](../REVIEWER.md#weather). Running this reference verifies a supplied example, not independent competence.

</details>
