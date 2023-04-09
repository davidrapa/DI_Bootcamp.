CREATE DATABASE fake_data_generator;

USE fake_data_generator;

CREATE TABLE fake_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_type VARCHAR(255) NOT NULL,
    fake_data VARCHAR(255) NOT NULL
);
