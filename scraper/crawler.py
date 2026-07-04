from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


class SmartCrawler:

    IMPORTANT_KEYWORDS = [
        "contact",
        "about",
        "team",
        "support",
        "company",
        "privacy",
        "legal",
        "career",
        "careers",
        "staff"
    ]

    @staticmethod
    def extract(base_url, html):

        soup = BeautifulSoup(html, "html.parser")

        links = []

        base_domain = urlparse(base_url).netloc

        for tag in soup.find_all("a"):

            href = tag.get("href")

            if not href:
                continue

            full_url = urljoin(base_url, href)

            parsed = urlparse(full_url)

            # Skip external websites
            if parsed.netloc != base_domain:
                continue

            # Skip files
            if any(
                full_url.lower().endswith(ext)
                for ext in [
                    ".jpg",
                    ".png",
                    ".pdf",
                    ".zip",
                    ".doc",
                    ".docx"
                ]
            ):
                continue

            for keyword in SmartCrawler.IMPORTANT_KEYWORDS:

                if keyword in full_url.lower():

                    if full_url not in links:
                        links.append(full_url)

                    break

        return links[:5]