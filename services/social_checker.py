from bs4 import BeautifulSoup


class SocialChecker:
    @staticmethod
    def check(html: str) -> dict:
        """
        Detect social media profile links from HTML.
        """

        soup = BeautifulSoup(html, "html.parser")

        result = {
            "facebook": None,
            "instagram": None,
            "linkedin": None,
            "x": None,
            "youtube": None,
            "tiktok": None,
        }

        social_domains = {
            "facebook": ["facebook.com"],
            "instagram": ["instagram.com"],
            "linkedin": ["linkedin.com"],
            "x": ["x.com", "twitter.com"],
            "youtube": ["youtube.com", "youtu.be"],
            "tiktok": ["tiktok.com"],
        }

        for link in soup.find_all("a", href=True):
            href = link["href"].strip()

            for platform, domains in social_domains.items():
                if result[platform]:
                    continue

                if any(domain in href.lower() for domain in domains):
                    result[platform] = href

        return result


if __name__ == "__main__":

    sample_html = """
    <html>
        <body>

            <a href="https://facebook.com/agencyhash">Facebook</a>

            <a href="https://instagram.com/agencyhash">Instagram</a>

            <a href="https://linkedin.com/company/agencyhash">LinkedIn</a>

            <a href="https://x.com/agencyhash">X</a>

            <a href="https://youtube.com/@agencyhash">YouTube</a>

            <a href="https://tiktok.com/@agencyhash">TikTok</a>

        </body>
    </html>
    """

    print(SocialChecker.check(sample_html))