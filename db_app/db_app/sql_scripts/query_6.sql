SELECT DISTINCT groups.name AS Group_name, students.name AS Student_name
FROM students
JOIN groups ON groups.id = students.group_id
WHERE groups.name = (SELECT name FROM groups ORDER BY RANDOM());
