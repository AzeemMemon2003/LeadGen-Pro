from bs4 import BeautifulSoup


class SEOExtractor:

    @staticmethod
    def extract(html):

        soup = BeautifulSoup(html, "html.parser")

        report = {
            "title": False,
            "meta_description": False,
            "h1": False,
            "images_without_alt": 0
        }

        # Title
        if soup.title and soup.title.text.strip():
            report["title"] = True

        # Meta Description
        meta = soup.find("meta", attrs={"name": "description"})
        if meta and meta.get("content"):
            report["meta_description"] = True

        # H1
        if soup.find("h1"):
            report["h1"] = True

        # Images without alt
        images = soup.find_all("img")

        for image in images:

            if not image.get("alt"):
                report["images_without_alt"] += 1

        return report