from scraper.company import CompanyExtractor
from scraper.email import EmailExtractor
from scraper.phone import PhoneExtractor
from scraper.address import AddressExtractor
from scraper.tech import TechExtractor
from scraper.seo import SEOExtractor

from intelligence.contact import ContactIntelligence
from intelligence.qualifier import LeadQualifier
from intelligence.website_intelligence import WebsiteIntelligence

from services.crawl_service import CrawlService

from ai.opportunity import OpportunityEngine

from verification.email import EmailVerifier
from ranking.email_ranker import EmailRanker


class ScanService:

    @staticmethod
    def scan(browser, website):

        page = browser.open(website)

        html = page.content()

        title = page.title()

        company = CompanyExtractor.extract(
            page,
            html
        )

        emails = EmailExtractor.extract(html)

        phones = PhoneExtractor.extract(html)

        addresses = AddressExtractor.extract(html)

        technology = TechExtractor.extract(html)

        seo = SEOExtractor.extract(html)

        website_intelligence = WebsiteIntelligence.analyze(
            website,
            html
        )

        crawl = CrawlService.crawl(
            browser,
            website,
            html
        )

        emails.extend(crawl["emails"])
        phones.extend(crawl["phones"])
        addresses.extend(crawl["addresses"])

        emails = EmailRanker.sort(
            sorted(set(emails))
            )

        primary_email = EmailRanker.best(
            emails
            )

        phones = sorted(set(phones))
        addresses = sorted(set(addresses))

        # ---------------------------------
        # Email Verification
        # ---------------------------------

        email_verification = {}

        if emails:

            try:

                email_verification = EmailVerifier.verify(
                    emails[0]
                )

            except Exception as e:

                email_verification = {
                    "verified": False,
                    "confidence": 0,
                    "provider": "",
                    "syntax_valid": False,
                    "domain_valid": False,
                    "mx_valid": False,
                    "role_account": False,
                    "disposable": False,
                    "reasons": [
                        str(e)
                    ]
                }

        # ---------------------------------
        # Debug Output
        # ---------------------------------

        print("\n" + "=" * 70)
        print("📧 EMAIL VERIFICATION")
        print("=" * 70)

        if emails:
            print(f"Primary Email : {emails[0]}")
        else:
            print("Primary Email : None")

        if email_verification:

            print(f"Verified      : {email_verification.get('verified')}")
            print(f"Confidence    : {email_verification.get('confidence')}%")
            print(f"Syntax        : {email_verification.get('syntax_valid')}")
            print(f"Domain        : {email_verification.get('domain_valid')}")
            print(f"MX            : {email_verification.get('mx_valid')}")
            print(f"Provider      : {email_verification.get('provider')}")
            print(f"Role Account  : {email_verification.get('role_account')}")
            print(f"Disposable    : {email_verification.get('disposable')}")

            if email_verification.get("reasons"):
                print("Reasons:")
                for reason in email_verification["reasons"]:
                    print(f" - {reason}")

        else:

            print("No email verification data.")

        print("=" * 70)

        social = {

            "linkedin": "",
            "facebook": "",
            "instagram": "",
            "twitter": ""

        }

        result = {

            "company": company,
            "website": website,
            "title": title,

            "emails": emails,
            "phones": phones,
            "addresses": addresses,

            "technology": technology,
            "seo": seo,

            "website_intelligence": website_intelligence,

            "email_verification": email_verification,

            "social": social,

            "crawl_pages": crawl["pages"]

        }

        result["qualification"] = LeadQualifier.qualify(
            result
        )

        result["contact"] = ContactIntelligence.build(
            result
        )

        result["opportunity"] = OpportunityEngine.analyze(
            result
        )

        return result