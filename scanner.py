import pandas as pd

from scraper.browser import Browser
from scraper.company import CompanyExtractor
from scraper.email import EmailExtractor
from scraper.phone import PhoneExtractor
from scraper.contact import ContactFinder
from scraper.social import SocialExtractor
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

            print(f"\n[{index+1}/{total}] {website}")

            try:

                page = browser.open(website)

                html = page.content()

                title = page.title()

                company = CompanyExtractor.extract(page, html)

                emails = EmailExtractor.extract(html)

                phones = PhoneExtractor.extract(html)

                contacts = ContactFinder.extract(
                    website,
                    html
                )

                social = SocialExtractor.extract(html)

                for contact in contacts:

                    try:

                        contact_page = browser.open(contact)

                        contact_html = contact_page.content()

                        emails.extend(
                            EmailExtractor.extract(contact_html)
                        )

                        phones.extend(
                            PhoneExtractor.extract(contact_html)
                        )

                    except:
                        pass

                emails = sorted(set(emails))
                phones = sorted(set(phones))

                excel.add(
                    company,
                    website,
                    title,
                    emails,
                    phones,
                    social,
                    contacts
                )

                print(f"🏢 {company}")
                print(f"📧 {len(emails)} emails")
                print(f"📞 {len(phones)} phones")

            except Exception as e:

                print(e)

        browser.stop()

        excel.save()

        print("\n✅ Scan Finished")