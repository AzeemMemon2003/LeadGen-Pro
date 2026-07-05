class OpportunityEngine:

    SERVICE_CATALOG = {
        "Technical SEO": 500,
        "On-Page SEO": 400,
        "Content Optimization": 350,
        "Image SEO": 250,
        "WordPress Maintenance": 300,
        "Shopify Optimization": 600,
        "Website Redesign": 2000,
        "Lead Capture": 500,
        "Conversion Optimization": 700,
        "Google Analytics 4 Setup": 250,
        "Google Tag Manager Setup": 200,
        "Meta Pixel Setup": 200,
        "Privacy Policy Implementation": 150,
        "Local SEO": 800,
        "Google Business Profile Optimization": 600,
    }

    @staticmethod
    def analyze(result):

        seo = result["seo"]

        tech = [t.lower() for t in result["technology"]]

        website = result.get("website_intelligence", {})

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

        elif "shopify" in tech:
            services.append("Shopify Optimization")

        elif "wix" in tech:
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
        # Website Intelligence
        # -----------------------

        for item in website.get(
            "sales_opportunities",
            []
        ):

            if item == "Install Google Analytics 4":

                services.append(
                    "Google Analytics 4 Setup"
                )

            elif item == "Install Google Tag Manager":

                services.append(
                    "Google Tag Manager Setup"
                )

            elif item == "Install Meta Pixel":

                services.append(
                    "Meta Pixel Setup"
                )

            elif item == "Add Privacy Policy":

                services.append(
                    "Privacy Policy Implementation"
                )

            elif item == "Create Social Media Profiles":

                services.append(
                    "Local SEO"
                )

        # -----------------------
        # Remove duplicates
        # -----------------------

        services = sorted(set(services))

        estimate = sum(

            OpportunityEngine.SERVICE_CATALOG.get(
                service,
                0
            )

            for service in services

        )

        # -----------------------
        # Priority
        # -----------------------

        total_issues = len(problems)

        if total_issues >= 6:
            priority = "HIGH"

        elif total_issues >= 3:
            priority = "MEDIUM"

        else:
            priority = "LOW"

        summary = (
            f"Found {len(services)} service opportunities "
            f"worth approximately ${estimate:,}."
        )

        return {

            "priority": priority,

            "summary": summary,

            "problems": problems,

            "services": services,

            "estimated_value": estimate

        }