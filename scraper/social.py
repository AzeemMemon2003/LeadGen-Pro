from bs4 import BeautifulSoup


class SocialExtractor:

    @staticmethod
    def extract(html):

        soup = BeautifulSoup(html, "html.parser")

        social = {
            "linkedin": "",
            "facebook": "",
            "instagram": "",
            "twitter": ""
        }

        for link in soup.find_all("a"):

            href = link.get("href")

            if not href:
                continue

            href = href.strip()

            if "linkedin.com" in href.lower():
                social["linkedin"] = href

            elif "facebook.com" in href.lower():
                social["facebook"] = href

            elif "instagram.com" in href.lower():
                social["instagram"] = href

            elif "twitter.com" in href.lower() or "x.com" in href.lower():
                social["twitter"] = href

        return social