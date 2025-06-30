---Part 1
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);


CREATE TABLE customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id INT UNIQUE REFERENCES customer(id)
);

INSERT INTO customer (first_name, last_name) VALUES 
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');


INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES (
    TRUE,
    (SELECT id FROM customer WHERE first_name = 'John' AND last_name = 'Doe')
);


INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES (
    FALSE,
    (SELECT id FROM customer WHERE first_name = 'Jerome' AND last_name = 'Lalu')
);

SELECT c.first_name
FROM customer c
JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = TRUE;

SELECT c.first_name, cp.isLoggedIn
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id;

SELECT COUNT(*) AS not_logged_in_customers
FROM customer c
LEFT JOIN customer_profile cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = FALSE OR cp.isLoggedIn IS NULL;

---Part 2
CREATE TABLE Book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);

INSERT INTO Book (title, author) VALUES 
('Alice In Wonderland', 'Lewis Carroll'),
('Harry Potter', 'J.K Rowling'),
('To kill a mockingbird', 'Harper Lee');

CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
);

INSERT INTO Student (name, age) VALUES
('John', 12),
('Lera', 11),
('Patrick', 10),
('Bob', 14);

CREATE TABLE Library (
    book_fk_id INT REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INT REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id)
);


INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'John'),
    '2022-02-15'
);


INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'To kill a mockingbird'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-03-03'
);


INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM Student WHERE name = 'Lera'),
    '2021-05-23'
);


INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
VALUES (
    (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM Student WHERE name = 'Bob'),
    '2021-08-12'
);

SELECT * FROM Library;

SELECT s.name AS student_name, b.title AS book_title, l.borrowed_date
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id;

SELECT AVG(s.age) AS average_age
FROM Library l
JOIN Student s ON l.student_fk_id = s.student_id
JOIN Book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

DELETE FROM Student WHERE name = 'Bob';

SELECT * FROM Library;







