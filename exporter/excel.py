from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter


class ExcelExporter:

    def __init__(self):

        self.workbook = Workbook()

        self.sheet = self.workbook.active

        self.sheet.title = "LeadGen Pro"

        headers = [
            "Company",
            "Website",
            "Title",
            "Emails",
            "Phones",
            "Addresses",
            "Technology",
            "LinkedIn",
            "Facebook",
            "Instagram",
            "Twitter",
            "Contact Pages"
        ]

        self.sheet.append(headers)

        header_fill = PatternFill(
            fill_type="solid",
            fgColor="1F4E78"
        )

        header_font = Font(
            bold=True,
            color="FFFFFF"
        )

        for cell in self.sheet[1]:

            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(
                horizontal="center",
                vertical="center"
            )

        self.sheet.freeze_panes = "A2"

        self.sheet.auto_filter.ref = "A1:L1"

    def add(
        self,
        company,
        website,
        title,
        emails,
        phones,
        addresses,
        technology,
        social,
        contacts
    ):

        self.sheet.append([

            company,

            website,

            title,

            ", ".join(emails),

            ", ".join(phones),

            ", ".join(addresses),

            ", ".join(technology),

            social["linkedin"],

            social["facebook"],

            social["instagram"],

            social["twitter"],

            ", ".join(contacts)

        ])

    def save(self):

        for column in self.sheet.columns:

            max_length = 0

            column_letter = get_column_letter(
                column[0].column
            )

            for cell in column:

                try:

                    if cell.value:

                        max_length = max(
                            max_length,
                            len(str(cell.value))
                        )

                except:
                    pass

            adjusted_width = min(max_length + 3, 60)

            self.sheet.column_dimensions[
                column_letter
            ].width = adjusted_width

        self.workbook.save(
            "output/leads.xlsx"
        )