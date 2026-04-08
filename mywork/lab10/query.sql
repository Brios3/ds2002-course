SELECT s.name, s.email, c.course_name, c.semester
FROM students s
JOIN courses c ON s.student_id = c.student_id
WHERE c.semester = 'Fall 2026';
