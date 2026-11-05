-- SQLite teaching schema: amount_cents is integer money, not a floating total.
-- Foreign-key enforcement is enabled by connect(), outside any transaction.
CREATE TABLE customers (
    customer_id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL
);
CREATE TABLE orders (
    order_id TEXT PRIMARY KEY NOT NULL,
    customer_id TEXT NOT NULL REFERENCES customers(customer_id),
    amount_cents INTEGER NOT NULL CHECK (typeof(amount_cents) = 'integer' AND amount_cents >= 0)
);
CREATE TABLE payments (
    payment_id TEXT PRIMARY KEY NOT NULL,
    order_id TEXT NOT NULL REFERENCES orders(order_id),
    amount_cents INTEGER NOT NULL CHECK (typeof(amount_cents) = 'integer' AND amount_cents >= 0)
);
