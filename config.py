"""Free-only configuration. No paid services or API keys required."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    # Local secret only — change on PythonAnywhere if you share the account
    SECRET_KEY = os.environ.get("CLOUFCITY_SECRET", "cloudcity-dev-change-me-on-deploy")

    # Free, local SQLite — no cloud database bill
    SQLALCHEMY_DATABASE_URI = None  # we use stdlib sqlite3
    DATABASE_PATH = BASE_DIR / "instance" / "cloudcity.db"

    # Free local disk storage for screenshots (PythonAnywhere free includes disk)
    UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"
    MAX_CONTENT_LENGTH = 4 * 1024 * 1024  # 4 MB
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}

    # Sessions for many concurrent logins
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = 60 * 60 * 12  # 12 hours

    # End-of-course certificate: all weeks submitted + overall score >= this %
    CERTIFICATE_PASS_PERCENT = float(os.environ.get("CLOUDCITY_CERT_PASS", "75"))

    # Academy brand (public free URL when deployed)
    ACADEMY_NAME = "CloudCity Academy"
    PUBLIC_HOST = "cloudcity.pythonanywhere.com"

    # Email notifications for new student applications (free: Gmail app password or similar)
    # On PythonAnywhere set these in Web → WSGI file or Bash:
    #   export CLOUDCITY_ADMIN_EMAIL='you@gmail.com'
    #   export CLOUDCITY_SMTP_USER='you@gmail.com'
    #   export CLOUDCITY_SMTP_PASSWORD='your-app-password'
    ADMIN_NOTIFY_EMAIL = os.environ.get("CLOUDCITY_ADMIN_EMAIL", "").strip()
    SMTP_HOST = os.environ.get("CLOUDCITY_SMTP_HOST", "smtp.gmail.com").strip()
    SMTP_PORT = int(os.environ.get("CLOUDCITY_SMTP_PORT", "587"))
    SMTP_USER = os.environ.get("CLOUDCITY_SMTP_USER", "").strip()
    SMTP_PASSWORD = os.environ.get("CLOUDCITY_SMTP_PASSWORD", "").strip()
    SMTP_FROM = os.environ.get("CLOUDCITY_SMTP_FROM", SMTP_USER or "noreply@cloudcity.local").strip()
    SMTP_USE_TLS = os.environ.get("CLOUDCITY_SMTP_TLS", "1") != "0"
