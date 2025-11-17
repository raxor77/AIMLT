create Database PersonalDB 
use PersonalDB

create table Person
(PersonID nvarchar(50) primary key,
FullName nvarchar(50) not null,
DateofBirth date,
Nationality nvarchar(50))

-- drop table Person
select * from Person
--drop table Passport
create table Passport
(PassportID nvarchar(50) primary key,
PersonID nvarchar(50) not null foreign key references Person,
PassportNumber nvarchar(50) unique,
IssueDate date,
ExpiryDate date)
select * from Passport

insert into Person values
('ID001','Asrul Adam','1996-12-06','Malaysia')

insert into Person values
('ID002','Kim Jong Yung','2006-06-07','Korea'),
('ID003','Mamoto Kenji','2003-10-07','Japan'),
('ID004','David Copper','1989-06-07','Australia'),
('ID005','Asmah Ali','2000-11-11','Malaysia'),
('ID006','Zaid Daud','2011-05-25','Malaysia')

 insert into Passport(PassportID,PersonID,PassportNumber,IssueDate,ExpiryDate)
 values
 ('001','ID001','CX000010002','2023-12-06','2026-12-06'),
 ('002','ID002','KX000010002','2025-06-07','2028-06-07'),
 ('003','ID003','JX000010002','2024-10-07','2029-10-07'),
 ('004','ID004','AU000010002','2024-06-07','2026-06-07'),
 ('005','ID005','CX000010302','2025-11-11','2028-11-11'),
 ('006','ID006','CX000010782','2022-05-25','2027-05-25')
 select * from Passport
 select * from Person

-- select s.SalesId,s.SalesDate,p.ProductId,p.ProductName,s.Quantity,p.UnitPrice,s.TotalAmount
-- from Sales s,Products p 
-- where p.ProductId=s.ProductId