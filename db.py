"""SQLite helpers — local file-based database."""
import json
import sqlite3
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

from flask import current_app, g
from werkzeug.security import generate_password_hash

# level field stores a category used for grouping / imagery
# (slug, title, category, description)
COURSE_CATALOG = [
    (
        "office-ms-word",
        "Office Application (MS Word)",
        "office",
        "Create and format professional documents, letters, reports, and templates in Microsoft Word.",
    ),
    (
        "office-excel",
        "Office Application (Excel)",
        "office",
        "Work with spreadsheets, formulas, charts, and data tables in Microsoft Excel.",
    ),
    (
        "office-powerpoint",
        "Office Application (PowerPoint)",
        "office",
        "Design clear slide decks, presentations, and storytelling with Microsoft PowerPoint.",
    ),
    (
        "graphic-coreldraw",
        "Graphic Design (CorelDRAW)",
        "design",
        "Vector graphics, layouts, branding and print-ready artwork using CorelDRAW.",
    ),
    (
        "graphic-ai",
        "Graphic Design (AI)",
        "design",
        "Modern visual design with AI-assisted tools for posters, social media and creative assets.",
    ),
    (
        "video-editing-ai",
        "Video Editing & Animation (AI)",
        "media",
        "Edit video, motion, and simple animation with AI-assisted production workflows.",
    ),
    (
        "ai-engineer",
        "AI Engineer",
        "ai",
        "Foundations of applied AI: models, tools, prompts, and building useful AI solutions.",
    ),
    (
        "python-developer",
        "Python Developer",
        "python",
        "Write clean Python code, solve problems, and build developer habits for real projects.",
    ),
    (
        "system-design-thinking",
        "System Design / Thinking",
        "systems",
        "Design thinking and systems thinking: problem framing, architecture concepts, and structured solutions.",
    ),
    (
        "python-data-apps",
        "Python & Data Apps",
        "python",
        "Use Python for data work and build small data-driven applications.",
    ),
    (
        "python-blocks",
        "Python Blocks",
        "kids",
        "Visual block-based path into Python concepts for younger or early learners.",
    ),
    (
        "scratch",
        "Scratch",
        "kids",
        "Create interactive stories, games and animations with Scratch.",
    ),
    (
        "android-app-development",
        "Android App Development",
        "mobile",
        "Build mobile apps for Android — screens, layout, and packaging a simple app.",
    ),
    (
        "website-development",
        "Website Development",
        "web",
        "Create modern websites with structure, styling, and practical project delivery.",
    ),
    (
        "python-for-beginners",
        "Python for Beginners",
        "python",
        "Start Python from zero: syntax, variables, simple programs and hands-on practice.",
    ),
    (
        "cloud-computing",
        "Cloud Computing",
        "cloud",
        "Cloud concepts, services, deployment ideas, and how modern apps run online.",
    ),
]

CATEGORY_LABELS = {
    "office": "Office",
    "design": "Design",
    "media": "Media",
    "ai": "AI",
    "python": "Python",
    "systems": "Systems",
    "kids": "Kids & blocks",
    "mobile": "Mobile",
    "web": "Web",
    "cloud": "Cloud",
}

# Unique free Unsplash image per course (no shared thumbnails)
COURSE_IMAGES = {
    "office-ms-word": "https://images.unsplash.com/photo-1586281380349-632531db7ed4?auto=format&fit=crop&w=900&q=80",
    "office-excel": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=900&q=80",
    "office-powerpoint": "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=900&q=80",
    "graphic-coreldraw": "https://images.unsplash.com/photo-1626785774573-4b7993143485?auto=format&fit=crop&w=900&q=80",
    "graphic-ai": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=900&q=80",
    "video-editing-ai": "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?auto=format&fit=crop&w=900&q=80",
    "ai-engineer": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=900&q=80",
    "python-developer": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=900&q=80",
    "system-design-thinking": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=900&q=80",
    "python-data-apps": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?auto=format&fit=crop&w=900&q=80",
    "python-blocks": "https://images.unsplash.com/photo-1587620962725-abab7fe55159?auto=format&fit=crop&w=900&q=80",
    "scratch": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=900&q=80",
    "android-app-development": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=900&q=80",
    "website-development": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=900&q=80",
    "python-for-beginners": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=900&q=80",
    "cloud-computing": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=900&q=80",
}



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
            level TEXT NOT NULL,
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


def ensure_staff_user(full_name, email, password, role):
    """Create staff account if missing (never overwrites an existing password)."""
    existing = query_one("SELECT id FROM users WHERE email = ?", (email,))
    if existing:
        return existing["id"]
    now = datetime.utcnow().isoformat(timespec="seconds")
    cur = execute(
        """INSERT INTO users (full_name, email, password_hash, role, is_active, created_at)
           VALUES (?,?,?,?,1,?)""",
        (full_name, email, generate_password_hash(password), role, now),
    )
    return cur.lastrowid


def _seed_week_one_content(course_slug, course_title, teacher_id, now):
    course = query_one("SELECT id FROM courses WHERE slug = ?", (course_slug,))
    if not course:
        return
    week1 = query_one(
        "SELECT id FROM weeks WHERE course_id = ? AND week_number = 1",
        (course["id"],),
    )
    if not week1 or query_one("SELECT id FROM notes WHERE week_id = ?", (week1["id"],)):
        return

    execute(
        """INSERT INTO notes (week_id, teacher_id, title, content, examples, updated_at)
           VALUES (?,?,?,?,?,?)""",
        (
            week1["id"],
            teacher_id,
            f"Welcome to {course_title}",
            f"Welcome to CloudCity Academy.\n\n"
            f"This is Week 1 of {course_title}. Your teacher will expand notes and examples here.\n\n"
            f"Build good habits from day one: save your work, follow class naming rules, "
            f"and capture clear screenshots for your weekly assessment.",
            "Checklist:\n1. Open the class software\n2. Create / save your first practice file\n"
            "3. Name it clearly (YourName_Week1)\n4. Screenshot your work when ready",
            now,
        ),
    )
    q_seed = [
        (
            "mcq",
            f"What is the first recommended habit in {course_title}?",
            json.dumps(
                [
                    "Skip practice",
                    "Save and name files carefully",
                    "Never take screenshots",
                    "Ignore the lesson notes",
                ]
            ),
            "Save and name files carefully",
            2,
            1,
        ),
        (
            "mcq",
            "Weekly assessments may include:",
            json.dumps(
                [
                    "Only multiple choice",
                    "MCQ, written answers, and screenshots",
                    "Payment only",
                    "Nothing practical",
                ]
            ),
            "MCQ, written answers, and screenshots",
            2,
            2,
        ),
        (
            "subjective",
            f"In one or two sentences, what do you hope to learn in {course_title}?",
            None,
            None,
            3,
            3,
        ),
        (
            "upload",
            "Upload a screenshot of your first practice session this week.",
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


def ensure_course_catalog(teacher_id):
    """Install / refresh the live course list (safe to run every boot)."""
    now = datetime.utcnow().isoformat(timespec="seconds")
    active_slugs = [row[0] for row in COURSE_CATALOG]

    # Hide anything not in the current catalog
    if active_slugs:
        placeholders = ",".join("?" * len(active_slugs))
        execute(
            f"UPDATE courses SET is_active = 0 WHERE slug NOT IN ({placeholders})",
            tuple(active_slugs),
        )

    for slug, title, category, desc in COURSE_CATALOG:
        row = query_one("SELECT id FROM courses WHERE slug = ?", (slug,))
        if row:
            execute(
                """UPDATE courses SET title = ?, level = ?, description = ?, is_active = 1
                   WHERE id = ?""",
                (title, category, desc, row["id"]),
            )
            course_id = row["id"]
        else:
            cur = execute(
                """INSERT INTO courses (slug, title, level, description, is_active)
                   VALUES (?,?,?,?,1)""",
                (slug, title, category, desc),
            )
            course_id = cur.lastrowid
            for n in range(1, 5):
                execute(
                    """INSERT INTO weeks (course_id, week_number, title, is_published)
                       VALUES (?,?,?,1)""",
                    (
                        course_id,
                        n,
                        "Week 1: Getting Started" if n == 1 else f"Week {n}",
                    ),
                )

        week_count = query_one(
            "SELECT COUNT(*) AS c FROM weeks WHERE course_id = ?", (course_id,)
        )["c"]
        if week_count == 0:
            for n in range(1, 5):
                execute(
                    """INSERT INTO weeks (course_id, week_number, title, is_published)
                       VALUES (?,?,?,1)""",
                    (
                        course_id,
                        n,
                        "Week 1: Getting Started" if n == 1 else f"Week {n}",
                    ),
                )

        _seed_week_one_content(slug, title, teacher_id, now)

    # Demo teacher only: if they have no assignments yet, give two sample courses.
    # Admin controls all further teacher → course assignments.
    has_any = query_one(
        "SELECT 1 FROM teacher_courses WHERE teacher_id = ? LIMIT 1", (teacher_id,)
    )
    if not has_any:
        for slug in ("office-ms-word", "graphic-coreldraw"):
            c = query_one("SELECT id FROM courses WHERE slug = ? AND is_active = 1", (slug,))
            if c:
                execute(
                    "INSERT OR IGNORE INTO teacher_courses (teacher_id, course_id) VALUES (?,?)",
                    (teacher_id, c["id"]),
                )


def seed_if_empty():
    """Seed staff + course catalog. Safe to call every boot."""
    admin_id = ensure_staff_user(
        "CloudCity Admin",
        "admin@cloudcity.local",
        "Admin123!",
        "admin",
    )
    teacher_id = ensure_staff_user(
        "Ada Teacher",
        "teacher@cloudcity.local",
        "Teacher123!",
        "teacher",
    )
    ensure_course_catalog(teacher_id)
    _ = admin_id
