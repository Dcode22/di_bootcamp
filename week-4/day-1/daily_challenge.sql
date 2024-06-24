select count(*) from actors;
insert into actors (first_name, age, number_oscars)
values ('The', '1978-11-04', 3), ('Daniel', '1987-07-31', 2)
-- ERROR:  null value in column "last_name" of relation "actors" violates not-null constraint