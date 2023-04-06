CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('rabbit', 'herbivore', 3, 150, NULL),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('eagle', 'carnivore', 8, 75, NULL),
('dolphin', 'carnivore', 210, NULL, 3),
('alligator', 'carnivore', 250, 50, NULL),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

--3번
SELECT name, height FROM zoo;

--4번
UPDATE zoo
  SET height='15'
  WHERE rowid = 2;

SELECT * FROM zoo
WHERE name='rabbit';

--5번
DELETE FROM zoo 
WHERE eat='omnivore';

SELECT * FROM zoo;