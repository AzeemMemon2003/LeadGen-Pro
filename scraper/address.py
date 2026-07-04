import re
from bs4 import BeautifulSoup


class AddressExtractor:

    STREET_TYPES = (
        "street", "st",
        "road", "rd",
        "avenue", "ave",
        "boulevard", "blvd",
        "drive", "dr",
        "lane", "ln",
        "court", "ct",
        "circle", "cir",
        "parkway", "pkwy",
        "way",
        "place", "pl",
        "suite", "ste"
    )

    @staticmethod
    def extract(html):

        soup = BeautifulSoup(html, "html.parser")

        # Remove junk
        for tag in soup([
            "script",
            "style",
            "noscript",
            "svg"
        ]):
            tag.decompose()

        text = soup.get_text(" ", strip=True)

        addresses = []

        pattern = re.compile(
            r"\d{1,6}\s+[^,]{2,80},\s*"
            r"[^,]{2,40},\s*"
            r"[A-Z]{2}\s+\d{5}",
            re.IGNORECASE
        )

        for match in pattern.findall(text):

            address = " ".join(match.split())

            lower = address.lower()

            if not any(
                street in lower
                for street in AddressExtractor.STREET_TYPES
            ):
                continue

            if address not in addresses:

                addresses.append(address)

        return addresses