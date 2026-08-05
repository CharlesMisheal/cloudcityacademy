"""SQLite helpers — free, file-based, no external DB."""
import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

from flask import current_app, g
from werkzeug.security import generate_password_hash


def get_db():
    if "db" not in g:
        path = current_app.config["DATABASE_PATH"]
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        g.db = sqlite3.connect(path)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(_e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@contextmanager
def db_cursor():
    db = get_db()
    cur = db.cursor()
    try:
        yield cur
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        cur.close()


def query_all(sql, params=()):
    return get_db().execute(sql, params).fetchall()


def query_one(sql, params=()):
    return get_db().execute(sql, params).fetchone()


def execute(sql, params=()):
    db = get_db()
    cur = db.execute(sql, params)
    db.commit()
    return cur


def init_db():
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE COLLATE NOCASE,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('admin', 'teacher', 'student')),
            is_active INTEGER NOT NULL DEFAULT 1,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            level TEXT NOT NULL CHECK(level IN ('beginner', 'advanced')),
            description TEXT NOT NULL,
            is_active INTEGER NOT NULL DEFAULT 1
        );

        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
            enrolled_at TEXT NOT NULL,
            certificate_issued_at TEXT,
            UNIQUE(user_id, course_id)
        );

        CREATE TABLE IF NOT EXISTS weeks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
            week_number INTEGER NOT NULL,
            title TEXT NOT NULL,
            is_published INTEGER NOT NULL DEFAULT 1,
            UNIQUE(course_id, week_number)
        );

        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week_id INTEGER NOT NULL REFERENCES weeks(id) ON DELETE CASCADE,
            teacher_id INTEGER REFERENCES users(id),
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            examples TEXT NOT NULL DEFAULT '',
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week_id INTEGER NOT NULL REFERENCES weeks(id) ON DELETE CASCADE,
            qtype TEXT NOT NULL CHECK(qtype IN ('mcq', 'subjective', 'upload')),
            prompt TEXT NOT NULL,
            options_json TEXT,
            correct_option TEXT,
            points INTEGER NOT NULL DEFAULT 1,
            sort_order INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            week_id INTEGER NOT NULL REFERENCES weeks(id) ON DELETE CASCADE,
            submitted_at TEXT NOT NULL,
            score REAL NOT NULL DEFAULT 0,
            max_score REAL NOT NULL DEFAULT 0,
            status TEXT NOT NULL DEFAULT 'submitted',
            UNIQUE(student_id, week_id)
        );

        CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL REFERENCES assessments(id) ON DELETE CASCADE,
            question_id INTEGER NOT NULL REFERENCES questions(id) ON DELETE CASCADE,
            text_answer TEXT,
            selected_option TEXT,
            is_correct INTEGER,
            points_awarded REAL NOT NULL DEFAULT 0,
            teacher_feedback TEXT,
            UNIQUE(assessment_id, question_id)
        );

        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            answer_id INTEGER NOT NULL REFERENCES answers(id) ON DELETE CASCADE,
            stored_name TEXT NOT NULL,
            original_name TEXT NOT NULL,
            uploaded_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS teacher_courses (
            teacher_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
            PRIMARY KEY (teacher_id, course_id)
        );
        """
    )
    db.commit()
    seed_if_empty()


def seed_if_empty():
    if query_one("SELECT id FROM users WHERE role = 'admin'"):
        return

    now = datetime.utcnow().isoformat(timespec="seconds")

    execute(
        "INSERT INTO users (full_name, email, password_hash, role, is_active, created_at) VALUES (?,?,?,?,1,?)",
        (
            "CloudCity Admin",
            "admin@cloudcity.local",
            generate_password_hash("Admin123!"),
            "admin",
            now,
        ),
    )
    execute(
        "INSERT INTO users (full_name, email, password_hash, role, is_active, created_at) VALUES (?,?,?,?,1,?)",
        (
            "Ada Teacher",
            "teacher@cloudcity.local",
            generate_password_hash("Teacher123!"),
            "teacher",
            now,
        ),
    )
    teacher = query_one("SELECT id FROM users WHERE email = ?", ("teacher@cloudcity.local",))

    courses = [
        (
            "python-beginners",
            "Python Beginners",
            "beginner",
            "Foundations of Python for absolute beginners: syntax, data types, control flow, and practice.",
        ),
        (
            "python-advanced",
            "Python Advanced",
            "advanced",
            "Deeper Python: functions mastery, OOP, files, modules, and applied problem solving.",
        ),
    ]
    for slug, title, level, desc in courses:
        execute(
            "INSERT INTO courses (slug, title, level, description, is_active) VALUES (?,?,?,?,1)",
            (slug, title, level, desc),
        )

    for course in query_all("SELECT id, title FROM courses"):
        execute(
            "INSERT INTO teacher_courses (teacher_id, course_id) VALUES (?,?)",
            (teacher["id"], course["id"]),
        )
        for n in range(1, 5):
            execute(
                "INSERT INTO weeks (course_id, week_number, title, is_published) VALUES (?,?,?,1)",
                (course["id"], n, f"Week {n}: Getting Started" if n == 1 else f"Week {n}"),
            )

    # Seed beginner week 1 content
    begin = query_one("SELECT id FROM courses WHERE slug = ?", ("python-beginners",))
    week1 = query_one(
        "SELECT id FROM weeks WHERE course_id = ? AND week_number = 1",
        (begin["id"],),
    )
    execute(
        """INSERT INTO notes (week_id, teacher_id, title, content, examples, updated_at)
           VALUES (?,?,?,?,?,?)""",
        (
            week1["id"],
            teacher["id"],
            "Hello, Python",
            "Welcome to CloudCity Academy.\n\n"
            "This week you will write your first programs: print messages, store values in variables, "
            "and understand how Python runs line by line.\n\n"
            "Focus on clarity. Small programs, run often.",
            'print("Hello, CloudCity")\n\nname = "Ada"\nprint("Hello,", name)',
            now,
        ),
    )
    q_seed = [
        (
            "mcq",
            "Which function displays text in Python?",
            json.dumps(["echo()", "print()", "show()", "display()"]),
            "print()",
            2,
            1,
        ),
        (
            "mcq",
            "Which symbol starts a comment in Python?",
            json.dumps(["//", "/*", "#", "--"]),
            "#",
            2,
            2,
        ),
        (
            "subjective",
            "In one or two sentences, explain what a variable is.",
            None,
            None,
            3,
            3,
        ),
        (
            "upload",
            "Upload a screenshot of your first print program running successfully.",
            None,
            None,
            3,
            4,
        ),
    ]
    for qtype, prompt, options, correct, points, order in q_seed:
        execute(
            """INSERT INTO questions
               (week_id, qtype, prompt, options_json, correct_option, points, sort_order)
               VALUES (?,?,?,?,?,?,?)""",
            (week1["id"], qtype, prompt, options, correct, points, order),
        )
