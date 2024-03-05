CREATE DATABASE EMPLOYEE;

CREATE TABLE employees(
    Employee_Id INT,
    first_name VARCHAR(64),
    last_name VARCHAR (128),
    email VARCHAR(78),
    phone_number VARCHAR(64),
    Hire_date VARCHAR(45),
    Job_id VARCHAR(78),
    Salary VARCHAR(64),
    Comission_pct VARCHAR(28),
    Manager_Id INT,
    Department_id INT
);
CREATE TABLE employees (
    EMPLOYEE_ID INT,
    FIRST_NAME VARCHAR(50),
    LAST_NAME VARCHAR(50),
    PHONE_NUMBER VARCHAR(20),
    HIRE_DATE DATE,
    JOB_ID VARCHAR(10),
    SALARY DECIMAL(10, 2),
    COMMISSION_PCT DECIMAL(5, 2),
    MANAGER_ID INT,
    DEPARTMENT_ID INT
);

INSERT INTO employees (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT, MANAGER_ID, DEPARTMENT_ID)
VALUES 
(100, 'Steven', 'King', '515.123.4567', '2003-06-17', 'AD_PRES', 24000.00, 0.00, NULL, 90),
(101, 'Neena', 'Kochhar', '515.123.4568', '2005-09-21', 'AD_VP', 17000.00, 0.00, 100, 90),
(102, 'Lex', 'De Haan', '515.123.4569', '2001-01-13', 'AD_VP', 17000.00, 0.00, 100, 40),
(103, 'Alexander', 'Hunold', '590.423.4567', '2006-01-03', 'IT_PROG', 9000.00, 0.00, 102, 60),
(104, 'Bruce', 'Ernst', '590.423.4568', '2007-05-21', 'IT_PROG', 6000.00, 0.00, 103, 60),
(105, 'David', 'Austin', '590.423.4569', '2005-06-25', 'IT_PROG', 17000.00, 0.00, 103, 60),
(106, 'Valli', 'Pataballa', NULL, '2006-02-05', 'IT_PROG', 4800.00, 0.00, 103, 60),
(107, 'Diana', 'Lorentz', NULL, '2007-02-07', 'IT_PROG', 17000.00, 0.00, 103, 60);
