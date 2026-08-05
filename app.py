"""
CloudCity Academy — free stack only.

No paid APIs, no paid database, no paid hosting required.
Host on PythonAnywhere free: https://cloudcity.pythonanywhere.com
"""
from __future__ import annotations

import json
import uuid
from datetime import datetime
from functools import wraps
from pathlib import Path

from flask import (
    Flask,
    abort,
    flash,
    g,
    redirect,
    render_template,
    request,
    send_file,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from config import Config
from db import close_db, execute, init_db, query_all, query_one
from services.certificates import build_certificate_pdf


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Path(app.config["UPLOAD_FOLDER"]).mkdir(parents=True, exist_ok=True)
    Path(app.config["DATABASE_PATH"]).parent.mkdir(parents=True, exist_ok=True)

    app.teardown_appcontext(close_db)

    @app.before_request
    def load_user():
        g.user = None
        uid = session.get("user_id")
        if uid:
            g.user = query_one("SELECT * FROM users WHERE id = ? AND is_active = 1", (uid,))
            if not g.user:
                session.clear()

    @app.context_processor
    def inject_brand():
        return {
            "ACADEMY_NAME": app.config["ACADEMY_NAME"],
            "PUBLIC_HOST": app.config["PUBLIC_HOST"],
            "current_user": g.get("user"),
        }

    with app.app_context():
        init_db()

    register_routes(app)
    return app


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not g.user:
            flash("Please sign in to continue.", "warn")
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)

    return wrapped


def role_required(*roles):
    def decorator(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if not g.user:
                return redirect(url_for("login", next=request.path))
            if g.user["role"] not in roles:
                abort(403)
            return view(*args, **kwargs)

        return wrapped

    return decorator


def allowed_file(filename: str) -> bool:
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS
    )


def now_iso() -> str:
    return datetime.utcnow().isoformat(timespec="seconds")


def student_course(user_id: int):
    """Active course enrolment for a student (one primary course)."""
    return query_one(
        """
        SELECT c.*, e.id AS enrollment_id, e.certificate_issued_at, e.enrolled_at
        FROM enrollments e
        JOIN courses c ON c.id = e.course_id
        WHERE e.user_id = ? AND c.is_active = 1
        ORDER BY e.enrolled_at DESC
        LIMIT 1
        """,
        (user_id,),
    )


def student_enrolled_in_course(user_id: int, course_id: int) -> bool:
    row = query_one(
        """
        SELECT 1 FROM enrollments e
        JOIN courses c ON c.id = e.course_id
        WHERE e.user_id = ? AND e.course_id = ? AND c.is_active = 1
        """,
        (user_id, course_id),
    )
    return bool(row)


def teacher_teaches_course(teacher_id: int, course_id: int) -> bool:
    row = query_one(
        """
        SELECT 1 FROM teacher_courses
        WHERE teacher_id = ? AND course_id = ?
        """,
        (teacher_id, course_id),
    )
    return bool(row)


def user_can_access_course(course_id: int) -> bool:
    """Admin: all courses. Teacher: assigned only. Student: enrolled only."""
    if not g.user:
        return False
    role = g.user["role"]
    if role == "admin":
        return True
    if role == "teacher":
        return teacher_teaches_course(g.user["id"], course_id)
    if role == "student":
        return student_enrolled_in_course(g.user["id"], course_id)
    return False


def require_course_access(course_id: int, *, for_roles=None):
    """Abort if current user cannot access this course (admin always allowed)."""
    if not g.user:
        abort(403)
    if for_roles and g.user["role"] not in for_roles and g.user["role"] != "admin":
        abort(403)
    if g.user["role"] == "admin":
        return
    if not user_can_access_course(course_id):
        abort(403)


def assert_student_week(week_id: int):
    """Return (course, week) only if week belongs to student's enrolled course."""
    course = student_course(g.user["id"])
    week = query_one(
        """
        SELECT w.*, c.title AS course_title, c.id AS course_id
        FROM weeks w
        JOIN courses c ON c.id = w.course_id
        WHERE w.id = ? AND w.is_published = 1 AND c.is_active = 1
        """,
        (week_id,),
    )
    if not course or not week or week["course_id"] != course["id"]:
        abort(404)
    return course, week


def assert_staff_course(course_id: int):
    """Teacher must be assigned; admin always allowed."""
    course = query_one("SELECT * FROM courses WHERE id = ?", (course_id,))
    if not course:
        abort(404)
    if g.user["role"] == "admin":
        return course
    if g.user["role"] != "teacher" or not teacher_teaches_course(
        g.user["id"], course_id
    ):
        abort(403)
    return course


def assert_staff_week(week_id: int):
    week = query_one(
        """
        SELECT w.*, c.title AS course_title, c.id AS course_id
        FROM weeks w JOIN courses c ON c.id = w.course_id
        WHERE w.id = ?
        """,
        (week_id,),
    )
    if not week:
        abort(404)
    assert_staff_course(week["course_id"])
    return week


def week_progress(student_id: int, course_id: int):
    weeks = query_all(
        "SELECT * FROM weeks WHERE course_id = ? AND is_published = 1 ORDER BY week_number",
        (course_id,),
    )
    done = query_all(
        """
        SELECT a.week_id FROM assessments a
        JOIN weeks w ON w.id = a.week_id
        WHERE a.student_id = ? AND w.course_id = ?
        """,
        (student_id, course_id),
    )
    done_ids = {r["week_id"] for r in done}
    return weeks, done_ids


def course_complete(student_id: int, course_id: int) -> bool:
    weeks, done_ids = week_progress(student_id, course_id)
    if not weeks:
        return False
    return all(w["id"] in done_ids for w in weeks)


def register_routes(app: Flask):
    # ── Public ──────────────────────────────────────────────
    @app.route("/")
    def home():
        if g.user:
            return redirect(url_for("dashboard"))
        courses = query_all(
            "SELECT * FROM courses WHERE is_active = 1 ORDER BY title"
        )
        from db import CATEGORY_LABELS, COURSE_IMAGES

        return render_template(
            "home.html",
            courses=courses,
            course_images=COURSE_IMAGES,
            category_labels=CATEGORY_LABELS,
        )

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if g.user:
            return redirect(url_for("dashboard"))
        courses = query_all(
            "SELECT * FROM courses WHERE is_active = 1 ORDER BY title"
        )
        selected_course = request.args.get("course") or request.form.get("course_id")
        if request.method == "POST":
            name = (request.form.get("full_name") or "").strip()
            email = (request.form.get("email") or "").strip().lower()
            password = request.form.get("password") or ""
            course_id = request.form.get("course_id")

            if not name or not email or len(password) < 6 or not course_id:
                flash("Fill all fields. Password must be at least 6 characters.", "error")
                return render_template(
                    "register.html", courses=courses, selected_course=course_id
                )

            course = query_one(
                "SELECT * FROM courses WHERE id = ? AND is_active = 1", (course_id,)
            )
            if not course:
                flash("Choose a valid course.", "error")
                return render_template(
                    "register.html", courses=courses, selected_course=selected_course
                )

            if query_one("SELECT id FROM users WHERE email = ?", (email,)):
                flash("That email is already registered. Sign in instead.", "error")
                return render_template(
                    "register.html", courses=courses, selected_course=course_id
                )

            cur = execute(
                """INSERT INTO users (full_name, email, password_hash, role, is_active, created_at)
                   VALUES (?,?,?,'student',1,?)""",
                (name, email, generate_password_hash(password), now_iso()),
            )
            user_id = cur.lastrowid
            execute(
                "INSERT INTO enrollments (user_id, course_id, enrolled_at) VALUES (?,?,?)",
                (user_id, course["id"], now_iso()),
            )
            session["user_id"] = user_id
            flash(f"Welcome to CloudCity — you joined {course['title']}.", "ok")
            return redirect(url_for("student_home"))

        return render_template(
            "register.html", courses=courses, selected_course=selected_course
        )

    @app.route("/login", methods=["GET", "POST"])
    def login():
        return _login_view(staff_mode=False)

    @app.route("/staff", methods=["GET", "POST"])
    def staff_login():
        """Staff entry: admin & teacher dashboards after successful login."""
        return _login_view(staff_mode=True)

    def _login_view(staff_mode=False):
        if g.user:
            return redirect(url_for("dashboard"))
        if request.method == "POST":
            email = (request.form.get("email") or "").strip().lower()
            password = request.form.get("password") or ""
            user = query_one(
                "SELECT * FROM users WHERE email = ? AND is_active = 1", (email,)
            )
            if user and check_password_hash(user["password_hash"], password):
                if staff_mode and user["role"] == "student":
                    flash(
                        "That account is a student account. Use student sign in, or enrol as a student.",
                        "warn",
                    )
                    return render_template("login.html", staff=staff_mode)
                if not staff_mode and user["role"] in ("admin", "teacher"):
                    # Still allow staff on /login — send them to their dashboard
                    session["user_id"] = user["id"]
                    flash(f"Welcome back, {user['full_name'].split()[0]}.", "ok")
                    return redirect(url_for("dashboard"))
                session["user_id"] = user["id"]
                flash(f"Welcome back, {user['full_name'].split()[0]}.", "ok")
                nxt = request.args.get("next")
                if nxt:
                    return redirect(nxt)
                return redirect(url_for("dashboard"))
            flash(
                "Invalid email or password. Staff demo: admin@cloudcity.local / Admin123!",
                "error",
            )
        return render_template("login.html", staff=staff_mode)

    @app.route("/logout")
    def logout():
        session.clear()
        flash("Signed out.", "ok")
        return redirect(url_for("home"))

    @app.route("/dashboard")
    @login_required
    def dashboard():
        role = g.user["role"]
        if role == "admin":
            return redirect(url_for("admin_home"))
        if role == "teacher":
            return redirect(url_for("teacher_home"))
        return redirect(url_for("student_home"))

    # ── Student ─────────────────────────────────────────────
    @app.route("/student")
    @role_required("student")
    def student_home():
        course = student_course(g.user["id"])
        if not course:
            flash("You are not enrolled in an active course. Contact admin.", "warn")
            return render_template(
                "student/home.html", course=None, weeks=[], done_ids=set()
            )
        weeks, done_ids = week_progress(g.user["id"], course["id"])
        complete = course_complete(g.user["id"], course["id"])
        return render_template(
            "student/home.html",
            course=course,
            weeks=weeks,
            done_ids=done_ids,
            complete=complete,
        )

    @app.route("/student/week/<int:week_id>")
    @role_required("student")
    def student_week(week_id):
        course, week = assert_student_week(week_id)
        note = query_one(
            "SELECT * FROM notes WHERE week_id = ? ORDER BY updated_at DESC LIMIT 1",
            (week_id,),
        )
        assessment = query_one(
            "SELECT * FROM assessments WHERE student_id = ? AND week_id = ?",
            (g.user["id"], week_id),
        )
        return render_template(
            "student/week.html",
            course=course,
            week=week,
            note=note,
            assessment=assessment,
        )

    @app.route("/student/week/<int:week_id>/test", methods=["GET", "POST"])
    @role_required("student")
    def student_test(week_id):
        course, week = assert_student_week(week_id)

        existing = query_one(
            "SELECT * FROM assessments WHERE student_id = ? AND week_id = ?",
            (g.user["id"], week_id),
        )
        if existing:
            flash("You already submitted this week's assessment.", "warn")
            return redirect(url_for("student_result", week_id=week_id))

        questions = query_all(
            "SELECT * FROM questions WHERE week_id = ? ORDER BY sort_order, id",
            (week_id,),
        )
        if request.method == "POST":
            # Re-check enrolment before accepting answers
            if not student_enrolled_in_course(g.user["id"], course["id"]):
                abort(403)
            if not questions:
                flash("No questions yet for this week.", "warn")
                return redirect(url_for("student_week", week_id=week_id))

            score = 0.0
            max_score = float(sum(q["points"] for q in questions))
            cur = execute(
                """INSERT INTO assessments
                   (student_id, week_id, submitted_at, score, max_score, status)
                   VALUES (?,?,?,?,?,?)""",
                (g.user["id"], week_id, now_iso(), 0, max_score, "submitted"),
            )
            assessment_id = cur.lastrowid
            upload_dir = Path(app.config["UPLOAD_FOLDER"])

            for q in questions:
                qid = q["id"]
                text_answer = None
                selected = None
                is_correct = None
                points_awarded = 0.0

                if q["qtype"] == "mcq":
                    selected = (request.form.get(f"q_{qid}") or "").strip()
                    if selected and selected == (q["correct_option"] or ""):
                        is_correct = 1
                        points_awarded = float(q["points"])
                        score += points_awarded
                    else:
                        is_correct = 0
                elif q["qtype"] == "subjective":
                    text_answer = (request.form.get(f"q_{qid}") or "").strip()
                    # Teacher/admin can review later; partial credit not auto
                    points_awarded = 0.0
                elif q["qtype"] == "upload":
                    text_answer = (request.form.get(f"q_{qid}_note") or "").strip()

                acur = execute(
                    """INSERT INTO answers
                       (assessment_id, question_id, text_answer, selected_option,
                        is_correct, points_awarded)
                       VALUES (?,?,?,?,?,?)""",
                    (
                        assessment_id,
                        qid,
                        text_answer,
                        selected,
                        is_correct,
                        points_awarded,
                    ),
                )
                answer_id = acur.lastrowid

                if q["qtype"] == "upload":
                    f = request.files.get(f"q_{qid}_file")
                    if f and f.filename and allowed_file(f.filename):
                        ext = f.filename.rsplit(".", 1)[1].lower()
                        stored = f"{uuid.uuid4().hex}.{ext}"
                        f.save(upload_dir / stored)
                        execute(
                            """INSERT INTO uploads
                               (answer_id, stored_name, original_name, uploaded_at)
                               VALUES (?,?,?,?)""",
                            (answer_id, stored, secure_filename(f.filename), now_iso()),
                        )
                        # credit upload points if a file was provided
                        execute(
                            "UPDATE answers SET points_awarded = ?, is_correct = 1 WHERE id = ?",
                            (float(q["points"]), answer_id),
                        )
                        score += float(q["points"])

            # Recompute score including uploads
            total = query_one(
                "SELECT COALESCE(SUM(points_awarded),0) AS s FROM answers WHERE assessment_id = ?",
                (assessment_id,),
            )["s"]
            execute(
                "UPDATE assessments SET score = ? WHERE id = ?",
                (total, assessment_id),
            )
            flash("Assessment submitted.", "ok")
            return redirect(url_for("student_result", week_id=week_id))

        parsed = []
        for q in questions:
            opts = json.loads(q["options_json"]) if q["options_json"] else []
            parsed.append({**dict(q), "options": opts})

        return render_template(
            "student/test.html", course=course, week=week, questions=parsed
        )

    @app.route("/student/week/<int:week_id>/result")
    @role_required("student")
    def student_result(week_id):
        course, week = assert_student_week(week_id)
        assessment = query_one(
            "SELECT * FROM assessments WHERE student_id = ? AND week_id = ?",
            (g.user["id"], week_id),
        )
        if not assessment:
            abort(404)
        answers = query_all(
            """
            SELECT a.*, q.prompt, q.qtype, q.points, q.correct_option
            FROM answers a JOIN questions q ON q.id = a.question_id
            WHERE a.assessment_id = ?
            ORDER BY q.sort_order, q.id
            """,
            (assessment["id"],),
        )
        return render_template(
            "student/result.html",
            week=week,
            course=course,
            assessment=assessment,
            answers=answers,
        )

    @app.route("/student/certificate")
    @role_required("student")
    def student_certificate():
        course = student_course(g.user["id"])
        if not course or not course["certificate_issued_at"]:
            flash("Certificate not available yet.", "warn")
            return redirect(url_for("student_home"))
        return _send_certificate(
            g.user["full_name"],
            course["title"],
            course["certificate_issued_at"][:10],
        )

    # ── Teacher ─────────────────────────────────────────────
    @app.route("/teacher")
    @role_required("teacher", "admin")
    def teacher_home():
        if g.user["role"] == "admin":
            courses = query_all(
                "SELECT * FROM courses WHERE is_active = 1 ORDER BY title"
            )
        else:
            courses = query_all(
                """
                SELECT c.* FROM courses c
                JOIN teacher_courses tc ON tc.course_id = c.id
                WHERE tc.teacher_id = ? AND c.is_active = 1
                ORDER BY c.title
                """,
                (g.user["id"],),
            )
        return render_template("teacher/home.html", courses=courses)

    @app.route("/teacher/course/<int:course_id>")
    @role_required("teacher", "admin")
    def teacher_course(course_id):
        course = assert_staff_course(course_id)
        weeks = query_all(
            "SELECT * FROM weeks WHERE course_id = ? ORDER BY week_number",
            (course_id,),
        )
        return render_template("teacher/course.html", course=course, weeks=weeks)

    @app.route("/teacher/week/<int:week_id>", methods=["GET", "POST"])
    @role_required("teacher", "admin")
    def teacher_week(week_id):
        week = assert_staff_week(week_id)
        note = query_one(
            "SELECT * FROM notes WHERE week_id = ? ORDER BY updated_at DESC LIMIT 1",
            (week_id,),
        )

        if request.method == "POST":
            # Access already verified via assert_staff_week
            action = request.form.get("action")
            if action == "save_note":
                title = (request.form.get("title") or "").strip() or "Lesson notes"
                content = (request.form.get("content") or "").strip()
                examples = (request.form.get("examples") or "").strip()
                if note:
                    execute(
                        """UPDATE notes SET title=?, content=?, examples=?, teacher_id=?, updated_at=?
                           WHERE id=?""",
                        (title, content, examples, g.user["id"], now_iso(), note["id"]),
                    )
                else:
                    execute(
                        """INSERT INTO notes (week_id, teacher_id, title, content, examples, updated_at)
                           VALUES (?,?,?,?,?,?)""",
                        (week_id, g.user["id"], title, content, examples, now_iso()),
                    )
                flash("Notes saved.", "ok")
            elif action == "add_question":
                qtype = request.form.get("qtype")
                prompt = (request.form.get("prompt") or "").strip()
                points = int(request.form.get("points") or 1)
                if qtype not in ("mcq", "subjective", "upload") or not prompt:
                    flash("Invalid question.", "error")
                else:
                    options_json = None
                    correct = None
                    if qtype == "mcq":
                        opts = [
                            o.strip()
                            for o in (request.form.get("options") or "").split("\n")
                            if o.strip()
                        ]
                        correct = (request.form.get("correct_option") or "").strip()
                        options_json = json.dumps(opts)
                    max_order = query_one(
                        "SELECT COALESCE(MAX(sort_order),0) AS m FROM questions WHERE week_id=?",
                        (week_id,),
                    )["m"]
                    execute(
                        """INSERT INTO questions
                           (week_id, qtype, prompt, options_json, correct_option, points, sort_order)
                           VALUES (?,?,?,?,?,?,?)""",
                        (
                            week_id,
                            qtype,
                            prompt,
                            options_json,
                            correct,
                            points,
                            max_order + 1,
                        ),
                    )
                    flash("Question added.", "ok")
            elif action == "delete_question":
                qid = request.form.get("question_id")
                execute("DELETE FROM questions WHERE id = ? AND week_id = ?", (qid, week_id))
                flash("Question removed.", "ok")
            return redirect(url_for("teacher_week", week_id=week_id))

        note = query_one(
            "SELECT * FROM notes WHERE week_id = ? ORDER BY updated_at DESC LIMIT 1",
            (week_id,),
        )
        questions = query_all(
            "SELECT * FROM questions WHERE week_id = ? ORDER BY sort_order, id",
            (week_id,),
        )
        parsed = []
        for q in questions:
            parsed.append(
                {
                    **dict(q),
                    "options": json.loads(q["options_json"]) if q["options_json"] else [],
                }
            )
        return render_template(
            "teacher/week.html", week=week, note=note, questions=parsed
        )

    @app.route("/teacher/reviews")
    @role_required("teacher", "admin")
    def teacher_reviews():
        if g.user["role"] == "admin":
            rows = query_all(
                """
                SELECT a.*, u.full_name, w.week_number, w.title AS week_title, c.title AS course_title
                FROM assessments a
                JOIN users u ON u.id = a.student_id
                JOIN weeks w ON w.id = a.week_id
                JOIN courses c ON c.id = w.course_id
                ORDER BY a.submitted_at DESC
                LIMIT 200
                """
            )
        else:
            rows = query_all(
                """
                SELECT a.*, u.full_name, w.week_number, w.title AS week_title, c.title AS course_title
                FROM assessments a
                JOIN users u ON u.id = a.student_id
                JOIN weeks w ON w.id = a.week_id
                JOIN courses c ON c.id = w.course_id
                JOIN teacher_courses tc ON tc.course_id = c.id
                WHERE tc.teacher_id = ?
                ORDER BY a.submitted_at DESC
                LIMIT 200
                """,
                (g.user["id"],),
            )
        return render_template("teacher/reviews.html", assessments=rows)

    @app.route("/teacher/assessment/<int:assessment_id>", methods=["GET", "POST"])
    @role_required("teacher", "admin")
    def teacher_assessment(assessment_id):
        assessment = query_one(
            """
            SELECT a.*, u.full_name, w.week_number, w.title AS week_title,
                   c.title AS course_title, c.id AS course_id
            FROM assessments a
            JOIN users u ON u.id = a.student_id
            JOIN weeks w ON w.id = a.week_id
            JOIN courses c ON c.id = w.course_id
            WHERE a.id = ?
            """,
            (assessment_id,),
        )
        if not assessment:
            abort(404)
        # Teacher only for assigned courses; admin unrestricted
        assert_staff_course(assessment["course_id"])

        if request.method == "POST":
            for key, val in request.form.items():
                if key.startswith("points_"):
                    aid = int(key.split("_", 1)[1])
                    # Only update answers that belong to this assessment
                    owns = query_one(
                        "SELECT id FROM answers WHERE id = ? AND assessment_id = ?",
                        (aid, assessment_id),
                    )
                    if not owns:
                        continue
                    try:
                        pts = float(val)
                    except ValueError:
                        pts = 0
                    feedback = request.form.get(f"feedback_{aid}", "")
                    execute(
                        "UPDATE answers SET points_awarded = ?, teacher_feedback = ? WHERE id = ?",
                        (pts, feedback, aid),
                    )
            total = query_one(
                "SELECT COALESCE(SUM(points_awarded),0) AS s FROM answers WHERE assessment_id = ?",
                (assessment_id,),
            )["s"]
            execute(
                "UPDATE assessments SET score = ?, status = 'reviewed' WHERE id = ?",
                (total, assessment_id),
            )
            flash("Review saved.", "ok")
            return redirect(url_for("teacher_assessment", assessment_id=assessment_id))

        answers = query_all(
            """
            SELECT an.*, q.prompt, q.qtype, q.points AS max_points
            FROM answers an JOIN questions q ON q.id = an.question_id
            WHERE an.assessment_id = ?
            ORDER BY q.sort_order
            """,
            (assessment_id,),
        )
        uploads_map = {}
        for an in answers:
            up = query_one("SELECT * FROM uploads WHERE answer_id = ?", (an["id"],))
            if up:
                uploads_map[an["id"]] = up
        return render_template(
            "teacher/assessment.html",
            assessment=assessment,
            answers=answers,
            uploads_map=uploads_map,
        )

    # ── Admin ───────────────────────────────────────────────
    @app.route("/admin")
    @role_required("admin")
    def admin_home():
        stats = {
            "students": query_one(
                "SELECT COUNT(*) AS c FROM users WHERE role='student'"
            )["c"],
            "teachers": query_one(
                "SELECT COUNT(*) AS c FROM users WHERE role='teacher'"
            )["c"],
            "assessments": query_one("SELECT COUNT(*) AS c FROM assessments")["c"],
            "certs": query_one(
                "SELECT COUNT(*) AS c FROM enrollments WHERE certificate_issued_at IS NOT NULL"
            )["c"],
        }
        recent = query_all(
            """
            SELECT a.submitted_at, a.score, a.max_score, u.full_name, w.week_number, c.title AS course_title
            FROM assessments a
            JOIN users u ON u.id = a.student_id
            JOIN weeks w ON w.id = a.week_id
            JOIN courses c ON c.id = w.course_id
            ORDER BY a.submitted_at DESC
            LIMIT 12
            """
        )
        return render_template("admin/home.html", stats=stats, recent=recent)

    @app.route("/admin/users", methods=["GET", "POST"])
    @role_required("admin")
    def admin_users():
        if request.method == "POST":
            action = request.form.get("action")
            if action == "add_teacher":
                name = (request.form.get("full_name") or "").strip()
                email = (request.form.get("email") or "").strip().lower()
                password = request.form.get("password") or "Teacher123!"
                course_ids = request.form.getlist("course_ids")
                if name and email:
                    if query_one("SELECT id FROM users WHERE email = ?", (email,)):
                        flash("Email already exists.", "error")
                    else:
                        cur = execute(
                            """INSERT INTO users (full_name, email, password_hash, role, is_active, created_at)
                               VALUES (?,?,?,'teacher',1,?)""",
                            (name, email, generate_password_hash(password), now_iso()),
                        )
                        tid = cur.lastrowid
                        for cid in course_ids:
                            execute(
                                "INSERT OR IGNORE INTO teacher_courses (teacher_id, course_id) VALUES (?,?)",
                                (tid, cid),
                            )
                        flash("Teacher created with assigned courses.", "ok")
            elif action == "assign_courses":
                tid = request.form.get("teacher_id")
                teacher = query_one(
                    "SELECT id FROM users WHERE id = ? AND role = 'teacher'", (tid,)
                )
                if teacher:
                    course_ids = request.form.getlist("course_ids")
                    execute(
                        "DELETE FROM teacher_courses WHERE teacher_id = ?",
                        (teacher["id"],),
                    )
                    for cid in course_ids:
                        c = query_one("SELECT id FROM courses WHERE id = ?", (cid,))
                        if c:
                            execute(
                                "INSERT INTO teacher_courses (teacher_id, course_id) VALUES (?,?)",
                                (teacher["id"], c["id"]),
                            )
                    flash("Teacher course assignments updated.", "ok")
            elif action == "change_student_course":
                sid = request.form.get("student_id")
                course_id = request.form.get("course_id")
                student = query_one(
                    "SELECT id FROM users WHERE id = ? AND role = 'student'", (sid,)
                )
                course = query_one(
                    "SELECT id, title FROM courses WHERE id = ? AND is_active = 1",
                    (course_id,),
                )
                if student and course:
                    existing = query_one(
                        "SELECT id FROM enrollments WHERE user_id = ?",
                        (student["id"],),
                    )
                    if existing:
                        execute(
                            "UPDATE enrollments SET course_id = ?, enrolled_at = ? WHERE id = ?",
                            (course["id"], now_iso(), existing["id"]),
                        )
                    else:
                        execute(
                            "INSERT INTO enrollments (user_id, course_id, enrolled_at) VALUES (?,?,?)",
                            (student["id"], course["id"], now_iso()),
                        )
                    flash(f"Student moved to {course['title']}.", "ok")
            elif action == "toggle":
                uid = request.form.get("user_id")
                if str(uid) != str(g.user["id"]):
                    u = query_one("SELECT is_active FROM users WHERE id = ?", (uid,))
                    if u:
                        execute(
                            "UPDATE users SET is_active = ? WHERE id = ?",
                            (0 if u["is_active"] else 1, uid),
                        )
                        flash("User updated.", "ok")
            return redirect(url_for("admin_users"))

        users = query_all(
            """
            SELECT u.*,
              (SELECT c.title FROM enrollments e JOIN courses c ON c.id = e.course_id
               WHERE e.user_id = u.id LIMIT 1) AS course_title
            FROM users u
            ORDER BY u.role, u.full_name
            """
        )
        courses = query_all(
            "SELECT * FROM courses WHERE is_active = 1 ORDER BY title"
        )
        teachers = [u for u in users if u["role"] == "teacher"]
        teacher_assign = {}
        for t in teachers:
            rows = query_all(
                "SELECT course_id FROM teacher_courses WHERE teacher_id = ?",
                (t["id"],),
            )
            teacher_assign[t["id"]] = {r["course_id"] for r in rows}
        students = [u for u in users if u["role"] == "student"]
        return render_template(
            "admin/users.html",
            users=users,
            courses=courses,
            teachers=teachers,
            teacher_assign=teacher_assign,
            students=students,
        )

    @app.route("/admin/assessments")
    @role_required("admin")
    def admin_assessments():
        course_id = request.args.get("course_id")
        sql = """
            SELECT a.*, u.full_name, u.email, w.week_number, w.title AS week_title,
                   c.title AS course_title, c.id AS course_id
            FROM assessments a
            JOIN users u ON u.id = a.student_id
            JOIN weeks w ON w.id = a.week_id
            JOIN courses c ON c.id = w.course_id
        """
        params = ()
        if course_id:
            sql += " WHERE c.id = ?"
            params = (course_id,)
        sql += " ORDER BY a.submitted_at DESC"
        rows = query_all(sql, params)
        courses = query_all("SELECT * FROM courses ORDER BY title")
        return render_template(
            "admin/assessments.html",
            assessments=rows,
            courses=courses,
            selected_course=course_id,
        )

    @app.route("/admin/certificates", methods=["GET", "POST"])
    @role_required("admin")
    def admin_certificates():
        if request.method == "POST":
            enrollment_id = request.form.get("enrollment_id")
            action = request.form.get("action")
            enr = query_one(
                """
                SELECT e.*, u.full_name, c.title AS course_title, e.user_id, e.course_id
                FROM enrollments e
                JOIN users u ON u.id = e.user_id
                JOIN courses c ON c.id = e.course_id
                WHERE e.id = ?
                """,
                (enrollment_id,),
            )
            if not enr:
                flash("Enrollment not found.", "error")
                return redirect(url_for("admin_certificates"))

            if action == "issue":
                if not course_complete(enr["user_id"], enr["course_id"]):
                    flash(
                        f"{enr['full_name']} has not completed all weeks yet.",
                        "error",
                    )
                else:
                    execute(
                        "UPDATE enrollments SET certificate_issued_at = ? WHERE id = ?",
                        (now_iso(), enrollment_id),
                    )
                    flash(f"Certificate issued for {enr['full_name']}.", "ok")
            elif action == "download":
                issued = enr["certificate_issued_at"] or now_iso()
                return _send_certificate(
                    enr["full_name"], enr["course_title"], issued[:10]
                )
            return redirect(url_for("admin_certificates"))

        rows = query_all(
            """
            SELECT e.*, u.full_name, u.email, c.title AS course_title, c.id AS course_id
            FROM enrollments e
            JOIN users u ON u.id = e.user_id
            JOIN courses c ON c.id = e.course_id
            WHERE u.role = 'student'
            ORDER BY c.title, u.full_name
            """
        )
        enriched = []
        for r in rows:
            weeks, done = week_progress(r["user_id"], r["course_id"])
            enriched.append(
                {
                    **dict(r),
                    "weeks_total": len(weeks),
                    "weeks_done": len(done),
                    "complete": bool(weeks) and len(done) == len(weeks),
                }
            )
        return render_template("admin/certificates.html", enrollments=enriched)

    @app.errorhandler(403)
    def forbidden(_e):
        return render_template("error.html", code=403, message="Access denied."), 403

    @app.errorhandler(404)
    def not_found(_e):
        return render_template("error.html", code=404, message="Page not found."), 404

    def _send_certificate(student_name, course_title, issued_date):
        pdf = build_certificate_pdf(
            academy_name=app.config["ACADEMY_NAME"],
            student_name=student_name,
            course_title=course_title,
            issued_date=issued_date,
        )
        name = secure_filename(f"{student_name}-certificate.pdf") or "certificate.pdf"
        path = Path(app.config["UPLOAD_FOLDER"]) / f"cert_{uuid.uuid4().hex}.pdf"
        path.write_bytes(pdf)
        return send_file(
            path,
            mimetype="application/pdf",
            as_attachment=True,
            download_name=name,
        )


app = create_app()

if __name__ == "__main__":
    # Local free development server
    app.run(debug=True, port=5000)
