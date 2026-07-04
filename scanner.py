from scraper.browser import Browser

from exporter.excel import ExcelExporter

from search.manager import SearchManager

from services.scan_service import ScanService
from services.report_service import ReportService

from utils.logger import Logger


class Scanner:

    def run(self):

        manager = SearchManager()

        websites = manager.menu()

        if not websites:

            print("\nNo websites found.")

            return

        browser = Browser()

        browser.start()

        logger = Logger.get_logger()

        logger.info("LeadGen Pro Started")

        excel = ExcelExporter()

        total = len(websites)

        for index, website in enumerate(websites):

            print("\n" + "=" * 60)
            print(f"[{index + 1}/{total}] {website}")
            print("=" * 60)

            logger.info(f"Scanning: {website}")

            try:

                result = ScanService.scan(
                    browser,
                    website
                )

                excel.add(
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

                ReportService.print(result)

                logger.info(
                    f"{result['company']} | Emails:{len(result['emails'])} | Phones:{len(result['phones'])}"
                )

            except Exception as e:

                logger.error(f"{website} | {e}")

                print(f"❌ {e}")

        browser.stop()

        excel.save()

        logger.info("Scan Finished")

        print("\n" + "=" * 60)
        print("✅ Scan Finished")
        print("📄 Excel saved to output/leads.xlsx")
        print("=" * 60)