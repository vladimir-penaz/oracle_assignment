CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    mail VARCHAR(255) UNIQUE NOT NULL
);

INSERT INTO customers (customer_id, name, mail) VALUES
('100001', 'Alice Johnson', 'alice@example.com'),
('100002', 'Bob Smith', 'bob@example.com'),
('100003', 'Charlie Davis', 'charlie@example.com'),
('100004', 'John Doe', 'johndoe@example.com');