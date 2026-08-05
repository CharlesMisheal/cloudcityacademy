"""SQLite helpers — local file-based database."""
import json
import sqlite3
import time
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

# Course card media: Unsplash photos, or /static paths for brand logos
COURSE_IMAGES = {
    "office-ms-word": "https://images.unsplash.com/photo-1586281380349-632531db7ed4?auto=format&fit=crop&w=900&q=80",
    "office-excel": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=900&q=80",
    "office-powerpoint": "https://images.unsplash.com/photo-1557804506-669a67965ba0?auto=format&fit=crop&w=900&q=80",
    "graphic-coreldraw": "/static/images/coreldraw-course.png",
    "graphic-ai": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=900&q=80",
    "video-editing-ai": "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?auto=format&fit=crop&w=900&q=80",
    "ai-engineer": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=900&q=80",
    "python-developer": "https://images.unsplash.com/photo-1515879218367-8466d910aaa4?auto=format&fit=crop&w=900&q=80",
    "system-design-thinking": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=900&q=80",
    "python-data-apps": "https://images.unsplash.com/photo-1555949963-aa79dcee981c?auto=format&fit=crop&w=900&q=80",
    "python-blocks": "/static/images/python-blocks.png",
    "scratch": "/static/images/scratch-logo.svg",
    "android-app-development": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=900&q=80",
    "website-development": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=900&q=80",
    "python-for-beginners": "/static/images/python-logo.svg",
    "cloud-computing": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=900&q=80",
}

# Use contain + brand tint instead of photo crop for these cards
COURSE_LOGO_SLUGS = frozenset(
    {"scratch", "python-for-beginners", "python-blocks", "graphic-coreldraw"}
)



def get_db():
    """Per-request connection, tuned for many students reading/writing at once."""
    if "db" not in g:
        path = current_app.config["DATABASE_PATH"]
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        # timeout: wait up to 30s if another student is mid-write (not fail instantly)
        g.db = sqlite3.connect(str(path), timeout=30.0)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
        g.db.execute("PRAGMA busy_timeout = 30000")
        # WAL: readers don't block writers as harshly (good for class labs)
        try:
            g.db.execute("PRAGMA journal_mode = WAL")
            g.db.execute("PRAGMA synchronous = NORMAL")
            g.db.execute("PRAGMA temp_store = MEMORY")
        except sqlite3.Error:
            pass
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


def _is_locked(err: BaseException) -> bool:
    msg = str(err).lower()
    return "locked" in msg or "busy" in msg


def query_all(sql, params=()):
    last = None
    for attempt in range(8):
        try:
            return get_db().execute(sql, params).fetchall()
        except sqlite3.OperationalError as e:
            last = e
            if not _is_locked(e) or attempt == 7:
                raise
            time.sleep(0.04 * (2**attempt))
    raise last  # pragma: no cover


def query_one(sql, params=()):
    last = None
    for attempt in range(8):
        try:
            return get_db().execute(sql, params).fetchone()
        except sqlite3.OperationalError as e:
            last = e
            if not _is_locked(e) or attempt == 7:
                raise
            time.sleep(0.04 * (2**attempt))
    raise last  # pragma: no cover


def execute(sql, params=()):
    last = None
    for attempt in range(8):
        try:
            db = get_db()
            cur = db.execute(sql, params)
            db.commit()
            return cur
        except sqlite3.OperationalError as e:
            last = e
            try:
                get_db().rollback()
            except sqlite3.Error:
                pass
            if not _is_locked(e) or attempt == 7:
                raise
            time.sleep(0.05 * (2**attempt))
    raise last  # pragma: no cover


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
            student_code TEXT UNIQUE COLLATE NOCASE,
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
    _migrate_schema(db)
    seed_if_empty()


def _migrate_schema(db):
    """Additive column migrations for existing SQLite files."""
    cols = {
        row[1]
        for row in db.execute("PRAGMA table_info(users)").fetchall()
    }
    if "student_code" not in cols:
        db.execute("ALTER TABLE users ADD COLUMN student_code TEXT")
        db.commit()
    db.execute(
        """CREATE UNIQUE INDEX IF NOT EXISTS idx_users_student_code
           ON users(student_code) WHERE student_code IS NOT NULL AND student_code != ''"""
    )
    db.commit()
    _migrate_courses_level_constraint(db)


def _migrate_courses_level_constraint(db):
    """
    Older DBs used: level CHECK(level IN ('beginner', 'advanced')).
    Catalog now stores category tags (office, python, ai, …).
    SQLite cannot ALTER CHECK — rebuild the courses table without the constraint.
    """
    row = db.execute(
        "SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'courses'"
    ).fetchone()
    if not row or not row[0]:
        return
    ddl = row[0]
    # Already free of the old two-level check
    if "beginner" not in ddl and "advanced" not in ddl:
        return
    if "CHECK" not in ddl.upper():
        return

    db.execute("PRAGMA foreign_keys = OFF")
    try:
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS courses_mig (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT NOT NULL UNIQUE,
                title TEXT NOT NULL,
                level TEXT NOT NULL,
                description TEXT NOT NULL,
                is_active INTEGER NOT NULL DEFAULT 1
            );
            DELETE FROM courses_mig;
            INSERT INTO courses_mig (id, slug, title, level, description, is_active)
            SELECT id, slug, title, level, description, is_active FROM courses;
            DROP TABLE courses;
            ALTER TABLE courses_mig RENAME TO courses;
            """
        )
        db.commit()
    finally:
        db.execute("PRAGMA foreign_keys = ON")
        db.commit()


def normalize_student_code(raw: str) -> str:
    """School student IDs are compared without spaces; stored upper-case."""
    return " ".join((raw or "").strip().split()).upper()


def ensure_staff_user(full_name, email, password, role):
    """Create staff account if missing (never overwrites an existing password)."""
    existing = query_one("SELECT id FROM users WHERE email = ?", (email,))
    if existing:
        return existing["id"]
    now = datetime.utcnow().isoformat(timespec="seconds")
    cur = execute(
        """INSERT INTO users (full_name, email, password_hash, role, student_code, is_active, created_at)
           VALUES (?,?,?,?,NULL,1,?)""",
        (full_name, email, generate_password_hash(password), role, now),
    )
    return cur.lastrowid


def _seed_or_refresh_week(week_id: int, lesson: dict, teacher_id: int, now: str):
    """Write full lesson notes + assessment for one week (upgrades to latest MARKER)."""
    from lessons import MARKER

    note = query_one(
        "SELECT * FROM notes WHERE week_id = ? ORDER BY updated_at DESC LIMIT 1",
        (week_id,),
    )
    title = lesson["title"]
    content = lesson["content"]
    examples = lesson["examples"]

    is_current = bool(note and MARKER in (note["content"] or ""))
    if note:
        if not is_current:
            execute(
                """UPDATE notes SET title=?, content=?, examples=?, teacher_id=?, updated_at=?
                   WHERE id=?""",
                (title, content, examples, teacher_id, now, note["id"]),
            )
    else:
        execute(
            """INSERT INTO notes (week_id, teacher_id, title, content, examples, updated_at)
               VALUES (?,?,?,?,?,?)""",
            (week_id, teacher_id, title, content, examples, now),
        )

    qcount = query_one(
        "SELECT COUNT(*) AS c FROM questions WHERE week_id = ?", (week_id,)
    )["c"]
    # Refresh bank when upgrading curriculum or empty
    if qcount == 0 or not is_current:
        if qcount:
            execute("DELETE FROM questions WHERE week_id = ?", (week_id,))
        for qtype, prompt, options, correct, points, order in lesson["questions"]:
            execute(
                """INSERT INTO questions
                   (week_id, qtype, prompt, options_json, correct_option, points, sort_order)
                   VALUES (?,?,?,?,?,?,?)""",
                (week_id, qtype, prompt, options, correct, points, order),
            )


def ensure_course_weeks(course_id: int, slug: str, course_title: str, teacher_id: int, now: str):
    from lessons import syllabus_for
    from curriculum import weeks_for

    plan = syllabus_for(slug, course_title)
    total = weeks_for(slug)

    for lesson in plan:
        n = lesson["week"]
        w = query_one(
            "SELECT id FROM weeks WHERE course_id = ? AND week_number = ?",
            (course_id, n),
        )
        title = lesson["title"]
        if w:
            execute(
                "UPDATE weeks SET title = ?, is_published = 1 WHERE id = ?",
                (title, w["id"]),
            )
            week_id = w["id"]
        else:
            cur = execute(
                """INSERT INTO weeks (course_id, week_number, title, is_published)
                   VALUES (?,?,?,1)""",
                (course_id, n, title),
            )
            week_id = cur.lastrowid

        _seed_or_refresh_week(week_id, lesson, teacher_id, now)

    extras = query_all(
        "SELECT id FROM weeks WHERE course_id = ? AND week_number > ?",
        (course_id, total),
    )
    for ex in extras:
        execute("UPDATE weeks SET is_published = 0 WHERE id = ?", (ex["id"],))


def ensure_course_catalog(teacher_id):
    """Install / refresh courses, week counts, notes, and assessments."""
    now = datetime.utcnow().isoformat(timespec="seconds")
    active_slugs = [row[0] for row in COURSE_CATALOG]

    if active_slugs:
        placeholders = ",".join("?" * len(active_slugs))
        execute(
            f"UPDATE courses SET is_active = 0 WHERE slug NOT IN ({placeholders})",
            tuple(active_slugs),
        )

    from curriculum import duration_label

    for slug, title, category, desc in COURSE_CATALOG:
        full_desc = f"{desc} Duration: {duration_label(slug)}."
        row = query_one("SELECT id FROM courses WHERE slug = ?", (slug,))
        if row:
            execute(
                """UPDATE courses SET title = ?, level = ?, description = ?, is_active = 1
                   WHERE id = ?""",
                (title, category, full_desc, row["id"]),
            )
            course_id = row["id"]
        else:
            cur = execute(
                """INSERT INTO courses (slug, title, level, description, is_active)
                   VALUES (?,?,?,?,1)""",
                (slug, title, category, full_desc),
            )
            course_id = cur.lastrowid

        ensure_course_weeks(course_id, slug, title, teacher_id, now)

    has_any = query_one(
        "SELECT 1 FROM teacher_courses WHERE teacher_id = ? LIMIT 1", (teacher_id,)
    )
    if not has_any:
        for slug in ("office-ms-word", "graphic-coreldraw"):
            c = query_one(
                "SELECT id FROM courses WHERE slug = ? AND is_active = 1", (slug,)
            )
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
    _ensure_demo_student()
    _ = admin_id


def _ensure_demo_student():
    """Demo student ID for local / PA testing: STU-DEMO-001 → AI Engineer."""
    code = "STU-DEMO-001"
    if query_one("SELECT id FROM users WHERE student_code = ?", (code,)):
        return
    course = query_one(
        "SELECT id FROM courses WHERE slug = 'ai-engineer' AND is_active = 1"
    )
    if not course:
        course = query_one("SELECT id FROM courses WHERE is_active = 1 ORDER BY id LIMIT 1")
    if not course:
        return
    now = datetime.utcnow().isoformat(timespec="seconds")
    email = f"{code.lower()}@id.cloudcity.local"
    cur = execute(
        """INSERT INTO users
           (full_name, email, password_hash, role, student_code, is_active, created_at)
           VALUES (?,?,?,'student',?,1,?)""",
        (
            "Demo Student",
            email,
            generate_password_hash(f"nologin-{code}"),
            code,
            now,
        ),
    )
    execute(
        "INSERT INTO enrollments (user_id, course_id, enrolled_at) VALUES (?,?,?)",
        (cur.lastrowid, course["id"], now),
    )
