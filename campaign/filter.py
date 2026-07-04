class CampaignFilter:

    @staticmethod
    def filter(leads, min_score=70, priority="HOT", status="Not Contacted"):

        filtered = []

        for lead in leads:

            score = lead["score"]
            lead_priority = lead["priority"]
            lead_status = lead["status"]

            if score < min_score:
                continue

            if priority and lead_priority != priority:
                continue

            if status and lead_status != status:
                continue

            filtered.append(lead)

        return filtered