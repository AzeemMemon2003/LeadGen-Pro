from scraper.browser import Browser

from search.manager import SearchManager

from services.scan_service import ScanService
from services.report_service import ReportService

from database.repository import LeadRepository

from exporter.manager import ExportManager

from campaign.builder import CampaignBuilder
from campaign.exporter import CampaignExporter

from proposal.manager import ProposalManager

from integration.manager import IntegrationManager

from utils.logger import Logger


class Scanner:

    def run(self):

        manager = SearchManager()

        websites = manager.menu()

        if not websites:

            print("\n❌ No websites found.")

            return

        browser = Browser()
        browser.start()

        logger = Logger.get_logger()

        repo = LeadRepository()

        exporter = ExportManager()

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

                # -----------------------------
                # Database
                # -----------------------------

                repo.save(result)

                # -----------------------------
                # Proposal PDF
                # -----------------------------

                proposal = ProposalManager.generate(
                    result
                )

                print(
                    f"\n📄 Proposal Generated : {proposal}"
                )

                # -----------------------------
                # n8n Payload / Webhook
                # -----------------------------

                payload, response = IntegrationManager.send(

                    result,

                    proposal

                )

                if response["success"]:

                    print("✅ n8n Webhook Sent")

                else:

                    print(f"⚠ {response['message']}")

                # -----------------------------
                # Excel
                # -----------------------------

                exporter.add(result)

                # -----------------------------
                # Console Report
                # -----------------------------

                ReportService.print(result)

                logger.info(
                    f"Saved: {result['company']}"
                )

            except Exception as e:

                logger.error(str(e))

                print(f"\n❌ {website}")

                print(e)

        browser.stop()

        # -----------------------------
        # Save Excel
        # -----------------------------

        exporter.save()

        # -----------------------------
        # Campaign Builder
        # -----------------------------

        leads = repo.all()

        builder = CampaignBuilder(
            leads
        )

        campaigns = builder.build()

        CampaignExporter().export(
            campaigns
        )

        builder.stats(
            campaigns
        )

        print("\n" + "=" * 70)
        print("✅ Scan Complete")
        print("📄 Proposal PDFs Generated")
        print("🔗 n8n Integration Completed")
        print("📄 Excel Updated")
        print("📢 Campaigns Generated")
        print("🗄 Database Updated")
        print("=" * 70)