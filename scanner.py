from scraper.browser import Browser

from exporter.excel import ExcelExporter
from search.manager import SearchManager

from services.scan_service import ScanService
from services.report_service import ReportService

from database.repository import LeadRepository

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

        repo = LeadRepository()

        excel = ExcelExporter()

        total = len(websites)

        print(f"\n🚀 Starting scan of {total} websites...\n")

        for index, website in enumerate(websites):

            print("=" * 70)
            print(f"[{index + 1}/{total}] {website}")
            print("=" * 70)

            try:

                result = ScanService.scan(
                    browser,
                    website
                )

                # Save to Database
                repo.save(result)

                # Save to Excel
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
                    f"Saved: {result['company']}"
                )

            except Exception as e:

                logger.error(str(e))

                print(f"\n❌ {website}")
                print(e)

        browser.stop()

        excel.save()

        print("\n" + "=" * 70)
        print("✅ Scan Complete")
        print("📄 Excel Updated")
        print("🗄 Database Updated")
        print("=" * 70)