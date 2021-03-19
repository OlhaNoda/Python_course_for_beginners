# task2_200321
"""
As a solution to HW, create a file named: task2.sql with all SQL queries:
1. write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" from the table of employees;
2. write a query to get the unique department ID from the employee table
3. write a query to get all employee details from the employee table ordered by first name, descending
4. write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)
5. write a query to get the maximum and minimum salary from the employees table
6. write a query to get a monthly salary (round 2 decimal places) of each and every employee
"""
import sqlite3


def get_select(db_name, selects, select_number):
    con = sqlite3.connect(db_name)
    with con:
        cur = con.cursor()
        cur.execute(selects[select_number])
        records = cur.fetchall()
    return records


if __name__ == '__main__':
    my_db_name = 'hr.db'
    my_selects = {
        '1': 'SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees',
        '2': 'SELECT DISTINCT department_id FROM employees',
        '3': 'SELECT * FROM employees ORDER BY first_name DESC',
        '4': 'SELECT first_name, last_name, salary, salary*0.12 AS PF FROM employees',
        '5': 'SELECT MAX(salary), MIN (salary) FROM employees',
        '6': 'SELECT employee_id, first_name, last_name, ROUND(salary*(1-commission_pct), 2) FROM employees'
    }
    for i in get_select(my_db_name, my_selects, '6'):
        print(i)
