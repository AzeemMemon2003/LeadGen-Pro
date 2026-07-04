import json

from bs4 import BeautifulSoup


class CompanyExtractor:

    @staticmethod
    def extract(page, html):

        soup = BeautifulSoup(html, "html.parser")

        # -------------------------
        # Open Graph
        # -------------------------

        og = soup.find("meta", property="og:site_name")

        if og and og.get("content"):

            return og["content"].strip()

        # -------------------------
        # JSON-LD Organization
        # -------------------------

        scripts = soup.find_all(
            "script",
            type="application/ld+json"
        )

        for script in scripts:

            try:

                data = json.loads(script.string)

                if isinstance(data, list):

                    for item in data:

                        if isinstance(item, dict):

                            if item.get("@type") in [
                                "Organization",
                                "LocalBusiness",
                                "Corporation"
                            ]:

                                if item.get("name"):

                                    return item["name"].strip()

                elif isinstance(data, dict):

                    if data.get("@type") in [
                        "Organization",
                        "LocalBusiness",
                        "Corporation"
                    ]:

                        if data.get("name"):

                            return data["name"].strip()

            except Exception:

                pass

        # -------------------------
        # Application Name
        # -------------------------

        app = soup.find(
            "meta",
            attrs={"name": "application-name"}
        )

        if app and app.get("content"):

            return app["content"].strip()

        # -------------------------
        # Title
        # -------------------------

        title = page.title()

        for sep in [

            "|",

            "-",

            "—",

            "•",

            ":"

        ]:

            if sep in title:

                title = title.split(sep)[0]

        title = title.strip()

        if title:

            return title

        # -------------------------
        # Domain fallback
        # -------------------------

        url = page.url

        domain = (
            url.replace("https://", "")
               .replace("http://", "")
               .split("/")[0]
        )

        if domain.startswith("www."):

            domain = domain[4:]

        return domain