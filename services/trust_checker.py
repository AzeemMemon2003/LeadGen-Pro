from bs4 import BeautifulSoup


class TrustChecker:
    @staticmethod
    def check(html: str) -> dict:
        """
        Detect trust and legal pages from HTML.
        """

        soup = BeautifulSoup(html, "html.parser")

        result = {
            "privacy_policy": False,
            "terms": False,
            "cookie_policy": False,
            "refund_policy": False,
            "about_page": False,
            "testimonials": False,
            "reviews": False,
        }

        keywords = {
            "privacy_policy": [
                "privacy policy",
                "privacy"
            ],
            "terms": [
                "terms",
                "terms of service",
                "terms & conditions",
                "terms and conditions",
            ],
            "cookie_policy": [
                "cookie policy",
                "cookies",
            ],
            "refund_policy": [
                "refund",
                "returns",
                "return policy",
                "refund policy",
            ],
            "about_page": [
                "about",
                "about us",
            ],
            "testimonials": [
                "testimonial",
                "testimonials",
                "what our clients say",
            ],
            "reviews": [
                "reviews",
                "customer reviews",
                "google reviews",
            ],
        }

        for tag in soup.find_all(["a", "button"]):
            text = tag.get_text(" ", strip=True).lower()

            for field, words in keywords.items():
                if result[field]:
                    continue

                if any(word in text for word in words):
                    result[field] = True

        return result


if __name__ == "__main__":

    sample_html = """
    <html>
        <body>

            <a href="/about">About Us</a>
            <a href="/privacy-policy">Privacy Policy</a>
            <a href="/terms">Terms & Conditions</a>
            <a href="/cookies">Cookie Policy</a>
            <a href="/refund">Refund Policy</a>
            <a href="/reviews">Customer Reviews</a>
            <a href="/testimonials">Testimonials</a>

        </body>
    </html>
    """

    print(TrustChecker.check(sample_html))