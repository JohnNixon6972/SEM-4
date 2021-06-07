create database airline;
use airline;

CREATE TABLE FLIGHTS(
flight_no integer,
fromPlace varchar(20),
toPlace varchar(20),
distance integer,
departs date,
arrives date,
price real,
PRIMARY KEY(flight_no));

CREATE TABLE AIRCRAFT(
a_id integer,
a_name varchar(15),
cruisingrange integer,
PRIMARY KEY(a_id));

CREATE TABLE EMPLOYEES(
e_id integer,
e_name varchar(15),
salary integer,
PRIMARY KEY(e_id));

CREATE TABLE CERTIFIED(
e_id integer,
a_id integer,
foreign key(e_id) references employees(e_id),
foreign key(a_id) references aircraft(a_id));


insert into flights values(255, "bangalore", "frankfurt", 200, '2011-08-01', '2011-08-01', 5000);
insert into flights values(256, "bangalore", "frankfurt", 200, '2011-08-01', '2011-08-01', 8000);
insert into flights values(257, "bangalore", "delhi", 200, '2011-08-01', '2011-08-01', 5000);
insert into flights values(258, "bangalore", "delhi", 200, '2011-08-01', '2011-08-01', 6000);
insert into flights values(259, "bangalore", "mangalore", 200, '2011-08-01', '2011-08-01', 8000);

insert into aircraft values(685, "boeing15", 1000);
insert into aircraft values(686, "boeing10", 1000);
insert into aircraft values(687, "skytrain", 1000);
insert into aircraft values(688, "avenger", 100);

insert into employees values(101, "asha", 90000);
insert into employees values(102, "arun", 85000);
insert into employees values(103, "anand", 3000);
insert into employees values(104, "ramya", 4000);

insert into certified values(101, 685);
insert into certified values(101, 686);
insert into certified values(101, 687);
insert into certified values(101, 688);
insert into certified values(102, 685);
insert into certified values(103, 686);
insert into certified values(103, 687);

select distinct a.a_name from aircraft a, certified c, employees e where c.e_id = e.e_id and e.salary>80000;

SELECT C.e_id, MAX(a.cruisingrange) FROM CERTIFIED C, AIRCRAFT A WHERE C.a_id = A.a_id GROUP BY C.e_id HAVING COUNT(*) > 3;

SELECT E.e_name FROM EMPLOYEES E WHERE E.salary< (SELECT min(price) FROM FLIGHTS WHERE fromPlace = 'bangalore' AND toPlace = 'frankfurt');
 
SELECT A.a_id FROM AIRCRAFT A WHERE A.cruisingrange> (SELECT min(distance) FROM FLIGHTS WHERE fromPlace='bangalore' AND toPlace = 'delhi'); 

 

