create database institute;
use institute;

CREATE TABLE FACULTY(
FID INT,
FNAME VARCHAR(15),
LNAME VARCHAR(15),
DOB DATE,
DOJ DATE,
GENDER CHAR,
ADDRESS VARCHAR(40),
CITY VARCHAR(15),
SALARY INT,
DESIGNATION VARCHAR(10), 
PRIMARY KEY(FID)
);


insert into FACULTY values(6969,"Harvey","Specter","2001-06-01","2020-01-01","M","51 Story ScraperBay Adelaide West","Toronto",90000,"HOD");
insert into FACULTY values(1248,"Scotty","Jones","2002-01-29","2020-02-05","F","23 Story ScraperBay Adelaide East","Toronto",60000,"Teacher");
insert into FACULTY values(1000,"Tony","Stark","1995-01-01","2010-01-01","M","100818 Malibu Point ","Toronto",100000,"HOD");
insert into FACULTY values(1100,"Steve","Rogers","1980-01-01","2005-01-01","M","100818 Malibu Point ","Toronto",100000,"Teacher");
insert into FACULTY values(1111,"Thor","Odinson","1975-06-14","1999-04-01","M","Asguard Tower","Toronto",100000,"Teacher");
insert into FACULTY values(1230,"Naruto","Uzumaki","2000-08-12","2020-10-12","M","Eichiraku Ramen Street","Konoha",75000,"Teacher");
insert into FACULTY values(1690,"Kakashi","Hatake","1990-10-06","2000-10-12","M","Icha Icha Paradise","Konoha",105000,"HOD");
insert into FACULTY values(9999,"Sasuke","Uchiha","2000-02-06","2020-12-12","M","Uchicha Hideout","Konoha",74999,"Teacher");
insert into FACULTY values(8888,"Itachi","Uchiha","1994-06-29","2008-10-11","M","Uchicha Hideout","Konoha",105100,"HOD");

CREATE TABLE DEPARTMENT(
Dno int,
Dname varchar(20),
Dloc varchar(20), 
Head_Fid integer,
PRIMARY KEY(Dno),
FOREIGN KEY(Head_Fid) references FACULTY(Fid)
);

insert into department values(1,"Law","Pearson Hardman",6969);
insert into department values(2,"Tech","Avengers Tower",1000);
insert into department values(3,"Philosophy"," Forest of Death",1690);
insert into department values(4,"GenJutsu","Hiddent Mist ",8888);

ALTER TABLE FACULTY ADD COLUMN DNO INT;
ALTER TABLE FACULTY ADD CONSTRAINT FOREIGN KEY(DNO) REFERENCES DEPARTMENT(Dno);

UPDATE FACULTY SET DNO = 1 WHERE FID = 6969;
UPDATE FACULTY SET DNO = 1 WHERE FID = 1248;
UPDATE FACULTY SET DNO = 2 WHERE FID = 1000;
UPDATE FACULTY SET DNO = 3 WHERE FID = 1100;
UPDATE FACULTY SET DNO = 3 WHERE FID = 1111;
UPDATE FACULTY SET DNO = 1 WHERE FID = 1230;
UPDATE FACULTY SET DNO = 3 WHERE FID = 1690;
UPDATE FACULTY SET DNO = 4 WHERE FID = 9999;
UPDATE FACULTY SET DNO = 4 WHERE FID = 8888;

CREATE TABLE STUDENT(
USN CHAR(10),
Fname varchar(15),
Lname varchar(15),
Gender char(1),
Address varchar(30),
City varchar(15),
sem int, 
cell_no char(10),
dno int,
Primary key(USN),
Foreign key(Dno) references DEPARTMENT(Dno)
);

insert into student values("2GI19CS175","Venkatesh","Dhongadi","M","Plot 29, Sunflower Apartments","Toronto",3,1208763901,2);
insert into student values("2GI19IS175","John","Nixon","M","Street 129, Batman Apartments","Toronto",3,9081763901,1);
insert into student values("2GI19CS069","Aryan","Kulkarni","M","Street 169, Reyna Apartments","Toronto",3,9081565401,1);
insert into student values("2GI19CS169","Aman","Nadaf","M","C-69069, Sage Apartments","Toronto",3,6969696969,2);
insert into student values("2GI19CS269","Konahamaru","Sarutobi","M","Wall Street","Konoha",3,1969096960,3);


CREATE TABLE SUBJECTS(
SUB_CODE varchar(10),
SUB_NAME VARCHAR(15),
TYPE CHAR,
CREDIT INT,
PRIMARY KEY (SUB_CODE) 
);

insert into subjects values("01","Law",1,5);
insert into subjects values("02","Tech",2,5);
insert into subjects values("03","Philosophy",3,5);
insert into subjects values("04","GenJutsu",4,5);

CREATE TABLE ENGAGES(
FID INT,
SUB_CODE VARCHAR(10),
HOURS INT,
FOREIGN KEY (SUB_CODE) REFERENCES SUBJECTS(SUB_CODE),
FOREIGN KEY(FID) REFERENCES FACULTY(FID)
);

insert into engages values(1100,"03",5);
insert into engages values(1111,"03",5);
insert into engages values(1230,"01",5);
insert into engages values(1248,"01",5);
insert into engages values(9999,"04",5);


CREATE TABLE TEST(
TEST_NO INT,
DATE DATE,
TIME TIME,
PRIMARY KEY(TEST_NO)
);

insert into test values(1,"2021-06-03","10:30:00");

CREATE TABLE SCORE(
USN CHAR(10),
SUB_CODE VARCHAR(10),
TEST_NO INT,
I_A_MARKS INT,
FOREIGN KEY(TEST_NO) REFERENCES TEST(TEST_NO)
);

insert into score values("2GI19CS069","01",1,100);
insert into score values("2GI19CS069","02",1,90);
insert into score values("2GI19CS069","03",1,40);
insert into score values("2GI19CS069","04",1,39);

insert into score values("2GI19CS169","01",1,50);
insert into score values("2GI19CS169","02",1,90);
insert into score values("2GI19CS169","03",1,80);
insert into score values("2GI19CS169","04",1,100);

insert into score values("2GI19CS175","01",1,100);
insert into score values("2GI19CS175","02",1,100);
insert into score values("2GI19CS175","03",1,100);
insert into score values("2GI19CS175","04",1,100);

CREATE TABLE ATTENDANCE(
USN VARCHAR(10),
SUB_CODE VARCHAR(10),
DATE DATE,
TIME TIME,
STATUS VARCHAR(5),
REASON VARCHAR(20),
FOREIGN KEY (USN) REFERENCES STUDENT(USN),
FOREIGN KEY (SUB_CODE) REFERENCES SUBJECTS(SUB_CODE)
);

insert into attendance values("2GI19CS069","04","2021-06-01","12:00:00","P","");
insert into attendance values("2GI19CS169","04","2021-06-01","12:00:00","A","Sick");
insert into attendance values("2GI19CS175","04","2021-06-01","12:00:00","A","I know Genjutsu");
insert into attendance values("2GI19CS269","04","2021-06-01","12:00:00","P","");
insert into attendance values("2GI19IS175","04","2021-06-01","12:00:00","P","");

CREATE TABLE PARENT(
USN VARCHAR(10),
PNAME VARCHAR(15),
ADDRESS VARCHAR(30),
CITY VARCHAR(10),
PINCODE INT,
CELL_NO INT,
FOREIGN KEY(USN) REFERENCES STUDENT(USN)
);

insert into parent values("2GI19CS069","Sova K","Street 169, Reyna Apartments","Toronto",590003,1081565401);
insert into parent values("2GI19CS169","Brimston N","C-69069, Sage Apartments","Toronto",590003,1696969696);
insert into parent values("2GI19CS175","Minato D","Plot 29, Sunflower Apartments","Toronto",590003,1208763901);
insert into parent values("2GI19CS269","Hizuren S","Wall Street","Konoha",590003,1969096960);
insert into parent values("2GI19IS175","Breach N","Street 129, Batman Apartments","Toronto",590003,1081763901);

SELECT Fname, Lname, Dname from STUDENT S, DEPARTMENT D WHERE S.Dno=D.Dno and Dname='LAW';