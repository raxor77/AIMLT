use FirstDB
-- Constraint,not null,
-- primary key: not null and unique,

create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Lname nvarchar(50))

select * from Emp
insert into Emp values (1,'Ahmad','Salleh')
insert into Emp (Id,Fname) values (2,'Rashid')
-- cannot insert below because Null
-- insert into Emp (Id,Lname) values(3,'Razak')

-- To delete table
drop table Emp
select * from Emp

create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Lname nvarchar(50),
City nvarchar(50) default ('Kuala Lumpur')
)
select * from Emp
insert into Emp values (1,'Ahmad','Salleh','JB')
insert into Emp (Id,Fname,City) values (2,'Rashid','KB')
insert into Emp (Id,Fname,Lname) values (3,'Rashidah','Hashim')

drop table Emp

create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
City nvarchar(50) default ('Kuala Lumpur'),
Salary float, 
Mobile nvarchar(10) check (Mobile like'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')
)
insert into Emp values (1,'Ahmad','JB',5000.50,1234567892)
select * from Emp
insert into Emp values (2,'zid','KB',5000.50,56247896333)
-- conflict Arithmetic overflow
insert into Emp values (3,'Fareez','SP',5078.50,562478963f)
-- incorrect syntax

drop table Emp

create table Emp
(Id int primary key,
Fname nvarchar(50) not null,
Mobile nvarchar(10) unique not null check (Mobile like'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
Email nvarChar(100) unique
)
select * from Emp
alter table Emp add City nvarchar(50) not null
select * from Emp
alter table Emp drop column City

insert into Emp values (1,'syed',1234567895,'syed@gmail.com')
insert into Emp values (2,'anuar',1234567895,'anuarmadani@gmail.com')

-- Violation of unique key, cannot insert duplicate key value Mobile
insert into Emp (Id,Fname,Mobile) values (3,'ros','9876543214')
select * from Emp

-- identity(seed,increament)
create table Students
(SId int identity,
SName nvarchar(50) not null,
SFee float)
insert into Students(SName,SFee) values ('Wafi',4500.30)
insert into Students(SName,SFee) values ('Atif',5000.65)
insert into Students(SName,SFee) values ('Shah',5000.70)
select * from Students
insert into Students(SName,SFee) values ('Rafa',4300.70)
------------------------------------------------------------
drop table Students
create table Students
(SId int identity(100,2),
SName nvarchar(50) not null,
SFee float)
insert into Students(SName,SFee) values ('Wafi',4500.30)
insert into Students(SName,SFee) values ('Atif',5000.65)
insert into Students(SName,SFee) values ('Shah',5000.70)
select * from Students
insert into Students(SName,SFee) values ('Rafa',4300.70)
---------------------------------------------------------------

create table Salary
(Grade varchar(1) primary key,
BasicSalary float,
HRA as BasicSalary*0.10 persisted,
TA as BasicSalary*0.15 persisted,
DA as BasicSalary*0.20 persisted
)
select * from Salary
insert into Salary values ('A',10000)
insert into Salary values ('B',5000)
select Grade,BasicSalary,HRA,TA,DA, BasicSalary+TA+DA+HRA as 'Net Salary' from Salary

insert into Salary values ('C',2000)
insert into Salary values ('D',1000)
select max(BasicSalary) as 'Max Basic' from Salary
select min(BasicSalary) as 'Min Basic' from Salary
select avg(BasicSalary) as 'Avg Basic' from Salary
------------------------------------------------------
-- foreign key
------------------------------------------------------
create table Category
(CatId int primary key,
categoryName nvarchar(50) not null unique
)
insert into Category values (1,'Electronics'),(2,'Clothing'),(3,'Home Deco'),(4,'Mobile')
select* from Category order by CatId

create table Products
(PId int primary key identity,
PName nvarchar(50) not null,
PPrice float not null,
ProductsCat int foreign key references Category
)
select * from Products
insert into Products values ('iPhone-17',5000,4)
insert into Products values ('Nothing 3a',2000,4)
insert into Products values ('Washing Machine',4000,1)

insert into Products values ('Shirt',200,2)
insert into Products values ('T-Shirt',199,2)
insert into Products values ('Jeans',399,2)

insert into Products values ('Remote',209,5)

select* from Category
select * from Products

-- select column from table1 join table2 on Table1.CommonColumn=Table2.CommonColumn
select * from Products join Category
on Products.ProductsCat=Category.CatId

select * from Products p join Category c
on p.ProductsCat=c.CatId

select p.PId,p.PName, p.PPrice,p.ProductsCat,c.CategoryName
from Products p join Category c
on p.ProductsCat=c.CatId

select p.PId 'Product ID' ,p.PName 'Product Name' , p.PPrice 'Product Price' ,
p.ProductsCat 'Category Id',c.CategoryName 'Category Name'
from Products p join Category c
on p.ProductsCat=c.CatId

