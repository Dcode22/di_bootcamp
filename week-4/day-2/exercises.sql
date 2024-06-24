-- exercise 1
select * from items order by price;

select * from items where price >= 80 order by price desc;
SELECT firstname, lastname FROM Customers order by firstname limit 3;
select lastname from customers order by lastname desc;

-- exercise 2
select * from customer;
select first_name || ' ' || last_name as full_name from customer;
select distinct create_date from customer;
select * from customer order by first_name desc;
select film_id, title, description, release_year, rental_rate from film order by rental_rate;
select address, phone from address where district = 'Texas';
select * from film where film_id = 15 or film_id = 150;
select film_id, title, description, length, rental_rate from film where title = 'Harry Potter';
select film_id, title, description, length, rental_rate from film where title like 'Ha%';
select film_id, title, description, length, rental_rate from film order by rental_rate limit 10;
select film_id, title, description, length, rental_rate from film order by rental_rate limit 10 offset 10;
select customer.first_name, customer.last_name, payment.amount, payment.payment_date from customer join payment on customer.customer_id = payment.customer_id; 
select f1.* from film f1 where not exists(select 1 from inventory i1 where i1.film_id = f1.film_id)
select city.city, country.country from city join country on city.country_id = country.country_id

