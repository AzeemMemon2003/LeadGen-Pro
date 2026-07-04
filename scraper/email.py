import re
import html


class EmailExtractor:

    BLACKLIST = {
        "example@example.com",
        "test@test.com",
        "admin@example.com",
        "name@example.com",
        "your@email.com"
    }

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

        # Decode HTML entities
        html_content = html.unescape(html_content)

        # Convert common obfuscations
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

        emails = []

        # Standard email regex
        pattern = r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}"

        emails.extend(re.findall(pattern, html_content))

        # mailto links
        mailto = re.findall(
            r"mailto:([^?\"' >]+)",
            html_content,
            flags=re.IGNORECASE
        )

        emails.extend(mailto)

        cleaned = []

        for email in emails:

            email = email.lower().strip()

            # Remove query parameters
            if "?" in email:
                email = email.split("?")[0]

            # Remove mailto if still present
            email = email.replace("mailto:", "")

            # Skip fake emails
            if email in EmailExtractor.BLACKLIST:
                continue

            # Skip image names
            if email.endswith(EmailExtractor.IMAGE_EXTENSIONS):
                continue

            # Basic validation
            if email.count("@") != 1:
                continue

            if email not in cleaned:
                cleaned.append(email)

        return sorted(cleaned)