-- Creates the table force_name with a NOT NULL constraint on name

-- Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

