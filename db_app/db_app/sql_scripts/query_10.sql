SELECT DISTINCT teachers.name AS Teacher_name, GROUP_CONCAT(subjects.name) AS Subjects , students.name AS Student_name
FROM grades 
JOIN subjects ON subjects.id = grades.subject_id 
JOIN teachers ON teachers.id = subjects.teacher_id 
JOIN students ON students.id = grades.student_id 
WHERE teachers.name = (SELECT name FROM teachers ORDER BY RANDOM() LIMIT 1) 
AND students.name = (SELECT name FROM students ORDER BY RANDOM() LIMIT 1);
