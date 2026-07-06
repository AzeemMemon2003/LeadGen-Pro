import json
import re

from bs4 import BeautifulSoup


class CompanyExtractor:

    SEPARATORS = [
        "|",
        " - ",
        " – ",
        " — ",
        " • ",
        " :: ",
        ":"
    ]

    NOISE = [
        "official site",
        "official website",
        "home",
        "homepage",
        "welcome",
        "best",
        "premium",
        "since",
        "shop online",
        "buy online",
        "we help",
        "learn more",
        "contact us"
    ]

    @classmethod
    def clean(cls, text):

        if not text:
            return ""

        text = re.sub(r"\s+", " ", text).strip()

        for sep in cls.SEPARATORS:

            if sep in text:

                text = text.split(sep)[0].strip()

        lower = text.lower()

        for noise in cls.NOISE:

            if noise in lower:

                idx = lower.find(noise)

                text = text[:idx].strip()

                break

        text = re.sub(r"\s{2,}", " ", text)

        return text.strip(" -|:•")

    @classmethod
    def extract(cls, page, html):

        soup = BeautifulSoup(html, "html.parser")

        # --------------------------------
        # Open Graph
        # --------------------------------

        og = soup.find("meta", property="og:site_name")

        if og and og.get("content"):

            company = cls.clean(og["content"])

            if company:
                return company

        # --------------------------------
        # JSON-LD
        # --------------------------------

        scripts = soup.find_all(
            "script",
            type="application/ld+json"
        )

        for script in scripts:

            try:

                if not script.string:
                    continue

                data = json.loads(script.string)

                if isinstance(data, list):

                    items = data

                else:

                    items = [data]

                for item in items:

                    if not isinstance(item, dict):
                        continue

                    if item.get("@type") in (

                        "Organization",
                        "LocalBusiness",
                        "Corporation"

                    ):

                        name = cls.clean(
                            item.get("name", "")
                        )

                        if name:
                            return name

            except Exception:

                pass

        # --------------------------------
        # Application Name
        # --------------------------------

        app = soup.find(
            "meta",
            attrs={
                "name": "application-name"
            }
        )

        if app and app.get("content"):

            company = cls.clean(
                app["content"]
            )

            if company:
                return company

        # --------------------------------
        # Title
        # --------------------------------

        title = cls.clean(page.title())

        if title:

            return title

        # --------------------------------
        # Domain
        # --------------------------------

        domain = (
            page.url
            .replace("https://", "")
            .replace("http://", "")
            .split("/")[0]
            .replace("www.", "")
        )

        domain = domain.split(".")[0]

        return domain.replace("-", " ").title()