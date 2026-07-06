import re
import html


class EmailExtractor:

    BLACKLIST = {

        "example@example.com",
        "test@test.com",
        "admin@example.com",
        "name@example.com",
        "your@email.com",

    }

    BLACKLIST_KEYWORDS = (

        "example",
        "test",
        "dummy",
        "sample",
        "fake",
        "invalid",
        "your@email",
        "your-email",
        "noreply",
        "no-reply",
        "donotreply",
        "do-not-reply"

    )

    IMAGE_EXTENSIONS = (

        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".svg",
        ".webp",
        ".ico"

    )

    @staticmethod
    def extract(html_content):

        if not html_content:
            return []

        html_content = html.unescape(html_content)

        replacements = {

            "[at]": "@",
            "(at)": "@",
            " at ": "@",

            "[dot]": ".",
            "(dot)": ".",
            " dot ": "."

        }

        for old, new in replacements.items():

            html_content = html_content.replace(old, new)

        pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"

        emails = re.findall(pattern, html_content)

        emails.extend(

            re.findall(

                r"mailto:([^?\"' >]+)",

                html_content,

                flags=re.IGNORECASE

            )

        )

        cleaned = []

        for email in emails:

            email = email.lower().strip()

            email = email.replace("mailto:", "")

            if "?" in email:

                email = email.split("?")[0]

            if email in EmailExtractor.BLACKLIST:

                continue

            if email.endswith(EmailExtractor.IMAGE_EXTENSIONS):

                continue

            if email.count("@") != 1:

                continue

            local, domain = email.split("@")

            if len(local) < 2:

                continue

            if "." not in domain:

                continue

            if domain.endswith(".png"):

                continue

            if domain.endswith(".jpg"):

                continue

            if domain.endswith(".svg"):

                continue

            if domain.endswith(".gif"):

                continue

            if any(

                keyword in email

                for keyword in EmailExtractor.BLACKLIST_KEYWORDS

            ):

                continue

            if email not in cleaned:

                cleaned.append(email)

        return sorted(cleaned)