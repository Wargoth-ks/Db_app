SELECT DISTINCT  GROUP_CONCAT(subjects.name) AS Subject_names, teachers.name AS Teacher_name
FROM subjects
JOIN teachers ON teachers.id = subjects.teacher_id
WHERE teachers.name = (SELECT name FROM teachers ORDER BY RANDOM());
