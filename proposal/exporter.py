from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph

from config.settings import Settings


class ProposalExporter:

    @staticmethod
    def export(company, text):

        output = Settings.OUTPUT_DIR / "proposals"

        output.mkdir(
            parents=True,
            exist_ok=True
        )

        filename = (
            company
            .replace("/", "")
            .replace("\\", "")
            .replace(":", "")
            .replace("*", "")
            .replace("?", "")
            .replace('"', "")
            .replace("<", "")
            .replace(">", "")
            .replace("|", "")
            .strip()
        )

        pdf = output / f"{filename}.pdf"

        styles = getSampleStyleSheet()

        document = SimpleDocTemplate(
            str(pdf)
        )

        story = []

        for line in text.split("\n"):

            story.append(
                Paragraph(
                    line.replace("\n", "<br/>"),
                    styles["BodyText"]
                )
            )

        document.build(story)

        return pdf