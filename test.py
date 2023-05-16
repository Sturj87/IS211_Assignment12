import sqlite3

with sqlite3.connect('hw13.db') as conn:
    cur = conn.cursor()
    students = cur.execute('SELECT * FROM student').fetchall()
    quizzes = cur.execute('SELECT * FROM quizes').fetchall()
    print(students, quizzes)