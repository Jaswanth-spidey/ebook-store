create database ebook_db;
use ebook_db;
select database();

show tables;

describe bookapp_bookdetailsmodel;

insert into 
bookapp_bookdetailsmodel(profile_pic, book_name, book_price, book_description)
values (load_file('D:/harry.jpg'),'Harry Potter and the Philosopher\'s Stone
',8.25,'The boy wizard Harry Potter has been casting a spell over young readers and their families ever sinc');

select * from bookapp_bookdetailsmodel;

delete from bookapp_bookdetailsmodel where id<3;

drop table bookapp_orderdetailsmodel;

drop database ebook_db;