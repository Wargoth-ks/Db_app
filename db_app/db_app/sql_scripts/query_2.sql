SELECT students.name as Student_name, subjects.name as Subject_name, AVG(grades.grade) as Average_grade
FROM grades
JOIN students ON students.id = grades.student_id
JOIN subjects ON subjects.id = grades.subject_id
WHERE subjects.name = (SELECT name FROM subjects ORDER BY RANDOM())
GROUP BY students.name
ORDER BY average_grade DESC
LIMIT 1;
