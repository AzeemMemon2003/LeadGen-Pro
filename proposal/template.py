class ProposalTemplate:

    @staticmethod
    def render(proposal):

        lines = []

        lines.append("=" * 60)
        lines.append("           AGENCY HASH")
        lines.append("      Website Growth Proposal")
        lines.append("=" * 60)
        lines.append("")

        lines.append(f"Company           : {proposal['company']}")
        lines.append(f"Website           : {proposal['website']}")
        lines.append(f"Generated         : {proposal['generated_at']}")
        lines.append(f"Priority          : {proposal['priority']}")
        lines.append(f"Website Score     : {proposal['website_score']}/100")
        lines.append("")

        lines.append("EXECUTIVE SUMMARY")
        lines.append("-" * 60)
        lines.append(proposal["summary"])
        lines.append("")

        lines.append("PROBLEMS IDENTIFIED")
        lines.append("-" * 60)

        if proposal["problems"]:

            for problem in proposal["problems"]:
                lines.append(f"• {problem}")

        else:

            lines.append("No major issues detected.")

        lines.append("")

        lines.append("RECOMMENDED SERVICES")
        lines.append("-" * 60)

        if proposal["services"]:

            for service in proposal["services"]:

                lines.append(
                    f"• {service['service']}"
                )

                lines.append(
                    f"  Price    : ${service['price']}"
                )

                lines.append(
                    f"  Duration : {service['duration']}"
                )

                lines.append("")

        else:

            lines.append("No recommendations.")

        lines.append("-" * 60)

        lines.append(
            f"Estimated Budget : ${proposal['estimated_budget']:,}"
        )

        lines.append(
            f"Estimated Timeline : {proposal['estimated_duration']}"
        )

        lines.append("")

        lines.append("WHY AGENCY HASH?")
        lines.append("-" * 60)
        lines.append(
            "We specialize in SEO, Web Development, "
            "Google Ads, Local SEO, CRO and Marketing "
            "Automation."
        )

        lines.append("")

        lines.append(
            "Thank you for considering Agency Hash."
        )

        return "\n".join(lines)