class CRMMenu:

    @staticmethod
    def show():

        print("\n" + "=" * 65)
        print("🚀 LeadGen Pro CRM")
        print("=" * 65)

        print("1. Scan Websites")
        print("2. Search Leads")
        print("3. View All Leads")
        print("4. Update Lead Status")
        print("5. Export Excel")
        print("6. Exit")

        print("=" * 65)

        return input("Choice: ").strip()