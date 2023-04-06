CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL);

SELECT * FROM users
ORDER BY age
LIMIT 40 OFFSET 20;


CREATE TABLE classmates(
 name TEXT NOT NULL, 
 age INTEGER NOT NULL,
 address TEXT NOT NULL
 );

INSERT INTO classmates(name, age, address)
VALUES ('홍길동',23,'서울');

INSERT INTO classmates
VALUES 
  ('김철수',30,'경기'),
  ('이영미',31,'강원');

UPDATE classmates
SET name='김철수한무두루미',
  address='제주도'
WHERE rowid = 2;

DELETE FROM classmates
  WHERE rowid=3;

DELETE FROM classmates
  WHERE name LIKE '%영%';