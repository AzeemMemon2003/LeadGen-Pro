from bs4 import BeautifulSoup


class TechExtractor:

    @staticmethod
    def extract(html):

        soup = BeautifulSoup(html, "html.parser")

        html_lower = html.lower()

        tech = []

        # WordPress
        if "wp-content" in html_lower or "wordpress" in html_lower:
            tech.append("WordPress")

        # Shopify
        if "cdn.shopify.com" in html_lower or "shopify" in html_lower:
            tech.append("Shopify")

        # Wix
        if "wix" in html_lower:
            tech.append("Wix")

        # Squarespace
        if "squarespace" in html_lower:
            tech.append("Squarespace")

        # React
        if "__next" in html_lower or "_react" in html_lower:
            tech.append("React / Next.js")

        # Webflow
        if "webflow" in html_lower:
            tech.append("Webflow")

        # HubSpot
        if "hs-script-loader" in html_lower:
            tech.append("HubSpot")

        return sorted(list(set(tech)))