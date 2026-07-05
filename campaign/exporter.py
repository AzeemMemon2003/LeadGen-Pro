import csv
from config.settings import Settings


class CampaignExporter:

    def __init__(self):

        self.output_dir = Settings.CAMPAIGN_DIR

    def export(self, campaigns):

        for campaign_name, leads in campaigns.items():

            filename = self.output_dir / f"{campaign_name}.csv"

            with open(
                filename,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Company",
                    "Website",
                    "Email",
                    "Phone",
                    "Priority",
                    "Website Score"
                ])

                for lead in leads:

                    writer.writerow([

                        lead.get("company", ""),

                        lead.get("website", ""),

                        lead.get("primary_email", ""),

                        lead.get("phone", ""),

                        lead.get("priority", ""),

                        lead.get("website_score", "")

                    ])

        print(
            f"\n✅ {len(campaigns)} campaign files exported to {self.output_dir}"
        )


if __name__ == "__main__":

    sample = {

        "seo_campaign": [

            {
                "company": "ABC Dental",
                "website": "https://abc.com",
                "primary_email": "info@abc.com",
                "phone": "+123456789",
                "priority": "HIGH",
                "website_score": 58
            }

        ]

    }

    CampaignExporter().export(sample)