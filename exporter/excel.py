from openpyxl import Workbook


class ExcelExporter:

    def __init__(self):

        self.workbook = Workbook()

        self.sheet = self.workbook.active

        self.sheet.append([
            "Company",
            "Website",
            "Title",
            "Emails",
            "Phones",
            "Addresses",
            "LinkedIn",
            "Facebook",
            "Instagram",
            "Twitter",
            "Contact Pages"
        ])

    def add(
        self,
        company,
        website,
        title,
        emails,
        phones,
        addresses,
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
            social["linkedin"],
            social["facebook"],
            social["instagram"],
            social["twitter"],
            ", ".join(contacts)
        ])

    def save(self):

        self.workbook.save("output/leads.xlsx")