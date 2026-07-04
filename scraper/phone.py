import phonenumbers
from phonenumbers import PhoneNumberMatcher


class PhoneExtractor:

    @staticmethod
    def extract(html):

        phones = []

        try:

            for match in PhoneNumberMatcher(html, None):

                number = phonenumbers.format_number(
                    match.number,
                    phonenumbers.PhoneNumberFormat.INTERNATIONAL
                )

                if number not in phones:
                    phones.append(number)

        except:
            pass

        return phones