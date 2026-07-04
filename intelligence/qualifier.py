class LeadQualifier:

    @staticmethod
    def qualify(result):

        score = 0

        reasons = []

        # -----------------------
        # Emails
        # -----------------------

        if result["emails"]:

            score += 20

            reasons.append("Business email found")

        # -----------------------
        # Phones
        # -----------------------

        if result["phones"]:

            score += 15

            reasons.append("Phone number found")

        # -----------------------
        # Contact Pages
        # -----------------------

        if result["crawl_pages"]:

            score += 10

            reasons.append("Contact pages available")

        # -----------------------
        # SEO
        # -----------------------

        seo = result["seo"]

        if not seo["meta_description"]:

            score += 10

            reasons.append("Missing meta description")

        if not seo["h1"]:

            score += 10

            reasons.append("Missing H1 tag")

        if seo["images_without_alt"] > 5:

            score += 10

            reasons.append("Images missing ALT text")

        # -----------------------
        # Technology
        # -----------------------

        tech = [t.lower() for t in result["technology"]]

        if "wordpress" in tech:

            score += 10

            reasons.append("Uses WordPress")

        if "shopify" in tech:

            score += 10

            reasons.append("Uses Shopify")

        # -----------------------
        # Priority
        # -----------------------

        if score >= 70:

            priority = "🔥 HOT"

        elif score >= 40:

            priority = "🟡 WARM"

        else:

            priority = "⚪ LOW"

        return {

            "score": score,

            "priority": priority,

            "reasons": reasons

        }