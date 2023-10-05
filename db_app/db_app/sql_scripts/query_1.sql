SELECT students.name as Student_name, AVG(grades.grade) as Average_grade
FROM grades
JOIN students ON students.id = grades.student_id
GROUP BY students.name
ORDER BY average_grade DESC
LIMIT 5;