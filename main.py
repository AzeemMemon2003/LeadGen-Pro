import pandas as pd

from scraper.browser import Browser
from scraper.email import EmailExtractor
from scraper.contact import ContactFinder
from exporter.excel import ExcelExporter


def main():

    browser = Browser()
    browser.start()

    excel = ExcelExporter()

    df = pd.read_csv("input/websites.csv")

    for _, row in df.iterrows():

        website = row["website"]

        print(f"\nScanning {website}")

        try:

            page = browser.open(website)

            html = page.content()

            title = page.title()

            emails = EmailExtractor.extract(html)

            contacts = ContactFinder.extract(
                website,
                html
            )

            # Visit every contact page
            for contact in contacts:

                try:

                    contact_page = browser.open(contact)

                    contact_html = contact_page.content()

                    new_emails = EmailExtractor.extract(contact_html)

                    emails.extend(new_emails)

                except:
                    pass

            emails = sorted(set(emails))

            excel.add(
                website,
                title,
                emails,
                contacts
            )

            print("Emails:", len(emails))
            print("Contact Pages:", len(contacts))

        except Exception as e:

            print(e)

    browser.stop()

    excel.save()

    print("\n✅ Finished")
    print("output/leads.xlsx")


if __name__ == "__main__":
    main()