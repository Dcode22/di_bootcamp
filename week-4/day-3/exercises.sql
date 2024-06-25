select * from language;
select f1.title, f1.description, l1.name from film as f1 join language as l1 on f1.language_id = l1.language_id;
select f1.title, f1.description, l1.name from film as f1 right join language as l1 on f1.language_id = l1.language_id;
-- exercise 1
create table new_film(
	film_id serial primary key,
	name text
)
create table customer_review (
	review_id serial primary key,
	film_id int,
	foreign key(film_id) references new_film(film_id) on delete cascade,
	language_id int,
	foreign key(language_id) references language(language_id),
	title text,
	score int check(score > 0 and score < 11),
	review_text text,
	last_update date
)

insert into customer_review (film_id, language_id, title, score, review_text) 
	values (1, 1, 'This sucks', 2, 'I hate this perfect world'), (1, 1, 'wow', 9, 'amazing world')

delete from new_film where film_id = 1;

-- exercise 2
update film set language_id = 2 where language_id = 1;

insert into customer (store_id, first_name, last_name, address_id, email) values (1, 'John', 'Smith', 3, 'john@example.com');

drop table customer_review;

select count(*) from rental where return_date is null;

select * from film join inventory on inventory.film_id = film.film_id join rental on rental.inventory_id = inventory.inventory_id where rental.return_date is null order by film.rental_rate desc limit 30;

select * from film join film_actor on film_actor.film_id = film.film_id join actor on actor.actor_id = film_actor.actor_id where film.description like '%Sumo%' and  actor.first_name = 'Penelope' and actor.last_name = 'Monroe';

select * from film where film.length < 60 and film.rating = 'R';
select * from film 
	join inventory on inventory.film_id = film.film_id 
	join rental on rental.inventory_id = inventory.inventory_id 
	join customer on customer.customer_id = rental.customer_id
	where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and film.rental_rate > 4 and rental.return_date >= '2005-07-28' and rental.return_date <= '2005-08-01'; 
select * from film 
	join inventory on inventory.film_id = film.film_id 
	join rental on rental.inventory_id = inventory.inventory_id 
	join customer on customer.customer_id = rental.customer_id
	where customer.first_name = 'Matthew' and customer.last_name = 'Mahan' and and rental.return_date >= '2005-07-28' and rental.return_date <= '2005-08-01'; 