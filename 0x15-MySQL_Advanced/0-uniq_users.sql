-- create a table users
-- create a table
CREATE TABLE IF NOT EXISTS users (id INT NOT NULL DEFAULT 1 UNIQUE, email VARCHAR(255) NOT NULL UNIQUE, name VARCHAR(255), PRIMARY KEY(id));
