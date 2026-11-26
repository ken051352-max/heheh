-- Synthetic second shop. Each amount is in cents. IDs identify customers.
INSERT INTO customers (customer_id, name) VALUES
    ('1', 'Asha'), ('2', 'Ravi'), ('3', 'Noor'), ('4', 'Ravi');
INSERT INTO orders (order_id, customer_id, amount_cents) VALUES
    ('10', '1', 500), ('11', '1', 700), ('12', '2', 300), ('13', '2', 300);
