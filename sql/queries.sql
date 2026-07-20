SELECT * FROM hogwarts_students LIMIT 5;

-- total studnets --
SELECT COUNT(*) AS total_students
FROM hogwarts_students;



SELECT *
FROM hogwarts_students
WHERE house = 'Gryffindor';



SELECT *
FROM hogwarts_students
WHERE bravery > 8;

SELECT AVG(bravery) AS average_bravery
FROM hogwarts_students;

SELECT MAX(intelligence) AS highest_intelligence
FROM hogwarts_students;


SELECT house, COUNT(*) AS total_students
FROM hogwarts_students
GROUP BY house;

