import os

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from utils.constants import (
    ALLOWED_EXTENSIONS,
    REPORT_FOLDER
)


def allowed_file(filename):
    """
    Check whether uploaded file is PDF.
    """

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def generate_report(
    filename,
    ats_score,
    similarity,
    skills,
    missing_skills,
    recommendation
):
    """
    Generate a PDF report for one resume.
    """

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    report_name = (
        os.path.splitext(filename)[0]
        + "_report.pdf"
    )

    report_path = os.path.join(
        REPORT_FOLDER,
        report_name
    )

    doc = SimpleDocTemplate(report_path)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>AI Resume Screening Report</b>", styles["Title"])
    )

    elements.append(
        Paragraph(f"<b>Resume:</b> {filename}", styles["Normal"])
    )

    elements.append(
        Paragraph(f"<b>ATS Score:</b> {ats_score}%", styles["Normal"])
    )

    elements.append(
        Paragraph(f"<b>Match Percentage:</b> {similarity}%", styles["Normal"])
    )

    elements.append(
        Paragraph(
            f"<b>Skills:</b> {', '.join(skills) if skills else 'None'}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Missing Skills:</b> {', '.join(missing_skills) if missing_skills else 'None'}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Recommendation:</b> {recommendation}",
            styles["Normal"]
        )
    )

    doc.build(elements)

    return report_path