class LeadScorer:

    @staticmethod
    def score(
        emails,
        phones,
        addresses,
        technology,
        seo,
        contact_pages
    ):

        score = 0
        opportunities = []

        # Email
        if emails:
            score += 20
        else:
            opportunities.append("No public email")

        # Phone
        if phones:
            score += 15
        else:
            opportunities.append("No public phone")

        # Address
        if addresses:
            score += 10
        else:
            opportunities.append("No address found")

        # Contact Page
        if contact_pages:
            score += 15
        else:
            opportunities.append("No contact page")

        # SEO
        if seo["title"]:
            score += 10
        else:
            opportunities.append("Missing title")

        if seo["meta_description"]:
            score += 10
        else:
            opportunities.append("Missing meta description")

        if seo["h1"]:
            score += 10
        else:
            opportunities.append("Missing H1")

        # Images
        if seo["images_without_alt"] == 0:
            score += 10
        else:
            opportunities.append(
                f"{seo['images_without_alt']} images missing ALT"
            )

        return {
            "score": score,
            "opportunities": opportunities
        }