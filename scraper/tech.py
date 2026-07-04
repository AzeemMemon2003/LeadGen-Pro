class TechExtractor:

    @staticmethod
    def extract(html):

        html = html.lower()

        tech = []

        if "wp-content" in html or "wordpress" in html:
            tech.append("WordPress")

        if "cdn.shopify.com" in html or "shopify" in html:
            tech.append("Shopify")

        if "wix" in html:
            tech.append("Wix")

        if "webflow" in html:
            tech.append("Webflow")

        if "squarespace" in html:
            tech.append("Squarespace")

        if "__next" in html:
            tech.append("Next.js")

        if "react" in html:
            tech.append("React")

        if "hs-script-loader" in html:
            tech.append("HubSpot")

        if not tech:
            tech.append("Unknown")

        return sorted(set(tech))