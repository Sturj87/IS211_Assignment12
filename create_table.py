import sqlite3

conn = sqlite3.connect('hw13.db')
sql_file = open('schema.sql')
sql_tables = sql_file.read()

conn.executescript(sql_tables)
conn.execute("INSERT INTO student(student_id, first_name, last_name) VALUES (1,'John', 'Smith')")
conn.execute("INSERT INTO quizes(quiz_id, subject, questions, dates) VALUES (1,'Python_Basics', 5, 'February, 5th,2015')")
conn.execute("INSERT INTO results(results_id, student_id, quiz_id, score) VALUES (1,1,1, 85)")

conn.commit()
conn.close()
