from bs4 import BeautifulSoup
from urllib.parse import urljoin


class ContactFinder:

    KEYWORDS = [
        "contact",
        "contact-us",
        "contactus",
        "support",
        "help",
        "reach",
        "get-in-touch",
        "about"
    ]

    @staticmethod
    def extract(base_url, html):

        soup = BeautifulSoup(html, "html.parser")

        results = []

        seen = set()

        for link in soup.find_all("a"):

            href = link.get("href")

            if not href:
                continue

            full_url = urljoin(base_url, href)

            if full_url in seen:
                continue

            seen.add(full_url)

            for keyword in ContactFinder.KEYWORDS:

                if keyword in full_url.lower():

                    results.append(full_url)
                    break

        return results