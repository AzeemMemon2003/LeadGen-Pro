from bs4 import BeautifulSoup


class CompanyExtractor:

    @staticmethod
    def extract(page, html):

        soup = BeautifulSoup(html, "html.parser")

        # Open Graph
        og = soup.find("meta", property="og:site_name")

        if og and og.get("content"):
            return og["content"].strip()

        title = page.title()

        for sep in ["|", "-", "—", "•"]:

            if sep in title:
                title = title.split(sep)[0]

        return title.strip()