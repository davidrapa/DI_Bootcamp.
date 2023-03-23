-- -- Create the 'items' table
-- CREATE TABLE items (
--   id INT PRIMARY KEY,
--   name VARCHAR(50) NOT NULL,
--   price DECIMAL(10, 2) NOT NULL
-- );

-- -- Create the 'customers' table
-- CREATE TABLE customers (
--   id INT PRIMARY KEY,
--   first_name VARCHAR(50) NOT NULL,
--   last_name VARCHAR(50) NOT NULL
-- );

-- -- Add the given items to the 'items' table
-- INSERT INTO items (id, name, price)
-- VALUES
--   (1, 'Small Desk', 100),
--   (2, 'Large Desk', 300),
--   (3, 'Fan', 80);

-- -- Add the given customers to the 'customers' table
-- INSERT INTO customers (id, first_name, last_name)
-- VALUES
--   (1, 'Greg', 'Jones'),
--   (2, 'Sandra', 'Jones'),
--   (3, 'Scott', 'Scott'),
--   (4, 'Trevor', 'Green'),
--   (5, 'Melanie', 'Johnson');

-- -- Fetch all items
-- SELECT * FROM items;

-- -- Fetch all items with a price above 80 (80 not included)
-- SELECT * FROM items WHERE price > 80;

-- -- Fetch all items with a price below 300 (300 included)
-- SELECT * FROM items WHERE price <= 300;

-- --no customers with the last name 'Smith'
-- SELECT * FROM customers WHERE last_name = 'Smith';

-- -- Fetch all customers whose last name is 'Jones'
-- SELECT * FROM customers WHERE last_name = 'Jones';

-- -- Fetch all customers whose firstname is not 'Scott'
-- SELECT * FROM customers WHERE first_name <> 'Scott';