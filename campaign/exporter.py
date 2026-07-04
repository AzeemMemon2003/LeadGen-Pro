import csv
import os

from database.repository import LeadRepository
from campaign.filter import CampaignFilter


class CampaignExporter:

    @staticmethod
    def export():

        repo = LeadRepository()

        rows = repo.all()

        leads = []

        for row in rows:

            leads.append({

                "id": row[0],
                "company": row[1],
                "website": row[2],
                "email": row[3],
                "score": row[4],
                "priority": row[5],
                "status": row[6]

            })

        print("\nCampaign Export")

        min_score = int(input("Minimum Score (default 70): ") or "70")

        priority = input("Priority (HOT/WARM/LOW) [HOT]: ").strip().upper() or "HOT"

        status = input("Status [Not Contacted]: ").strip() or "Not Contacted"

        filtered = CampaignFilter.filter(
            leads,
            min_score=min_score,
            priority=priority,
            status=status
        )

        os.makedirs("output", exist_ok=True)

        filename = "output/campaign_export.csv"

        with open(filename, "w", newline="", encoding="utf-8") as f:

            writer = csv.writer(f)

            writer.writerow([
                "Company",
                "Website",
                "Email",
                "Score",
                "Priority",
                "Status"
            ])

            for lead in filtered:

                writer.writerow([
                    lead["company"],
                    lead["website"],
                    lead["email"],
                    lead["score"],
                    lead["priority"],
                    lead["status"]
                ])

        print(f"\n✅ Exported {len(filtered)} leads")
        print(f"📄 {filename}")