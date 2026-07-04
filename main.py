import pandas as pd

from scraper.browser import Browser
from scraper.email import EmailExtractor
from scraper.phone import PhoneExtractor
from scraper.contact import ContactFinder
from exporter.excel import ExcelExporter


def main():

    print("=" * 60)
    print("🚀 LeadGen Pro v1.1")
    print("=" * 60)

    browser = Browser()
    browser.start()

    excel = ExcelExporter()

    df = pd.read_csv("input/websites.csv")

    for index, row in df.iterrows():

        website = row["website"]

        print(f"\nScanning ({index + 1}/{len(df)})")
        print(website)

        try:

            page = browser.open(website)

            html = page.content()

            title = page.title()

            emails = EmailExtractor.extract(html)

            phones = PhoneExtractor.extract(html)

            contacts = ContactFinder.extract(
                website,
                html
            )

            # Visit contact pages
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
                website,
                title,
                emails,
                phones,
                contacts
            )

            print(f"✅ {len(emails)} emails")
            print(f"✅ {len(phones)} phones")
            print(f"✅ {len(contacts)} contact pages")

        except Exception as e:

            print("❌", e)

    browser.stop()

    excel.save()

    print("\n🎉 Scan Complete")
    print("📄 output/leads.xlsx")


if __name__ == "__main__":
    main()