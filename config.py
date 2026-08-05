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

    # Academy brand (public free URL when deployed)
    ACADEMY_NAME = "CloudCity Academy"
    PUBLIC_HOST = "cloudcity.pythonanywhere.com"
