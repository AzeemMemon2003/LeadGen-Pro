from urllib.parse import urlparse


class URLHelper:

    @staticmethod
    def normalize(url):

        if not url:
            return ""

        url = url.strip().lower()

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        parsed = urlparse(url)

        domain = parsed.netloc

        if domain.startswith("www."):
            domain = domain[4:]

        path = parsed.path.rstrip("/")

        return f"https://{domain}{path}"

    @classmethod
    def remove_duplicates(cls, websites):

        unique = []
        seen = set()

        for website in websites:

            try:

                normalized = cls.normalize(website)

                if normalized in seen:
                    continue

                seen.add(normalized)

                unique.append(normalized)

            except Exception:
                pass

        return unique