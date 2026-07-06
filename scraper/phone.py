import re

import phonenumbers
from phonenumbers import (
    PhoneNumberMatcher,
    PhoneNumberFormat,
    PhoneNumberType
)


class PhoneExtractor:

    BLACKLIST = {

        "+1 123-456-7890",
        "+1 111-111-1111",
        "+1 000-000-0000"

    }

    @staticmethod
    def extract(html):

        phones = set()

        if not html:
            return []

        html = html.replace("tel:", "")

        try:

            matches = PhoneNumberMatcher(
                html,
                "US"
            )

            for match in matches:

                try:

                    number = match.number

                    if not phonenumbers.is_valid_number(number):
                        continue

                    number_type = phonenumbers.number_type(number)

                    if number_type not in (

                        PhoneNumberType.FIXED_LINE,
                        PhoneNumberType.MOBILE,
                        PhoneNumberType.FIXED_LINE_OR_MOBILE

                    ):

                        continue

                    formatted = phonenumbers.format_number(

                        number,
                        PhoneNumberFormat.INTERNATIONAL

                    )

                    formatted = re.sub(
                        r"\s+",
                        " ",
                        formatted
                    ).strip()

                    if formatted in PhoneExtractor.BLACKLIST:
                        continue

                    digits = re.sub(r"\D", "", formatted)

                    if len(digits) < 10:
                        continue

                    if digits.count(digits[0]) == len(digits):
                        continue

                    phones.add(formatted)

                except Exception:
                    continue

        except Exception:
            pass

        return sorted(phones)