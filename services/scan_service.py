from scraper.company import CompanyExtractor
from scraper.email import EmailExtractor
from scraper.phone import PhoneExtractor
from scraper.address import AddressExtractor
from scraper.tech import TechExtractor
from scraper.seo import SEOExtractor

from services.crawl_service import CrawlService

from intelligence.qualifier import LeadQualifier
from ai.opportunity import OpportunityEngine


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

        crawl = CrawlService.crawl(
            browser,
            website,
            html
        )

        emails.extend(crawl["emails"])
        phones.extend(crawl["phones"])
        addresses.extend(crawl["addresses"])

        emails = sorted(set(emails))
        phones = sorted(set(phones))
        addresses = sorted(set(addresses))

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
            "social": social,
            "crawl_pages": crawl["pages"]
        }

        result["qualification"] = LeadQualifier.qualify(result)

        result["opportunity"] = OpportunityEngine.analyze(result)

        return result