create database flick;
use flick;
create table sample(
name varchar(30),
age int,
dob date,
phnumber int,
unique(name),
primary key(dob)
);

desc sample;