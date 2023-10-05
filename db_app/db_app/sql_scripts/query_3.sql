SELECT groups.name AS Group_name, subjects.name AS Subject_name, AVG(grades.grade) as Average_grade
FROM grades
JOIN students ON students.id = grades.student_id
JOIN groups ON groups.id = students.group_id
JOIN subjects ON subjects.id = grades.subject_id
WHERE subjects.name = (SELECT name FROM subjects ORDER BY RANDOM())
GROUP BY groups.name;

