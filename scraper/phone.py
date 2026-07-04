import re
import phonenumbers
from phonenumbers import (
    PhoneNumberMatcher,
    PhoneNumberFormat
)


class PhoneExtractor:

    @staticmethod
    def extract(html):

        phones = []

        if not html:
            return phones

        # Remove tel:
        html = html.replace("tel:", "")

        try:

            matches = PhoneNumberMatcher(
                html,
                "US"
            )

            for match in matches:

                try:

                    number = phonenumbers.format_number(
                        match.number,
                        PhoneNumberFormat.INTERNATIONAL
                    )

                    number = re.sub(
                        r"\s+",
                        " ",
                        number
                    ).strip()

                    if number not in phones:

                        phones.append(number)

                except Exception:

                    pass

        except Exception:

            pass

        return sorted(phones)