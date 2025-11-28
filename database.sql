
-- SQL schema for Student Result Management System
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    roll VARCHAR(20)
);

CREATE TABLE marks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    subject VARCHAR(50),
    marks INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id)
);
