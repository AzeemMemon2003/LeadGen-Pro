from database.repository import LeadRepository


class LeadViewer:

    @staticmethod
    def show():

        repo = LeadRepository()

        leads = repo.all()

        if not leads:

            print("\n❌ No leads found.")

            return

        print("\n" + "=" * 90)

        for lead in leads:

            print(f"ID       : {lead[0]}")
            print(f"Company  : {lead[1]}")
            print(f"Website  : {lead[2]}")
            print(f"Email    : {lead[3]}")
            print(f"Score    : {lead[4]}")
            print(f"Priority : {lead[5]}")
            print(f"Status   : {lead[6]}")
            print("-" * 90)