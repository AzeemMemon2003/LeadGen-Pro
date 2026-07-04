class ReportService:

    @staticmethod
    def print(result):

        print(f"🏢 Company : {result['company']}")
        print(f"🌐 Website : {result['website']}")
        print(f"💻 Tech    : {', '.join(result['technology'])}")

        contact = result.get("contact", {})

        print("\n📇 Contact Intelligence")
        print(f"Primary Email : {contact.get('primary_email', 'Not Found')}")
        print(f"Primary Phone : {contact.get('primary_phone', 'Not Found')}")
        print(f"Head Office   : {contact.get('head_office', 'Not Found')}")
        print(f"Confidence    : {contact.get('confidence', 0)}%")

        backup_emails = contact.get("backup_emails", [])
        backup_phones = contact.get("backup_phones", [])

        print(f"Backup Emails : {len(backup_emails)}")
        print(f"Backup Phones : {len(backup_phones)}")

        seo = result["seo"]

        print("\n📊 SEO Audit")
        print(f"Title             : {'✅' if seo['title'] else '❌'}")
        print(f"Meta Description  : {'✅' if seo['meta_description'] else '❌'}")
        print(f"H1                : {'✅' if seo['h1'] else '❌'}")
        print(f"Images without ALT: {seo['images_without_alt']}")

        qualification = result["qualification"]

        print("\n⭐ Lead Qualification")
        print(f"Score    : {qualification['score']}/100")
        print(f"Priority : {qualification['priority']}")

        if qualification["reasons"]:

            print("\nReasons:")

            for reason in qualification["reasons"]:

                print(f"✔ {reason}")

        opportunity = result["opportunity"]

        print("\n💼 Sales Opportunity")
        print(f"Priority : {opportunity['priority']}")
        print(f"\nSummary : {opportunity['summary']}")

        if opportunity["problems"]:

            print("\nProblems:")

            for problem in opportunity["problems"]:

                print(f"• {problem}")

        if opportunity["services"]:

            print("\nRecommended Services:")

            for service in opportunity["services"]:

                print(f"✅ {service}")