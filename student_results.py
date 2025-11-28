
# Student Result Management System - Beginner Project
import sqlite3

def init_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        roll TEXT
    );""")
    c.execute("""CREATE TABLE IF NOT EXISTS marks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT,
        marks INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(id)
    );""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
