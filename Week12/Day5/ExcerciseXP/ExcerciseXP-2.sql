-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- SELECT * FROM customer;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- SELECT DISTINCT create_date FROM customer;
-- -- -- -- -- -- -- -- -- -- -- -- -- SELECT * FROM customer ORDER BY first_name DESC;

-- -- -- -- -- -- -- -- -- -- -- -- SELECT film_id, title, description, release_year, rental_rate
-- -- -- -- -- -- -- -- -- -- -- -- FROM film
-- -- -- -- -- -- -- -- -- -- -- -- ORDER BY rental_rate ASC;

-- -- -- -- -- -- -- -- -- -- -- SELECT address, phone FROM address WHERE district = 'Texas';

-- -- -- -- -- -- -- -- -- -- Retrieve all movie details where the movie id is either 15 or 150:
-- -- -- -- -- -- -- -- -- -- SELECT * FROM film WHERE film_id IN (15, 150);


-- -- -- -- -- -- -- -- --  favorite movie exists in the database and get the film ID, title, description, length and the rental rate:
-- -- -- -- -- -- -- -- SELECT film_id, title, description, length, rental_rate
-- -- -- -- -- -- -- -- FROM film
-- -- -- -- -- -- -- -- WHERE title = 'Rambo';

-- -- -- -- -- -- -- film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie:
-- -- -- -- -- -- SELECT film_id, title, description, length, rental_rate
-- -- -- -- -- -- FROM film
-- -- -- -- -- -- WHERE title LIKE 'Rambo%';

-- -- -- -- --  10 cheapest movies:
-- -- -- -- --  SELECT film_id, title, rental_rate
-- -- -- -- -- FROM film
-- -- -- -- -- ORDER BY rental_rate ASC
-- -- -- -- -- LIMIT 10;

-- -- -- -- Join the customer and payment tables to get the first name and last name from the customer table, as well as the amount and the date of every payment made by a customer, ordered by their id 
-- -- -- SELECT c.first_name, c.last_name, p.amount, p.payment_date
-- -- -- FROM customer c
-- -- -- JOIN payment p ON c.customer_id = p.customer_id
-- -- -- ORDER BY c.customer_id ASC;

-- -- all the movies which are not in inventory:
-- SELECT f.film_id, f.title
-- FROM film f
-- LEFT JOIN inventory i ON f.film_id = i.film_id
-- WHERE i.film_id IS NULL;

-- which city is in which country
-- SELECT ci.city_id, ci.city, co.country
-- FROM city ci
-- JOIN country co ON ci.country_id = co.country_id;

