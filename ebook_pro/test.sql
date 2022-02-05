show databases;
create database test_db;
use test_db;

create table test_tb(
	id int not null unique auto_increment,
	img varchar(50) not null
);

drop table test_tb;

INSERT INTO test_tb(img) VALUES(LOAD_FILE('D:/harry.jpg'));

select * from test_tb;