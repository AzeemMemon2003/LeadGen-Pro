from exporter.excel import ExcelExporter


class ExportManager:

    def __init__(self):

        self.excel = ExcelExporter()

    def add(self, result):

        self.excel.add(

            result["company"],

            result["website"],

            result["title"],

            result["emails"],

            result["phones"],

            result["addresses"],

            result["technology"],

            result["social"],

            result["crawl_pages"],

            result["website_intelligence"]

        )

    def save(self):

        self.excel.save()