from pprint import pprint

from services.contact_checker import ContactChecker
from services.https_checker import HTTPSChecker
from services.performance_checker import PerformanceChecker
from services.social_checker import SocialChecker
from services.tracking_checker import TrackingChecker
from services.trust_checker import TrustChecker


class WebsiteIntelligence:
    @staticmethod
    def analyze(url: str, html: str) -> dict:
        """
        Generate a complete website intelligence report.
        """

        https = HTTPSChecker.check(url)
        contact = ContactChecker.check(html)
        social = SocialChecker.check(html)
        tracking = TrackingChecker.check(html)
        trust = TrustChecker.check(html)
        performance = PerformanceChecker.check(html)

        score = 100
        strengths = []
        weaknesses = []
        opportunities = []

        # ------------------------
        # HTTPS
        # ------------------------

        if https["https"]:
            strengths.append("HTTPS Enabled")
        else:
            score -= 10
            weaknesses.append("HTTPS Not Enabled")
            opportunities.append("Enable HTTPS")

        # ------------------------
        # Contact
        # ------------------------

        if contact["contact_form"]:
            strengths.append("Contact Form Available")
        else:
            score -= 10
            weaknesses.append("No Contact Form")
            opportunities.append("Add Contact Form")

        if contact["email"]:
            strengths.append("Public Email Found")
        else:
            score -= 5
            weaknesses.append("No Email Address")
            opportunities.append("Display Business Email")

        if contact["phone"]:
            strengths.append("Phone Number Available")
        else:
            score -= 5
            weaknesses.append("No Phone Number")
            opportunities.append("Display Business Phone")

        if contact["whatsapp"]:
            strengths.append("WhatsApp Available")

        if contact["quote_button"]:
            strengths.append("Quote Button Available")

        # ------------------------
        # Tracking
        # ------------------------

        if tracking["ga4"]:
            strengths.append("Google Analytics 4 Installed")
        else:
            score -= 10
            weaknesses.append("Google Analytics Missing")
            opportunities.append("Install Google Analytics 4")

        if tracking["gtm"]:
            strengths.append("Google Tag Manager Installed")
        else:
            score -= 5
            weaknesses.append("Google Tag Manager Missing")
            opportunities.append("Install Google Tag Manager")

        if tracking["meta_pixel"]:
            strengths.append("Meta Pixel Installed")
        else:
            score -= 5
            weaknesses.append("Meta Pixel Missing")
            opportunities.append("Install Meta Pixel")

        if tracking["linkedin_insight"]:
            strengths.append("LinkedIn Insight Installed")

        if tracking["hotjar"]:
            strengths.append("Hotjar Installed")

        if tracking["clarity"]:
            strengths.append("Microsoft Clarity Installed")

        # ------------------------
        # Trust
        # ------------------------

        if trust["privacy_policy"]:
            strengths.append("Privacy Policy Found")
        else:
            score -= 5
            weaknesses.append("Privacy Policy Missing")
            opportunities.append("Add Privacy Policy")

        if trust["terms"]:
            strengths.append("Terms & Conditions Found")
        else:
            score -= 5
            weaknesses.append("Terms & Conditions Missing")
            opportunities.append("Add Terms & Conditions")

        if trust["cookie_policy"]:
            strengths.append("Cookie Policy Found")

        if trust["refund_policy"]:
            strengths.append("Refund Policy Found")

        if trust["about_page"]:
            strengths.append("About Page Found")

        if trust["testimonials"]:
            strengths.append("Testimonials Available")

        if trust["reviews"]:
            strengths.append("Customer Reviews Available")

        # ------------------------
        # Social
        # ------------------------

        social_profiles = sum(
            value is not None
            for value in social.values()
        )

        if social_profiles == 0:
            score -= 5
            weaknesses.append("No Social Media Presence")
            opportunities.append("Create Social Media Profiles")
        else:
            strengths.append(f"{social_profiles} Social Profiles Found")

        # ------------------------
        # Performance
        # ------------------------

        if performance["images_without_dimensions"] > 0:
            score -= 2
            weaknesses.append(
                f"{performance['images_without_dimensions']} Images Missing Dimensions"
            )
            opportunities.append("Optimize Image Dimensions")

        if performance["large_images"] > 5:
            score -= 3
            weaknesses.append("Too Many Large Images")
            opportunities.append("Compress Website Images")

        score = max(score, 0)

        return {
            "website_score": score,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "sales_opportunities": opportunities,
            "https": https,
            "contact": contact,
            "social": social,
            "tracking": tracking,
            "trust": trust,
            "performance": performance,
        }


if __name__ == "__main__":

    html = """
    <html>

        <body>

            <form></form>

            <a href="mailto:info@test.com">Email</a>

            <a href="tel:+123456789">Call</a>

            <a href="https://facebook.com/test">Facebook</a>

            <a href="/privacy-policy">Privacy Policy</a>

            <a href="/about">About Us</a>

            <img src="hero.jpg">

        </body>

    </html>
    """

    report = WebsiteIntelligence.analyze(
        "https://example.com",
        html,
    )

    pprint(report)