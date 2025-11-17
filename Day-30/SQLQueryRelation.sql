create database ProductSalesDB
use ProductSalesDB

create table Products
(ProductID nvarchar(50) primary key,
ProductName nvarchar(50) not null,
Category nvarchar(50),
UnitPrice decimal(10,2)
)

create table Sales
(SalesID nvarchar(10) primary key,
ProductID nvarchar(50) not null foreign key references Products,
Quantity int not null,
TotalAmount decimal (12,2),
--TotalAmount as (Quantity*(select UnitPrice From Products where Products.ProductID=Sales.ProductID)) persisted,
SalesDate date
)

insert into Products values ('P-001','Laptop','Electronis',2200)

insert into Products values
('P-002','Waching Machine','Electronis',1500),
('P-003','Nothing-3a','Mobiles',1800),
('P-004','Office-Chair','Furnitures',500.50),
('P-005','Office-Desk','Furnitures',700.25),
('P-006','SmartPhone','Electronis',150),
('P-007','Touch Screen Laptop','Electronis',2500),
('P-010','iPhone-I7','Mobiles',5800)

select * from Products
--drop table Sales
insert into Sales (SalesID,ProductID,Quantity,TotalAmount,SalesDate)
values
('SID-001','P-001',2,4400,'2025-11-17')
--
insert into Sales (SalesID,ProductID,Quantity,TotalAmount,SalesDate)
values
('SID-002','P-002',3,4500,'2025-11-17'),
('SID-003','P-003',1,1800,'2025-10-17'),
('SID-004','P-004',1,500.50,'2025-10-17'),
('SID-005','P-005',1,700.25,'2025-10-17'),
('SID-006','P-006',2,300,'2025-09-10'),
('SID-007','P-007',3,7500,'2025-09-10'),
('SID-008','P-010',3,11600,'2025-09-10')

 select s.SalesId,s.SalesDate,p.ProductId,p.ProductName,s.Quantity,p.UnitPrice,s.TotalAmount
 from Sales s,Products p 
 where p.ProductId=s.ProductId