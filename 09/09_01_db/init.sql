create database if not exists my_db;

use my_db;

create table if not exists articles (
    id int unsigned not null AUTO_INCREMENT,
    title varchar(255) not null,
    text text not null,
    primary key (id)
);

insert into articles (title, text)
values
    ('title1', 'text1'),
    ('title2', 'text2'),
    ('title3', 'text3'),
    ('title4', 'text4'),
    ('title5', 'text5');
