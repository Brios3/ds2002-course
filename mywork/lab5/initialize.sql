CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    major VARCHAR(50)
);
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name VARCHAR(100),
    student_id INTEGER,
    semester VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
INSERT INTO students VALUES (1, 'Alex Brown', 'abrown@univ.edu', 'Economics');
INSERT INTO students VALUES (2, 'Maria Lopez', 'mlopez@univ.edu', 'Computer Science');
INSERT INTO students VALUES (3, 'Daniel Kim', 'dkim@univ.edu', 'Mathematics');
INSERT INTO students VALUES (4, 'Sarah Patel', 'spatel@univ.edu', 'Biology');
INSERT INTO students VALUES (5, 'James Carter', 'jcarter@univ.edu', 'Finance');
INSERT INTO students VALUES (6, 'Olivia White', 'owhite@univ.edu', 'Physics');
INSERT INTO students VALUES (7, 'Michael Green', 'mgreen@univ.edu', 'History');
INSERT INTO students VALUES (8, 'Emily Davis', 'edavis@univ.edu', 'Chemistry');
INSERT INTO students VALUES (9, 'Ryan Hall', 'rhall@univ.edu', 'Political Science');
INSERT INTO students VALUES (10, 'Sophia Clark', 'sclark@univ.edu', 'Psychology');
INSERT INTO courses VALUES (101, 'Intro to Economics', 1, 'Fall 2026');
INSERT INTO courses VALUES (102, 'Data Structures', 2, 'Fall 2026');
INSERT INTO courses VALUES (103, 'Linear Algebra', 3, 'Fall 2026');
INSERT INTO courses VALUES (104, 'Genetics', 4, 'Fall 2026');
INSERT INTO courses VALUES (105, 'Corporate Finance', 5, 'Fall 2026');
INSERT INTO courses VALUES (106, 'Quantum Physics', 6, 'Fall 2026');
INSERT INTO courses VALUES (107, 'World History', 7, 'Fall 2026');
INSERT INTO courses VALUES (108, 'Organic Chemistry', 8, 'Fall 2026');
INSERT INTO courses VALUES (109, 'International Relations', 9, 'Fall 2026');
INSERT INTO courses VALUES (110, 'Psychology', 10, 'Fall 2026');
