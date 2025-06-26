/*
---- Exercice 1
select * from items order by price asc

select * from items where price >= 80 order by price desc

select * from customers order by first_name  asc limit 3

select last_name from customers order by last_name desc
*/
---- Exercice 2
/*
select * from customer

select (first_name,last_name )as full_name from customer

select Distinct create_date from customer

select * from customer order by first_name desc

select film_id,title,description,release_year,rental_rate from film order by rental_rate 

select address,phone,district from address where district ='Texas'

select * from film where film_id in (15,150)

select film_id, title, description, length,rental_rate from film where title='matrix'

select film_id, title, description, length,rental_rate from film where title ~*'^ma'

select title ,replacement_cost from film order by replacement_cost limit 10

select title ,replacement_cost from film order by replacement_cost OFFSET 10 ROWS FETCH FIRST 10 ROWS ONLY

SELECT  c.customer_id,c.first_name , c.last_name,p.amount,p.payment_date from customer as c join payment as p on c.customer_id= p.customer_id  order by c.customer_id 

SELECT *  FROM film f left JOIN inventory i ON f.film_id = i.film_id
WHERE i.film_id IS NULL;

select cn.country,ct.city from country cn  join city ct on cn.country_id=ct.country_id order by cn.country
*/

SELECT c.customer_id,c.first_name || ' ' || c.last_name as names ,p.amount, p.payment_date,p.staff_id FROM payment p  JOIN customer c ON p.customer_id = c.customer_id ORDER BY p.staff_id, c.customer_id






