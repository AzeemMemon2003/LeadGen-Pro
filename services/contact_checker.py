from bs4 import BeautifulSoup


class ContactChecker:
    @staticmethod
    def check(html: str) -> dict:
        """
        Analyze HTML and detect available contact methods.
        """

        soup = BeautifulSoup(html, "html.parser")

        result = {
            "contact_form": False,
            "email": False,
            "phone": False,
            "whatsapp": False,
            "quote_button": False,
        }

        # Contact Form
        if soup.find("form"):
            result["contact_form"] = True

        # Email Link
        if soup.find("a", href=lambda x: x and x.startswith("mailto:")):
            result["email"] = True

        # Phone Link
        if soup.find("a", href=lambda x: x and x.startswith("tel:")):
            result["phone"] = True

        # WhatsApp
        if soup.find(
            "a",
            href=lambda x: x and (
                "wa.me" in x
                or "whatsapp.com" in x
                or "api.whatsapp.com" in x
            ),
        ):
            result["whatsapp"] = True

        # Quote Button
        keywords = [
            "quote",
            "get quote",
            "request quote",
            "free quote",
            "estimate",
            "request estimate",
        ]

        for tag in soup.find_all(["a", "button"]):
            text = tag.get_text(" ", strip=True).lower()

            if any(keyword in text for keyword in keywords):
                result["quote_button"] = True
                break

        return result


if __name__ == "__main__":
    sample_html = """
    <html>
        <body>

            <form action="/contact"></form>

            <a href="mailto:info@example.com">Email Us</a>

            <a href="tel:+1234567890">Call Us</a>

            <a href="https://wa.me/1234567890">WhatsApp</a>

            <button>Get Quote</button>

        </body>
    </html>
    """

    print(ContactChecker.check(sample_html))