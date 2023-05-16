from flask import Flask, request, redirect, url_for, render_template
import datetime
import sqlite3




app = Flask(__name__)

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "password":
            return redirect(url_for('/dashboard'))
        else:
            error = "Invalid username or password"
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

students = []
quizzes = []

@app.route('/dashboard')
def dashboard():
    with sqlite3.connect('hw13.db') as conn:
        cur = conn.cursor()
        students = cur.execute('SELECT * FROM student').fetchall()
        quizzes = cur.execute('SELECT * FROM quizes').fetchall()
        print(students, quizzes)
    return render_template('dashboard.html', students=students, quizzes=quizzes)

@app.route('/student/add', methods=["GET","POST"])
def add_student():
    if request.method == "GET":
        return render_template('add_student.html')
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        with sqlite3.connect('hw13.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT MAX(student_id) FROM student")
            max_id = cur.fetchone()[0]
            new_id = max_id + 1
            cur.execute("INSERT INTO student (student_id, first_name, last_name) VALUES (?, ?, ?)",
                        (new_id, first_name, last_name))
            conn.commit()
            return redirect(url_for('dashboard'))

@app.route('/quiz/add', methods=["GET","POST"])
def add_quiz():
    if request.method == "GET":
        return render_template('add_quiz.html')
    elif request.method == 'POST':
        subject = request.form['subject']
        questions = request.form['questions']
        date_str = request.form['date']
        quiz_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        with sqlite3.connect('hw13.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT MAX(quiz_id) FROM quizes")
            max_id = cur.fetchone()[0]
            new_id = max_id + 1
            cur.execute("INSERT INTO quizes (quiz_id, subject, questions, dates) VALUES (?, ?, ?, ?)",
                        (new_id, subject, questions, quiz_date))
            conn.commit()
            return redirect(url_for('dashboard'))


@app.route('/student/<int:id>')
def results(id):
    with sqlite3.connect('hw13.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT first_name, last_name FROM student WHERE student_id=?", (id,))
        student = cur.fetchone()
        cur.execute("SELECT quiz_id, score FROM results WHERE student_id=?", (id,))
        quiz = cur.fetchone()
        if quiz is None:
            quiz = ('No Results',)
        return render_template('results.html', students=[student], results=[quiz])





if __name__ == '__main__':
    app.run()
