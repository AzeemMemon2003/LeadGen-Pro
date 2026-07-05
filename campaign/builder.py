from campaign.filters import CampaignFilters


class CampaignBuilder:

    def __init__(self, leads):

        self.leads = leads

    def build(self):

        campaigns = {}

        campaigns["high_priority"] = CampaignFilters.high_priority(
            self.leads
        )

        campaigns["seo_campaign"] = CampaignFilters.website_score_below(
            self.leads,
            70
        )

        campaigns["email_campaign"] = CampaignFilters.has_email(
            self.leads
        )

        campaigns["phone_campaign"] = CampaignFilters.has_phone(
            self.leads
        )

        campaigns["wordpress"] = CampaignFilters.technology(
            self.leads,
            "wordpress"
        )

        campaigns["shopify"] = CampaignFilters.technology(
            self.leads,
            "shopify"
        )

        campaigns["wix"] = CampaignFilters.technology(
            self.leads,
            "wix"
        )

        campaigns["squarespace"] = CampaignFilters.technology(
            self.leads,
            "squarespace"
        )

        campaigns["no_contact_form"] = CampaignFilters.no_contact_form(
            self.leads
        )

        # Remove empty campaigns
        campaigns = {
            name: leads
            for name, leads in campaigns.items()
            if leads
        }

        return campaigns

    @staticmethod
    def stats(campaigns):

        print("\n" + "=" * 60)
        print("📢 Campaign Summary")
        print("=" * 60)

        total = 0

        for name, leads in campaigns.items():

            print(f"{name:<25} {len(leads)}")

            total += len(leads)

        print("-" * 60)
        print(f"Total Segments : {len(campaigns)}")
        print(f"Total Leads    : {total}")
        print("=" * 60)