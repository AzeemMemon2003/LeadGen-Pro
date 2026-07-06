from scanner import Scanner

from crm.menu import CRMMenu
from crm.view import LeadViewer
from crm.status import LeadStatus



def main():

    scanner = Scanner()

    while True:

        choice = CRMMenu.show()

        if choice == "1":

            scanner.run()

        elif choice == "2":

            from search_leads import repo

            print()

            keyword = input("Enter company or website: ").strip()

            results = repo.search(keyword)

            if not results:

                print("\n❌ No leads found.")

            else:

                print()

                for lead in results:

                    print("-" * 60)
                    print(f"ID       : {lead[0]}")
                    print(f"Company  : {lead[1]}")
                    print(f"Website  : {lead[2]}")
                    print(f"Email    : {lead[3]}")
                    print(f"Score    : {lead[4]}")
                    print(f"Priority : {lead[5]}")
                    print(f"Status   : {lead[6]}")

        elif choice == "3":

            LeadViewer.show()

        elif choice == "4":

            LeadStatus.update()

        elif choice == "5":

            print("\n⚠️ Excel export already happens after every scan.")

        elif choice == "6":

            print("\n👋 Goodbye!")

            break

        else:

            print("\n❌ Invalid option.")


if __name__ == "__main__":
    main()