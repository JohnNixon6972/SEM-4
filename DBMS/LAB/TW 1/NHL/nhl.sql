create database nhl;
use nhl;

create table team(
team_id int,
team_name varchar(10),
city varchar(10),
coach_name varchar(10),
primary key(team_id)
);

create table players(
pid int,
p_name varchar(10),
position varchar(10),
skill varchar(10),
dob date,
team_id int,
primary key(pid),
foreign key(team_id) references team(team_id)
);

create table injury(
inj_name varchar(10),
pid int,
I_date date,
physician varchar(10),
type varchar(10),
primary key(inj_name,pid),
foreign key (pid) references players(pid)
);

create table games(
tid1 int,
tid2 int,
score varchar(5),
guest int,
g_date date,
venue varchar(10),
primary key(tid1,tid2,guest),
foreign key(tid1) references team(team_id),
foreign key(tid2) references team(team_id),
foreign key(guest) references team(team_id)
);

insert into team values(1,'team1','Pune','AAK');
insert into team values(2,'team2','Mumbai','JBN');
insert into team values(3,'team3','Banglore','SSD');
insert into team values(4,'team4','Hyderabad','KTK');

insert into players values(1,'Ramesh','CF','Scorer','02-04-01',1);
insert into players values(2,'Suresh','CMF','Passer','03-08-01',1);
insert into players values(3,'John','CB','Defender','09-06-01',2);
insert into players values(4,'Joe','LWF','Pacer','02-08-02',3);
insert into players values(5,'Oscar','CF','Scorer','12-09-01',4);

insert into games values(1,2,'2-0',2,'02-04-20','Pune');
insert into games values(1,3,'4-1',3,'02-04-20','Pune');
insert into games values(2,3,'5-3',3,'02-04-20','Mumbai');
insert into games values(3,4,'0-1',4,'02-04-20','Banglore');

update games set g_date='03-04-20' where tid2=3;
update games set g_date='04-04-20' where tid1=2;
update games set g_date='05-04-20' where tid1=3;

alter table injury modify column physician varchar(50);
insert into injury values('Knee',3,'02-04-20','Knee specialist','Severe');
insert into injury values('Arm',2,'03-04-20','Arm specialist','Moderate');
insert into injury values('Ankle',4,'04-04-20','Ankle specialist','Severe');
insert into injury values('Head',3,'05-04-20','Head specialist','Minor');

alter table team add captain_id int;

update team set captain_id=NULL;

alter table team add foreign key(captain_id) references players(pid);

update team set captain_id = 1 where team_id=1;
