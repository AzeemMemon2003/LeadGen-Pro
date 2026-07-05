from database.repository import LeadRepository


class LeadViewer:

    @staticmethod
    def show():

        repo = LeadRepository()

        leads = repo.all()

        if not leads:

            print("\n❌ No leads found.")

            return

        print("\n" + "=" * 100)
        print("📋 LeadGen Pro CRM")
        print("=" * 100)

        for lead in leads:

            print(f"🏢 Company        : {lead['company']}")
            print(f"🌐 Website        : {lead['website']}")
            print(f"📧 Primary Email  : {lead['primary_email'] or 'Not Found'}")
            print(f"📞 Phone          : {lead['phone'] or 'Not Found'}")
            print(f"⭐ Lead Score     : {lead['score']}/100")
            print(f"🌍 Website Score  : {lead['website_score']}/100")
            print(f"🔥 Priority       : {lead['priority']}")
            print(f"📌 Status         : {lead['status']}")

            technology = lead.get("technology", [])

            if technology:
                print(f"💻 Technology     : {', '.join(technology)}")
            else:
                print("💻 Technology     : Not Detected")

            print("-" * 100)