from bs4 import BeautifulSoup


class CompanyExtractor:

    @staticmethod
    def extract(page, html):

        soup = BeautifulSoup(html, "html.parser")

        # 1. Open Graph Site Name (Best)
        og = soup.find("meta", property="og:site_name")
        if og and og.get("content"):
            return og["content"].strip()

        # 2. Application Name
        app = soup.find("meta", attrs={"name": "application-name"})
        if app and app.get("content"):
            return app["content"].strip()

        # 3. Organization Schema
        org = soup.find("meta", attrs={"property": "og:site_name"})
        if org and org.get("content"):
            return org["content"].strip()

        # 4. Clean page title
        title = page.title().strip()

        separators = [
            "|",
            " - ",
            " — ",
            " • ",
            ":"
        ]

        for sep in separators:
            if sep in title:
                title = title.split(sep)[0].strip()

        # Remove common suffixes
        remove_words = [
            "Official Site",
            "Official Website",
            "Homepage",
            "Home"
        ]

        for word in remove_words:
            title = title.replace(word, "").strip()

        return title