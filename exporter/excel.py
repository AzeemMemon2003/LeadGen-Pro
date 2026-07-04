from openpyxl import Workbook


class ExcelExporter:

    def __init__(self):

        self.workbook = Workbook()
        self.sheet = self.workbook.active

        self.sheet.append([
            "Website",
            "Title",
            "Emails",
            "Contact Pages"
        ])

    def add(self, website, title, emails, contacts):

        self.sheet.append([
            website,
            title,
            ", ".join(emails),
            ", ".join(contacts)
        ])

    def save(self):

        self.workbook.save("output/leads.xlsx")