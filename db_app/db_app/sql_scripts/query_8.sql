WITH random_teacher AS (
    SELECT name FROM teachers 
    WHERE id IN (SELECT teacher_id FROM subjects WHERE id IN (SELECT subject_id FROM grades)) 
    ORDER BY RANDOM() LIMIT 1
)
SELECT teachers.name AS Teacher_name, subjects.name AS Subject_name, AVG(grades.grade) as Average_grade
FROM grades 
JOIN subjects ON subjects.id = grades.subject_id 
JOIN teachers ON teachers.id = subjects.teacher_id 
WHERE teachers.name = (SELECT name FROM random_teacher)
GROUP BY teachers.name, subjects.name;