--1. write a query in SQL to display the first name, last name, department number, and department name for each employee
SELECT first_name, last_name, employees.department_id, depart_name
FROM employees 
LEFT JOIN departments ON departments.department_id = employees.department_id
--2. write a query in SQL to display the first and last name, department, city, and state province for each employee
SELECT first_name, last_name, depart_name, city, state_province
FROM employees 
LEFT JOIN departments ON departments.department_id = employees.department_id
LEFT JOIN locations ON locations.location_id = departments.location_id
--3.write a query in SQL to display the first name, last name, department number, and department name, for all employees for departments 80 or 40
SELECT first_name, last_name, employees.department_id, depart_name
FROM employees 
LEFT JOIN departments ON departments.department_id = employees.department_id
WHERE employees.department_id in (40, 80)
--4.write a query in SQL to display all departments including those where does not have any employee
SELECT departments.department_id, depart_name, COUNT(employee_id) AS number_of_employees
FROM departments
LEFT JOIN employees ON employees.department_id = departments.department_id
GROUP BY departments.department_id
--5.write a query in SQL to display the first name of all employees including the first name of their manager
SELECT employees1.first_name AS first_name_employee , employees2.first_name AS first_name_manager
FROM employees AS employees1
LEFT JOIN employees AS employees2 ON employees1.manager_id = employees2.employee_id
--6.write a query in SQL to display the job title, full name (first and last name ) of the employee, 
--and the difference between the maximum salary for the job and the salary of the employee
SELECT job_title, first_name || " " || last_name AS full_name, max_salary, salary, max_salary - salary AS difference
FROM employees 
LEFT JOIN jobs ON jobs.job_id = employees.job_id
--7.write a query in SQL to display the job title and the average salary of employees
SELECT job_title, SUM(salary)/COUNT(job_title) AS average_salary
FROM jobs
LEFT JOIN employees ON jobs.job_id = employees.job_id
GROUP BY job_title
--8.write a query in SQL to display the full name and salary of those employees who work in any department located in London
SELECT first_name || " " || last_name AS full_name, salary, city
FROM employees
LEFT JOIN departments ON departments.department_id = employees.department_id
LEFT JOIN locations ON locations.location_id = departments.location_id
WHERE city = 'London'
--9.write a query in SQL to display the department name and the number of employees in each department
SELECT depart_name, COUNT(employee_id) AS number_of_employees
FROM departments
LEFT JOIN employees ON employees.department_id = departments.department_id
GROUP BY departments.department_id
