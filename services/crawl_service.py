from scraper.email import EmailExtractor
from scraper.phone import PhoneExtractor
from scraper.address import AddressExtractor
from scraper.crawler import SmartCrawler

from network.fetcher import Fetcher

from utils.logger import Logger


class CrawlService:

    MAX_PAGES = 5

    @staticmethod
    def crawl(browser, website, html):

        logger = Logger.get_logger()

        emails = set()
        phones = set()
        addresses = set()

        pages = SmartCrawler.extract(
            website,
            html
        )

        # Remove duplicates while preserving order
        crawl_pages = list(dict.fromkeys(pages))

        # Limit crawl pages
        crawl_pages = crawl_pages[:CrawlService.MAX_PAGES]

        print(f"🕷 Crawling {len(crawl_pages)} pages...")

        for index, url in enumerate(crawl_pages, start=1):

            print(f"   [{index}/{len(crawl_pages)}] {url}")

            try:

                crawl_html = Fetcher.get(url)

                if not crawl_html:
                    logger.warning(
                        f"Empty response: {url}"
                    )
                    continue

                emails.update(
                    EmailExtractor.extract(crawl_html)
                )

                phones.update(
                    PhoneExtractor.extract(crawl_html)
                )

                addresses.update(
                    AddressExtractor.extract(crawl_html)
                )

            except Exception as e:

                logger.warning(
                    f"Crawl failed: {url} | {e}"
                )

        return {

            "emails": sorted(emails),

            "phones": sorted(phones),

            "addresses": sorted(addresses),

            "pages": crawl_pages

        }