SELECT * FROM language;

SELECT f.title, f.description, l.name AS language_name
FROM film f
JOIN language l ON f.language_id = l.language_id;

SELECT film.title, film.description, language.name
FROM language
LEFT JOIN film ON film.language_id = language.language_id;

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO new_film (name) VALUES
('Al bortikala almora'),
('Switchers');

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(255),
    score INT CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


SELECT id FROM new_film;
SELECT language_id, name FROM language;

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'Chef-d''œuvre sombre', 9, 'Un film captivant et poétique.'),
(2, 2, 'Merveille cinématographique', 10, 'Une aventure visuelle incroyable.');

DELETE FROM new_film WHERE id = 1;

SELECT * FROM customer_review;

UPDATE film SET language_id = 2 WHERE title IN ('Academy Dinosaur', 'African Egg');

SELECT title, language_id FROM film WHERE title IN ('Academy Dinosaur', 'African Egg');
 
INSERT INTO customer (store_id, first_name, last_name, email, address_id, active)
VALUES (1, 'Salma', 'salma', 'salma.salma@example.com', 5, true);


DROP TABLE customer_review;

SELECT COUNT(*) FROM rental WHERE return_date IS NULL;

SELECT f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE r.return_date IS NULL
ORDER BY f.replacement_cost DESC
LIMIT 30;

SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'Penelope' AND a.last_name = 'Monroe'
AND (f.description ILIKE '%sumo%' OR f.title ILIKE '%sumo%');

SELECT title
FROM film
WHERE length < 60 AND rating = 'R'
AND description ILIKE '%documentary%';

SELECT DISTINCT f.title
FROM payment p
JOIN rental r ON p.rental_id = r.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND p.amount > 4
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';


SELECT DISTINCT f.title, f.replacement_cost
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN customer c ON r.customer_id = c.customer_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC;
