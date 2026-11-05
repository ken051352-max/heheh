-- This starting query runs before you change anything.
-- Week 15: filter orders for A; predict their count and total before running.
-- Week 16: LEFT JOIN customers to orders and group by customer ID to report
-- counts/totals, including C with zero. Keep ONE statement in this file.
-- Save earlier queries in private notes. Ingestion belongs to later M8a work.
SELECT order_id, customer_id, amount_cents
FROM orders
ORDER BY order_id;
