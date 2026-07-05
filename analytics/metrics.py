from database.repository import LeadRepository


class Metrics:

    @staticmethod
    def summary():

        repo = LeadRepository()

        leads = repo.all()

        total = len(leads)

        high_priority = 0
        emails = 0
        phones = 0
        avg_score = 0

        technologies = {}

        for lead in leads:

            if lead["priority"] == "HIGH":
                high_priority += 1

            if lead["primary_email"]:
                emails += 1

            if lead["phone"]:
                phones += 1

            avg_score += lead["website_score"]

            for tech in lead["technology"]:

                technologies[tech] = (
                    technologies.get(tech, 0) + 1
                )

        if total:
            avg_score /= total

        return {

            "total": total,

            "high_priority": high_priority,

            "emails": emails,

            "phones": phones,

            "average_score": round(avg_score, 2),

            "technologies": dict(

                sorted(

                    technologies.items(),

                    key=lambda x: x[1],

                    reverse=True

                )

            )

        }