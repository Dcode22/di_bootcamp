CREATE DATABASE bootcamp;

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    birth_date DATE
);
INSERT INTO students (first_name, last_name, birth_date) 
VALUES ('Marc', 'Benichou', '11/02/1998'), ('Yoan', 'Cohen', '12/03/2010'), ('Lea', 'Benichou', '07/27/1987') ('Amelia', 'Dux', '04/07/1996'), ('David', 'Grez', '06/14/2003'), ('Omer', 'Simpson', '10/03/1980');
insert into students (last_name, first_name, birth_date) values ('Levine', 'David', '06/24/1996');

SELECT * FROM students;
select first_name, last_name from students where id = 2;
select first_name, last_name from students where last_name = 'Benichou' and first_name = 'Marc';
select first_name, last_name from students where last_name = 'Benichou' or first_name = 'Marc';
select first_name, last_name from students where first_name like '%a%';
select first_name, last_name from students where first_name like 'A%';
select first_name, last_name from students where first_name like '%a';
select first_name, last_name from students where first_name like '%a_';
select first_name, last_name from students where id = 1 or id = 3;
select * from students where birth_date >= '2000-01-01';