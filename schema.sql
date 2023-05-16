CREATE TABLE student(
        student_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
        );

CREATE TABLE quizes(
        quiz_id INTEGER PRIMARY KEY,
        subject TEXT NOT NULL,
        questions INTEGER NOT NULL,
        dates TEXT NOT NULL
        );

CREATE TABLE results(
        results_id INTEGER PRIMARY KEY,
        student_id INTEGER NOT NULL,
        quiz_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES student (student_id),
        FOREIGN KEY (quiz_id) REFERENCES quizes (quiz_id)
        );