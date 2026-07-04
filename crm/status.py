from database.repository import LeadRepository


class LeadStatus:

    @staticmethod
    def update():

        repo = LeadRepository()

        lead_id = input("\nLead ID: ").strip()

        statuses = [
            "Not Contacted",
            "Email Sent",
            "Follow Up",
            "Meeting Booked",
            "Won",
            "Lost"
        ]

        print()

        for index, status in enumerate(statuses, start=1):

            print(f"{index}. {status}")

        choice = input("\nChoice: ").strip()

        try:

            repo.update_status(
                int(lead_id),
                statuses[int(choice) - 1]
            )

            print("\n✅ Status Updated")

        except Exception:

            print("\n❌ Invalid Input")