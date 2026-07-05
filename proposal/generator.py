from datetime import datetime

from proposal.pricing import Pricing


class ProposalGenerator:

    @staticmethod
    def generate(result):

        opportunity = result["opportunity"]

        pricing = Pricing.calculate(
            opportunity["services"]
        )

        return {

            "company": result["company"],

            "website": result["website"],

            "generated_at": datetime.now().strftime(
                "%d %B %Y %I:%M %p"
            ),

            "priority": opportunity["priority"],

            "summary": opportunity["summary"],

            "website_score": result.get(
                "website_intelligence",
                {}
            ).get(
                "website_score",
                0
            ),

            "problems": opportunity["problems"],

            "services": pricing["items"],

            "estimated_budget": pricing["total"],

            "estimated_duration": ProposalGenerator.duration(
                pricing["items"]
            )

        }

    @staticmethod
    def duration(items):

        if not items:
            return "N/A"

        durations = []

        for item in items:

            duration = item["duration"]

            if duration not in durations:
                durations.append(duration)

        return ", ".join(durations)