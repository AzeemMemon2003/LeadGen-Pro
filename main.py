import pandas as pd

from scraper.browser import Browser
from scraper.email import EmailExtractor
from scraper.phone import PhoneExtractor
from scraper.contact import ContactFinder
from scraper.company import CompanyExtractor
from exporter.excel import ExcelExporter


def main():

    print("=" * 60)
    print("🚀 LeadGen Pro v1.2")
    print("=" * 60)

    browser = Browser()
    browser.start()

    excel = ExcelExporter()

    df = pd.read_csv("input/websites.csv")

    total = len(df)

    for index, row in df.iterrows():

        website = row["website"]

        print("\n" + "=" * 60)
        print(f"Scanning ({index + 1}/{total})")
        print(website)
        print("=" * 60)

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

            # Visit every contact page
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

                except Exception:
                    pass

            emails = sorted(set(emails))
            phones = sorted(set(phones))

            excel.add(
                company,
                website,
                title,
                emails,
                phones,
                contacts
            )

            print(f"🏢 Company : {company}")
            print(f"📧 Emails  : {len(emails)}")
            print(f"📞 Phones  : {len(phones)}")
            print(f"📍 Contacts: {len(contacts)}")

        except Exception as e:

            print("❌", e)

    browser.stop()

    excel.save()

    print("\n")
    print("=" * 60)
    print("✅ Scan Complete")
    print("📄 Excel saved to output/leads.xlsx")
    print("=" * 60)


if __name__ == "__main__":
    main()