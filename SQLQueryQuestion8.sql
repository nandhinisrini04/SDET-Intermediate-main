Create table EMP_Data(
EmpNo int,
EmpName nvarchar(50),
EmpExp int,
EmpDepartment nvarchar(20),
EmpSalary int
);

insert into EMP_Data
values
(1,'John Smith',3,'Software',1000000),
(2,'Peter Parker',10,'Accounts',1500000),
(3,'Ravi Joshi',2,'Software',600000),
(4,'Preethi Jain',15,'Software',3000000),
(5,'Suma Swamy',1,'HR',400000),
(6,'Eva Mark',8,'Accounts',800000),
(7,'Tim Johnson',6,'HR',1000000)

Select * from EMP_Data where EmpDepartment = 'Software'