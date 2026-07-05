class CampaignFilters:

    @staticmethod
    def high_priority(leads):
        return [
            lead for lead in leads
            if lead.get("priority") == "HIGH"
        ]

    @staticmethod
    def has_email(leads):
        return [
            lead for lead in leads
            if lead.get("primary_email")
        ]

    @staticmethod
    def has_phone(leads):
        return [
            lead for lead in leads
            if lead.get("phone")
        ]

    @staticmethod
    def website_score_below(leads, score):
        return [
            lead for lead in leads
            if lead.get("website_score", 0) < score
        ]

    @staticmethod
    def technology(leads, keyword):
        keyword = keyword.lower()

        return [
            lead for lead in leads
            if keyword in str(
                lead.get("technology", "")
            ).lower()
        ]

    @staticmethod
    def no_contact_form(leads):
        return [
            lead for lead in leads
            if not lead.get("contact_form")
        ]