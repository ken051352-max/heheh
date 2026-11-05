[Project kit](README.md#reviewer-guide)

# Worked-example and assessment notes

These notes contain answers. Learners should attempt the named task first. A reviewer can use a classmate, a mentor or their own delayed check; external review is helpful, not a required public event.

The shared rubric concerns observable capability. Do not pass someone solely because they executed the reference, or fail them for using a different correct design. Ask for a changed example after closing reference/AI tabs. During practice, hints should narrow the next action rather than complete the exercise.

<a id="calculator"></a>
## Calculator

- `"2"` is input text; conversion determines numeric arithmetic. `7 / 2` should yield 3.5 under this contract.
- Comparing the raw right operand with integer zero misses a string such as `"0"`. Convert, then check; `-0.0` is also a zero divisor.
- A bare `except Exception` can hide a programming bug. Catch the expected conversion/domain errors and preserve a meaningful nonzero CLI failure.
- `float` can represent `NaN` and infinity. Finite inputs can also overflow to an infinite multiplication result. `math.isfinite` checks the intended finite-number contract; this is not decimal financial arithmetic.
- Normal example: `2 + 3` → 5. A useful independent change: negative decimal division, unsupported `**`, or a different overflow case. A learner's added test should have a reason beyond copying the existing input.

The supplied [reference](calculator/reference.py) prints `5.0`; equivalent formatting is fine. Tests assert numeric behavior and separate success/error streams, not exact error prose.

<a id="weather"></a>
## Weather

- Cache age 9 with TTL 10 is valid; age 10 expires, and age -1 is future-dated and invalid. Receipt time is not the provider observation time.
- A cache for Delhi must not answer a London request. This one-entry cache may evict a previous city's record; that is a documented simplification.
- JSON Booleans become Python `bool`, a subclass of `int`; the schema deliberately requires `type(value)` to be numeric without accepting Boolean temperatures. Other explicit schema validators are also valid.
- Malformed data must be rejected before replacement. Missing/corrupt cache entries trigger a fresh attempt; a failed fresh request must not be relabeled as successful current data.
- Network mocks validate request/error/cache behavior, not actual provider uptime or scientific accuracy. Offline output is always labeled synthetic, even if the user supplies a different fixture file.
- The permission-failure test injects `PermissionError` because filesystem permissions behave differently under Windows/admin environments. The reference writes a temporary sibling and replaces atomically within that filesystem; no multi-process coordination is claimed.

Review the [reference](weather/reference.py) after the learner has explained its boundaries. Useful extensions include another city or a strict timestamp rule with tests; async fetching, geocoding, Pydantic and retry frameworks are not required to demonstrate this brief.

<a id="sql"></a>
## SQL/data

For the first-semester [query preview](sql/README.md#query-preview), assess filtering, counts, a customer/order left join and 2,500 cents of order totals. Customer C must remain with zero orders. The supplied clean loader is scaffolding. Payment reconciliation, ingestion, rollback and plan analysis below belong to the expanded investigation after its design/writing lessons.

The expected fixture load is three accepted orders, one identical duplicate and three rejected rows: missing amount, unknown customer and negative amount. The report is:

```text
customer  ordered  paid  outstanding  (integer cents)
A         2000     1800  200
B          500      500    0
C            0        0    0
```

Independent accepted-order total = 2,500 cents; payment total = 2,300 cents; outstanding = 200 cents. These are synthetic fixture answers, not business findings.

- An order joined to two payments appears twice. Summing its amount after that join doubles it. Aggregate the order totals and payment totals separately at customer grain, or use an equivalent correct relational design.
- `SUM(DISTINCT amount)` removes legitimately equal amounts from distinct orders. Tests include two equal-valued orders to expose that attempted fix.
- Left joining to the customer dimension preserves C. `COALESCE` maps the absent sums to zero under this scoped report definition; it must not conceal unknown or malformed raw values.
- An identical immutable ID replay does not add revenue. A conflicting repeat must roll back even the earlier valid insert in its batch; a test also checks that the connection remains usable afterward.
- SQLite foreign keys are enabled per connection outside a transaction. The schema also uses `NOT NULL` and integer/nonnegative checks; declared types alone do not enforce the full SQLite contract.
- Query plans are strategy evidence, not timing evidence. The fixture is too small for a performance conclusion. If a release chooses an unexpected plan, investigate it rather than hardcoding a plan-text assertion.

The [reference](sql/reference.py) uses separate grouped subqueries. A different design is acceptable if it passes behavioral cases and the learner can explain grain, reconciliation and the effect of changed data. Full M8a still requires the module's larger PostgreSQL and warehouse outcomes.
