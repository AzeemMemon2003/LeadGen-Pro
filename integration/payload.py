from pathlib import Path


class PayloadBuilder:

    @staticmethod
    def build(result, proposal_path):

        opportunity = result.get("opportunity", {})
        contact = result.get("contact", {})
        website = result.get("website_intelligence", {})

        return {

            "company": result.get("company", ""),

            "website": result.get("website", ""),

            "title": result.get("title", ""),

            "email": contact.get("primary_email", ""),

            "phone": contact.get("primary_phone", ""),

            "address": contact.get("head_office", ""),

            "website_score": website.get(
                "website_score",
                0
            ),

            "priority": opportunity.get(
                "priority",
                "LOW"
            ),

            "summary": opportunity.get(
                "summary",
                ""
            ),

            "estimated_value": opportunity.get(
                "estimated_value",
                0
            ),

            "services": opportunity.get(
                "services",
                []
            ),

            "problems": opportunity.get(
                "problems",
                []
            ),

            "proposal": str(
                Path(proposal_path).resolve()
            )
        }