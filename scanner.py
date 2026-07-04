import pandas as pd

from scraper.browser import Browser
from scraper.company import CompanyExtractor
from scraper.email import EmailExtractor
from scraper.phone import PhoneExtractor
from scraper.crawler import SmartCrawler
from scraper.address import AddressExtractor
from exporter.excel import ExcelExporter


class Scanner:

    def run(self):

        browser = Browser()
        browser.start()

        excel = ExcelExporter()

        df = pd.read_csv("input/websites.csv")

        total = len(df)

        for index, row in df.iterrows():

            website = row["website"]

            print("\n" + "=" * 60)
            print(f"[{index + 1}/{total}] {website}")
            print("=" * 60)

            try:

                # Homepage
                page = browser.open(website)

                html = page.content()

                title = page.title()

                company = CompanyExtractor.extract(page, html)

                emails = EmailExtractor.extract(html)

                phones = PhoneExtractor.extract(html)

                addresses = AddressExtractor.extract(html)

                # Crawl important pages
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

                # Remove duplicates
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
                    social,
                    crawl_pages
                )

                print(f"🏢 Company  : {company}")
                print(f"📧 Emails  : {len(emails)}")
                print(f"📞 Phones  : {len(phones)}")
                print(f"📍 Address : {len(addresses)}")

            except Exception as e:

                print(f"❌ Error: {e}")

        browser.stop()

        excel.save()

        print("\n" + "=" * 60)
        print("✅ Scan Finished")
        print("📄 Excel saved to output/leads.xlsx")
        print("=" * 60)