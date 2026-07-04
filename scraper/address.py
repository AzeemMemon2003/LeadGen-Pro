import re


class AddressExtractor:

    @staticmethod
    def extract(html):

        addresses = []

        patterns = [

            # US style addresses
            r"\d{1,6}\s+[A-Za-z0-9\s.,'-]+,\s*[A-Za-z\s]+,\s*[A-Z]{2}\s+\d{5}",

            # UK / General postal codes
            r"\d{1,6}\s+[A-Za-z0-9\s.,'-]+,\s*[A-Za-z\s]+,\s*[A-Za-z0-9 ]{4,10}",

        ]

        for pattern in patterns:

            matches = re.findall(pattern, html)

            addresses.extend(matches)

        # Remove duplicates
        addresses = list(dict.fromkeys(addresses))

        return addresses