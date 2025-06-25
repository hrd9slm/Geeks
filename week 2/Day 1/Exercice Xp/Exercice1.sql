create database public

create table items (
  items_id SERIAL PRIMARY KEY,
  nom VARCHAR(30),
  prix  NUMERIC(10, 2)
 
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

INSERT INTO items (nom ,prix) VALUES 
('Small Desk', 100),
('Large Desk', 300),
('Fan', 80);

INSERT INTO customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson');

select * from items

select * from items where prix > 80

select * from items where prix <=300

select * from customers  where last_name = 'Smith'

select * from customers  where last_name = 'Jones'

select * from customers  where first_name <> 'Scott'


