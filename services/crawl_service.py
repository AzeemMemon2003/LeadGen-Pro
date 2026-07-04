from scraper.email import EmailExtractor
from scraper.phone import PhoneExtractor
from scraper.address import AddressExtractor
from scraper.crawler import SmartCrawler

from network.fetcher import Fetcher


class CrawlService:

    @staticmethod
    def crawl(browser, website, html):

        emails = []
        phones = []
        addresses = []

        crawl_pages = SmartCrawler.extract(
            website,
            html
        )

        print(f"🕷 Crawling {len(crawl_pages)} pages...")

        for url in crawl_pages:

            try:

                print(f"   ↳ {url}")

                crawl_html = Fetcher.get(url)

                if not crawl_html:
                    continue

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

        return {
            "emails": emails,
            "phones": phones,
            "addresses": addresses,
            "pages": crawl_pages
        }