from exporter.excel import ExcelExporter


class ExportManager:

    def __init__(self):

        self.excel = ExcelExporter()

        # Future exporters
        # self.json = JSONExporter()
        # self.hubspot = HubSpotExporter()

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
            result["crawl_pages"]
        )

        # Future
        # self.json.add(result)
        # self.hubspot.add(result)

    def save(self):

        self.excel.save()

        # Future
        # self.json.save()