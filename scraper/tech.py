from bs4 import BeautifulSoup


class TechExtractor:

    @staticmethod
    def extract(html):

        html = html.lower()

        soup = BeautifulSoup(html, "html.parser")

        tech = []

        # ---------- CMS ----------

        if "wp-content" in html or "wp-includes" in html:
            tech.append("WordPress")

        if "cdn.shopify.com" in html or "shopify.theme" in html:
            tech.append("Shopify")

        if "wixstatic" in html or "wix.com" in html:
            tech.append("Wix")

        if "webflow" in html:
            tech.append("Webflow")

        if "squarespace" in html:
            tech.append("Squarespace")

        # ---------- Frameworks ----------

        if "__next" in html:
            tech.append("Next.js")

        if "__nuxt" in html:
            tech.append("Nuxt.js")

        if "_astro" in html:
            tech.append("Astro")

        if "gatsby" in html:
            tech.append("Gatsby")

        # ---------- Libraries ----------

        scripts = soup.find_all("script", src=True)

        for script in scripts:

            src = script["src"].lower()

            if "react" in src:
                tech.append("React")

            if "vue" in src:
                tech.append("Vue")

            if "angular" in src:
                tech.append("Angular")

        # ---------- Hosting ----------

        if "cloudflare" in html:
            tech.append("Cloudflare")

        # ---------- Backend ----------

        if "csrfmiddlewaretoken" in html:
            tech.append("Django")

        # Remove duplicates
        tech = sorted(set(tech))

        if not tech:
            tech.append("Unknown")

        return tech