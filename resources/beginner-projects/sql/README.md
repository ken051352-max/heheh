[Project kit and setup](../README.md#setup) · [M8a SQL](../../../curriculum/2-statistics-and-data.md#module-8a) · [Previous: Weather CLI](../weather/README.md)

<a id="start"></a>
# First SQL/data investigation: reconcile a campus shop

**User:** a fictional campus shop coordinator who needs to know each customer's ordered, paid and outstanding amounts. **Prerequisite:** demonstrated M1 competence or equivalent evidence; then study the selected SQL lessons. This small investigation begins M8a. It does not certify full M8a warehouses/query tuning, M7 analysis or M8b distributed data.

**First-semester task:** use the [query preview](#query-preview) below. It runs before implementing ingestion. The full staged investigation follows when you study M8a's design and writing lessons.

<a id="query-preview"></a>
## Weeks 15–16: queries before ingestion

Read the customer/order keys in the [schema](schema.sql), then run the supplied workspace from the repository root:

```text
python resources/beginner-projects/sql/preview.py
```

It prints three clean synthetic orders. Edit [`preview.sql`](preview.sql), keeping one query at a time. Week 15: filter customer A's orders, predict their count/total and compare with output. Week 16: join customers to orders and report order counts/totals for **every customer**, including C with no orders. Use `COUNT(order_id)` rather than counting the outer row, and explain your handling of absent totals. Save your query, a hand calculation, output and a short memo. Add another query or changed condition you can explain independently.

The [workspace](preview.py) loads a documented, curated clean subset of the fixtures into memory. This is supplied setup, not evidence you implemented data cleaning. SQLite's query-only setting prevents accidental writes; this local learning aid is not a security sandbox for hostile SQL. No database or network service is needed.

**Preview completion:** explain keys, reproduce the filtered result, preserve C in the join and reconcile the 2,500-cent order total without duplicate counting. The [SQL readiness check](../../../guides/readiness-checks.md#sql-ready) supplies a different example. Observe supplied constraints when useful; implementing ingestion, payment reconciliation, transactions and index work below can wait until M8a. Record this as **query/join preview complete, M8a partial**.

**Free lecture default:** [CS50 SQL Lecture 0: Querying](https://cs50.harvard.edu/sql/weeks/0/), followed by [Lecture 1: Relating](https://cs50.harvard.edu/sql/weeks/1/). Use [Lecture 2: Designing](https://cs50.harvard.edu/sql/weeks/2/) for the schema and [Lecture 3: Writing](https://cs50.harvard.edu/sql/weeks/3/) for constraints/inserts. These are successive lessons for this project, not four simultaneous courses. No PostgreSQL installation is needed yet.

## Data contract and question

All records are **synthetic** and money is expressed in integer cents of a teaching currency. No customer is a real person.

- [`customers.csv`](fixtures/customers.csv): one row per customer; `customer_id` is the key. Customer C has no orders.
- [`orders.csv`](fixtures/orders.csv): one row per immutable order; `order_id` is the key, `customer_id` references customers. The raw file deliberately contains an identical duplicate, a missing amount, an unknown customer and a negative amount.
- [`payments.csv`](fixtures/payments.csv): one row per payment; `payment_id` is the key, `order_id` references orders. One order has two partial payments. Several legitimate amounts may be equal; distinct amounts are not a substitute for distinct entities.

Accept only whole nonnegative cents within SQLite's signed 64-bit integer range. Reject malformed rows with a line number/reason, count identical duplicates once, and reject a conflicting repeat of an order ID by rolling back its whole batch. A replay must not change accepted totals. Parameterize values rather than building SQL strings from them.

Return one row per customer, sorted by ID: `(customer_id, ordered_cents, paid_cents, outstanding_cents)`. Include no-order customers with zeros. Reconcile the report with independent sums of accepted orders and payments. Explain why directly summing order amounts after a one-to-many payment join can overstate revenue.

<a id="stages"></a>
## Expanded M8a investigation: build in four stages

After the query preview and the design/writing lectures, open [`starter.py`](starter.py) and implement `ingest_orders` and `report`. These outcomes extend the semester preview; they are not an extra requirement in its two introductory weeks.

1. **Understand the grain.** Manually compute expected totals for one customer, including split payments. Write down keys, required fields and which raw rows cannot be accepted. Run simple `SELECT` queries using the supplied connection; explain why foreign-key enforcement is enabled before inserting data.
2. **Load with evidence.** Implement `ingest_orders`. Begin with valid records; then add quarantines, duplicate detection and transaction rollback. Read [the ingestion tests](../tests/test_sql.py) one behavior at a time.
3. **Join and reconcile.** Implement `report`. Pre-aggregate at the appropriate grain or use an equivalent correct design. Test a no-order customer, split payments and two distinct orders with the same amount. Add one changed case, such as a zero-value order, and explain its intended treatment.
4. **Inspect a plan and report findings.** The supplied demo records plans before and after an index on `orders(customer_id)`. Explain scan versus search using your installed SQLite's output. Save the report, row decisions and [results memo](../RESULTS-MEMO.md). Tiny fixtures do not demonstrate a performance improvement; do not invent a speedup.

From the repository root:

```text
python resources/beginner-projects/sql/starter.py
python -m pytest resources/beginner-projects/tests/test_sql.py -q
```

The program creates an in-memory database and prints JSON; it writes no persistent database or results file. Save output in your own private artifact. Initial TODO failures are expected.

**Dialect boundary:** this lab uses SQLite `EXPLAIN QUERY PLAN`, which describes a chosen strategy. It is **not PostgreSQL `EXPLAIN ANALYZE`** and reports no measured execution time. Its output format can change across SQLite releases, so tests verify data contracts rather than exact plan prose. For full M8a, continue to the module's PostgreSQL migrations, validation, before/after execution plans and anomalies memo.

<a id="assessment"></a>
## Demonstrate and explain

- **Recall:** state the grain and primary/foreign key of each table.
- **Read:** explain what a left join preserves that an inner join would omit for customer C.
- **Debug:** an order for 1,000 cents has two payments, 200 and 300 cents. A joined query reports 2,000 cents ordered. Identify the cardinality error and correct the query; do not use `SUM(DISTINCT amount)` as a general fix.
- **Change:** create two different orders with equal amounts. Prove both remain in the total and explain what happens if a conflicting duplicate appears after a valid insert in the same batch.

Apply the [shared rubric](../README.md#one-shared-submission-and-assessment-pattern) and [SQL readiness check](../../../guides/readiness-checks.md#sql-ready). Submit the schema/key sketch, your implementation, rejection/replay evidence, reconciled totals, plans and memo. A decorated chart cannot replace reconciliation.

**Recovery:** draw one order joined to two payment rows, write each repeated value, then sum at each grain separately. If ingestion is confusing, test one valid row, one duplicate and one rejected row before returning to the complete fixture. If totals differ, inspect row counts after every join rather than changing the expected total.

**Next:** record this as **partial M8a** in the [tracker](../../../guides/progress-tracker.md#full-tracker), then use the [semester review](../../../guides/first-semester.md#semester-exit) to choose the next task. Continue the [full SQL module](../../../curriculum/2-statistics-and-data.md#module-8a) when scheduled; M4 is useful for index internals, not a gate to this investigation.

<details>
<summary>Reviewer material and implementation references</summary>

The [worked solution](reference.py) and [reviewer notes](../REVIEWER.md#sql) expose answers; attempt the task first. Technical references: [Python 3.12 sqlite3](https://docs.python.org/3.12/library/sqlite3.html), [SQLite foreign keys](https://www.sqlite.org/foreignkeys.html) and [query plans](https://www.sqlite.org/eqp.html). Python 3.12's `autocommit=True` permits the lab's explicit `BEGIN`/`COMMIT`/`ROLLBACK`; connection `commit()` is not used to end those explicit SQL transactions.

</details>
