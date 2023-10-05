SELECT students.name AS Student_name, groups.name AS Group_name, subjects.name AS Subject_name, grades.grade AS Grade
FROM grades
JOIN students ON students.id = grades.student_id
JOIN groups ON groups.id = students.group_id
JOIN subjects ON subjects.id = grades.subject_id
WHERE groups.name = (SELECT name FROM groups ORDER BY RANDOM() LIMIT 1) 
AND subjects.name = (SELECT name FROM subjects ORDER BY RANDOM() LIMIT 1);
