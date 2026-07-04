import re


class EmailExtractor:

    @staticmethod
    def extract(html):

        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        emails = re.findall(pattern, html)

        clean_emails = []

        for email in emails:

            email = email.lower().strip()

            if email not in clean_emails:
                clean_emails.append(email)

        return clean_emails