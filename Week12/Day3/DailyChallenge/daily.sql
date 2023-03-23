-- Count the number of actors in the table
SELECT COUNT(*) FROM actors;

-- new actor with some blank fieldss
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('', 'Smith', NULL, 0);

--If the actors table has been set up with the STRICT_TRANS_TABLES SQL mode enabled, then the query will fail and return an error message indicating that the first_name field cannot be empty.