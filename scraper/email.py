import re


class EmailExtractor:

    @staticmethod
    def extract(html):

        emails = []

        # Normal emails
        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        emails.extend(re.findall(pattern, html))

        # mailto: links
        mailto = re.findall(
            r'mailto:([^\?"\' >]+)',
            html,
            flags=re.IGNORECASE
        )

        emails.extend(mailto)

        cleaned = []

        blacklist = [
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".svg",
            ".webp",
            "@example.com",
            "@email.com"
        ]

        for email in emails:

            email = email.lower().strip()

            # Remove query string
            if "?" in email:
                email = email.split("?")[0]

            # Skip fake emails
            if any(x in email for x in blacklist):
                continue

            if email not in cleaned:
                cleaned.append(email)

        return cleaned