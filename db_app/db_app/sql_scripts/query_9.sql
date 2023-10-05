SELECT DISTINCT students.name as Student_name, GROUP_CONCAT(subjects.name) AS Subjects
FROM students 
JOIN subjects ON subjects.id = grades.subject_id 
JOIN grades ON students.id = grades.student_id 
WHERE students.name = (SELECT name FROM students ORDER BY RANDOM() LIMIT 1);
