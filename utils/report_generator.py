"""
===========================================================
Report Generator
ResearchMind AI
===========================================================
"""

import os

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


def generate_report(
    title,
    summary,
    keywords,
    statistics
):

    os.makedirs("reports", exist_ok=True)

    pdf_path = os.path.join(
        "reports",
        "Research_Report.pdf"
    )

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>ResearchMind AI Report</b>", styles["Title"]))
    story.append(Spacer(1, 20))

    story.append(Paragraph(f"<b>Paper:</b> {title}", styles["Heading2"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Summary</b>", styles["Heading2"]))

    for sentence in summary:
        story.append(
            Paragraph(sentence, styles["BodyText"])
        )

    story.append(Spacer(1, 20))

    story.append(Paragraph("<b>Keywords</b>", styles["Heading2"]))

    story.append(
        Paragraph(
            ", ".join([k for k, s in keywords]),
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(Paragraph("<b>Statistics</b>", styles["Heading2"]))

    for key, value in statistics.items():

        story.append(
            Paragraph(
                f"{key}: {value}",
                styles["BodyText"]
            )
        )

    doc.build(story)

    return pdf_path
