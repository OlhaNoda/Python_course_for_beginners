# task1_200321
"""
Create a table
Create a table of your choice inside the sample SQLite database, rename it, and add a new column.
Insert a couple rows inside your table. Also, perform UPDATE and DELETE statements on inserted rows.
As a solution to this task, create a file named: task1.sql, with all the SQL statements you have used to accomplish this task
"""
import sqlite3

# установка связи с базой данных
conn = sqlite3.connect('example.db')
cur = conn.cursor()

# создание таблицы
cur.execute("""CREATE TABLE IF NOT EXISTS my_users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()

# переименование таблицы
cur.execute("ALTER TABLE my_users RENAME TO users")
conn.commit()

# добавление нового поля
cur.execute("ALTER TABLE users ADD COLUMN 'age' 'INT'")
conn.commit()

# добавление записи в таблицу users
cur.execute("""INSERT INTO users(userid, fname, lname, gender, age) 
   VALUES('00003', 'Tom', 'Jackson', 'male', '25');""")
conn.commit()

# корректировка записи
cur.execute("""UPDATE users SET age = '30' WHERE userid = '00001'""")
conn.commit()

# удаление записи
cur.execute("""DELETE FROM users WHERE lname = 'Jhonson'""")
conn.commit()

# вывод таблицы
for value in cur.execute("SELECT * FROM users"):
    print(value)
