CREATE DATABASE customer_migration;

USE customer_migration;

CREATE TABLE customers (
    customer_id INT,
    name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(15)
);
