"""Send plain-text email via free SMTP (e.g. Gmail app password)."""
from __future__ import annotations

import smtplib
import ssl
from email.message import EmailMessage
from typing import Optional

from flask import current_app


def email_configured() -> bool:
    cfg = current_app.config
    return bool(
        cfg.get("ADMIN_NOTIFY_EMAIL")
        and cfg.get("SMTP_USER")
        and cfg.get("SMTP_PASSWORD")
    )


def send_plain_email(
    subject: str,
    body: str,
    to_addr: Optional[str] = None,
) -> tuple[bool, str]:
    """
    Returns (ok, message). Never raises — callers can still keep a DB record.
    """
    cfg = current_app.config
    to_addr = (to_addr or cfg.get("ADMIN_NOTIFY_EMAIL") or "").strip()
    user = (cfg.get("SMTP_USER") or "").strip()
    password = (cfg.get("SMTP_PASSWORD") or "").strip()
    host = (cfg.get("SMTP_HOST") or "smtp.gmail.com").strip()
    port = int(cfg.get("SMTP_PORT") or 587)
    from_addr = (cfg.get("SMTP_FROM") or user or "noreply@cloudcity.local").strip()
    use_tls = cfg.get("SMTP_USE_TLS", True)

    if not to_addr:
        return False, "ADMIN_NOTIFY_EMAIL is not set"
    if not user or not password:
        return False, "SMTP username/password not set"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.set_content(body)

    try:
        with smtplib.SMTP(host, port, timeout=25) as smtp:
            smtp.ehlo()
            if use_tls:
                smtp.starttls(context=ssl.create_default_context())
                smtp.ehlo()
            smtp.login(user, password)
            smtp.send_message(msg)
        return True, "sent"
    except Exception as exc:  # noqa: BLE001 — surface SMTP issues to caller
        return False, str(exc)
