--создание таблицы
CREATE TABLE IF NOT EXISTS my_users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT)
   
--переименование таблицы
ALTER TABLE my_users RENAME TO users

--добавление нового поля
ALTER TABLE users ADD COLUMN age

--добавление записи в таблицу users
INSERT INTO users
(userid, fname, lname, gender, age)
VALUES
('00003', 'Tom', 'Jackson', 'male', '25')
   
--корректировка записи
UPDATE users SET age = '30' WHERE userid = '00001'

--удаление записи
DELETE FROM users WHERE lname = 'Jhonson'  
