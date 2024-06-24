insert into items (name, price)
values ('small desk', 100), ('large desk', 300), ('fan', 80)

insert into customers (firstname, lastname)
values ('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson')

select * from items

select * from items where price > 80

select * from items where price < 300

select * from customers where lastname = 'Smith'

select * from customers where lastname = 'Jones'

select * from customers where firstname != 'Scott'
