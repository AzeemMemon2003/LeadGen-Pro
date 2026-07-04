from bs4 import BeautifulSoup
from urllib.parse import urljoin


class ContactFormExtractor:

    CONTACT_KEYWORDS = [
        "contact",
        "contact-us",
        "contactus",
        "get-in-touch",
        "reach-us",
        "reach",
        "support"
    ]

    @staticmethod
    def extract(base_url, html):

        soup = BeautifulSoup(html, "html.parser")

        result = {
            "url": "",
            "has_form": False
        }

        # Detect forms on current page
        forms = soup.find_all("form")

        if forms:

            result["url"] = base_url
            result["has_form"] = True
            return result

        # Search links
        for link in soup.find_all("a", href=True):

            href = link["href"].lower()

            if any(keyword in href for keyword in ContactFormExtractor.CONTACT_KEYWORDS):

                result["url"] = urljoin(base_url, link["href"])

                return result

        return result