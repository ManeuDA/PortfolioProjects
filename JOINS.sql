
/*

Queries Used for JOIN

*/

--1. (INNER) JOIN - JOIN the shared data from two tables 

SELECT
	emp.name AS employee_name, emp.department_id, emp.role AS employee_role, dep.name AS department_name 
FROM
[Google Projects]..[Employees-Table] emp
JOIN [Google Projects]..[Departments-Table] dep
	ON emp.department_id = dep.department_id

SELECT
	emp.name AS employee_name, emp.department_id, emp.role AS employee_role, dep.name AS department_name 
FROM
[Google Projects]..[Employees-Table] emp
INNER JOIN [Google Projects]..[Departments-Table] dep
	ON emp.department_id = dep.department_id

--2. LEFT JOIN - JOIN the shared data and the left Table (Employees-Table)
SELECT
	emp.name AS employee_name, emp.department_id, emp.role AS employee_role, dep.name AS department_name 
FROM
[Google Projects]..[Employees-Table] emp
LEFT JOIN [Google Projects]..[Departments-Table] dep
	ON emp.department_id = dep.department_id

--3. RIGHT JOIN - JOIN the shared data and the right Table (Departments-Table)
SELECT
	emp.name AS employee_name, emp.department_id, emp.role AS employee_role, dep.name AS department_name 
FROM
[Google Projects]..[Employees-Table] emp
RIGHT JOIN [Google Projects]..[Departments-Table] dep
	ON emp.department_id = dep.department_id

--3. FULL OUTER JOIN - JOIN the shared data and both left and right Table (Employees-Table & Departments-Table)
SELECT
	emp.name AS employee_name, emp.department_id, emp.role AS employee_role, dep.name AS department_name 
FROM
[Google Projects]..[Employees-Table] emp
FULL OUTER JOIN [Google Projects]..[Departments-Table] dep
	ON emp.department_id = dep.department_id