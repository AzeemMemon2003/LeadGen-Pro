import re
import phonenumbers
from phonenumbers import PhoneNumberMatcher


class PhoneExtractor:

    @staticmethod
    def extract(html):

        phones = []

        # Method 1
        try:

            for match in PhoneNumberMatcher(html, "US"):

                number = phonenumbers.format_number(
                    match.number,
                    phonenumbers.PhoneNumberFormat.INTERNATIONAL
                )

                if number not in phones:
                    phones.append(number)

        except:
            pass

        # Method 2
        tel_links = re.findall(
            r'tel:([^"\']+)',
            html,
            flags=re.IGNORECASE
        )

        for phone in tel_links:

            phone = phone.strip()

            if phone not in phones:
                phones.append(phone)

        return phones