
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    product VARCHAR(100) NOT NULL
);

INSERT INTO users (name)
VALUES ('Daksh'), ('Rahul'), ('Aman');

INSERT INTO products (name)
VALUES ('Laptop'), ('Phone'), ('Keyboard');

INSERT INTO orders (product)
VALUES ('Laptop'), ('Phone');
