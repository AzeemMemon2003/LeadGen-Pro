import pandas as pd

from scraper.browser import Browser
from scraper.company import CompanyExtractor
from scraper.email import EmailExtractor
from scraper.phone import PhoneExtractor
from scraper.address import AddressExtractor
from scraper.crawler import SmartCrawler
from scraper.tech import TechExtractor
from scraper.seo import SEOExtractor

from exporter.excel import ExcelExporter
from search.manager import SearchManager


class Scanner:

    def run(self):

        print("\nSelect Input Mode")
        print("1. CSV File")
        print("2. Keyword Search")

        choice = input("\nChoice (1/2): ").strip()

        manager = SearchManager()

        if choice == "2":
            websites = manager.by_keyword()
        else:
            websites = manager.from_csv()

        if not websites:
            print("No websites found.")
            return

        browser = Browser()
        browser.start()

        excel = ExcelExporter()

        total = len(websites)

        for index, website in enumerate(websites):

            print("\n" + "=" * 60)
            print(f"[{index + 1}/{total}] {website}")
            print("=" * 60)

            try:

                page = browser.open(website)

                html = page.content()

                title = page.title()

                company = CompanyExtractor.extract(page, html)

                emails = EmailExtractor.extract(html)

                phones = PhoneExtractor.extract(html)

                addresses = AddressExtractor.extract(html)

                technology = TechExtractor.extract(html)

                seo = SEOExtractor.extract(html)

                crawl_pages = SmartCrawler.extract(
                    website,
                    html
                )

                print(f"🕷 Crawling {len(crawl_pages)} pages...")

                for url in crawl_pages:

                    try:

                        crawl_page = browser.open(url)

                        crawl_html = crawl_page.content()

                        emails.extend(
                            EmailExtractor.extract(crawl_html)
                        )

                        phones.extend(
                            PhoneExtractor.extract(crawl_html)
                        )

                        addresses.extend(
                            AddressExtractor.extract(crawl_html)
                        )

                    except Exception:
                        pass

                emails = sorted(set(emails))
                phones = sorted(set(phones))
                addresses = sorted(set(addresses))

                social = {
                    "linkedin": "",
                    "facebook": "",
                    "instagram": "",
                    "twitter": ""
                }

                excel.add(
                    company,
                    website,
                    title,
                    emails,
                    phones,
                    addresses,
                    technology,
                    social,
                    crawl_pages
                )

                print(f"🏢 Company : {company}")
                print(f"📧 Emails  : {len(emails)}")
                print(f"📞 Phones  : {len(phones)}")
                print(f"📍 Address : {len(addresses)}")
                print(f"💻 Tech    : {', '.join(technology)}")

                print("\n📊 SEO Audit")

                print(f"Title             : {'✅' if seo['title'] else '❌'}")
                print(f"Meta Description  : {'✅' if seo['meta_description'] else '❌'}")
                print(f"H1                : {'✅' if seo['h1'] else '❌'}")
                print(f"Images without ALT: {seo['images_without_alt']}")

            except Exception as e:

                print(f"❌ {e}")

        browser.stop()

        excel.save()

        print("\n" + "=" * 60)
        print("✅ Scan Finished")
        print("📄 Excel saved to output/leads.xlsx")
        print("=" * 60)