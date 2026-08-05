"""End-of-course PDF certificates — free via reportlab (no paid PDF API)."""
from io import BytesIO

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


INK = HexColor("#0F2438")
TEAL = HexColor("#1F6F78")
GOLD = HexColor("#B88A3B")
PAPER = HexColor("#F7F1E8")


def build_certificate_pdf(
    *,
    academy_name: str,
    student_name: str,
    course_title: str,
    issued_date: str,
) -> bytes:
    buffer = BytesIO()
    width, height = landscape(A4)
    c = canvas.Canvas(buffer, pagesize=landscape(A4))

    # Paper background
    c.setFillColor(PAPER)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Outer frame
    c.setStrokeColor(INK)
    c.setLineWidth(2)
    c.rect(12 * mm, 12 * mm, width - 24 * mm, height - 24 * mm, fill=0, stroke=1)

    c.setStrokeColor(TEAL)
    c.setLineWidth(0.8)
    c.rect(16 * mm, 16 * mm, width - 32 * mm, height - 32 * mm, fill=0, stroke=1)

    # Brand
    c.setFillColor(TEAL)
    c.setFont("Times-Bold", 14)
    c.drawCentredString(width / 2, height - 38 * mm, academy_name.upper())

    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    c.line(width / 2 - 45 * mm, height - 42 * mm, width / 2 + 45 * mm, height - 42 * mm)

    c.setFillColor(INK)
    c.setFont("Times-Roman", 12)
    c.drawCentredString(width / 2, height - 55 * mm, "Certificate of Completion")

    c.setFont("Times-Italic", 11)
    c.setFillColor(Color(0.2, 0.25, 0.3))
    c.drawCentredString(width / 2, height - 70 * mm, "This certifies that")

    c.setFillColor(INK)
    c.setFont("Times-Bold", 28)
    c.drawCentredString(width / 2, height - 90 * mm, student_name)

    c.setFont("Times-Roman", 12)
    c.setFillColor(Color(0.2, 0.25, 0.3))
    c.drawCentredString(
        width / 2,
        height - 108 * mm,
        "has successfully completed the course",
    )

    c.setFillColor(TEAL)
    c.setFont("Times-Bold", 16)
    c.drawCentredString(width / 2, height - 122 * mm, course_title)

    c.setFillColor(INK)
    c.setFont("Times-Roman", 11)
    c.drawCentredString(width / 2, height - 145 * mm, f"Issued on {issued_date}")

    c.setStrokeColor(INK)
    c.setLineWidth(0.6)
    c.line(45 * mm, 35 * mm, 95 * mm, 35 * mm)
    c.line(width - 95 * mm, 35 * mm, width - 45 * mm, 35 * mm)

    c.setFont("Times-Roman", 9)
    c.drawCentredString(70 * mm, 28 * mm, "Academy Director")
    c.drawCentredString(width - 70 * mm, 28 * mm, "CloudCity Seal")

    c.setFont("Times-Italic", 8)
    c.setFillColor(Color(0.35, 0.38, 0.42))
    c.drawCentredString(
        width / 2,
        18 * mm,
        "CloudCity Academy — Python learning for beginners and advanced learners",
    )

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.read()
