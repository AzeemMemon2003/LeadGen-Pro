class OpportunityEngine:

    @staticmethod
    def analyze(result):

        seo = result["seo"]
        tech = [t.lower() for t in result["technology"]]

        problems = []
        services = []

        # -----------------------
        # SEO
        # -----------------------

        if not seo["title"]:
            problems.append("Missing page title")
            services.append("Technical SEO")

        if not seo["meta_description"]:
            problems.append("Missing meta description")
            services.append("On-Page SEO")

        if not seo["h1"]:
            problems.append("Missing H1 heading")
            services.append("Content Optimization")

        if seo["images_without_alt"] > 5:
            problems.append(
                f"{seo['images_without_alt']} images missing ALT tags"
            )
            services.append("Image SEO")

        # -----------------------
        # Technology
        # -----------------------

        if "wordpress" in tech:
            services.append("WordPress Maintenance")

        if "shopify" in tech:
            services.append("Shopify Optimization")

        if "wix" in tech:
            services.append("Website Redesign")

        # -----------------------
        # Contact
        # -----------------------

        if not result["emails"]:
            problems.append("No business email found")
            services.append("Lead Capture")

        if not result["phones"]:
            problems.append("No phone number found")
            services.append("Conversion Optimization")

        # -----------------------
        # Remove duplicates
        # -----------------------

        services = sorted(set(services))

        # -----------------------
        # Summary
        # -----------------------

        if not problems:

            summary = (
                "This business appears technically healthy. "
                "Focus on growth opportunities."
            )

            priority = "Low"

        else:

            summary = (
                f"Found {len(problems)} improvement opportunities "
                "that Agency Hash can help solve."
            )

            if len(problems) >= 5:
                priority = "High"
            elif len(problems) >= 3:
                priority = "Medium"
            else:
                priority = "Low"

        return {
            "summary": summary,
            "priority": priority,
            "problems": problems,
            "services": services
        }