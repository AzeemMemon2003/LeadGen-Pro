class ReportService:

    @staticmethod
    def print(result):

        print(f"🏢 Company : {result['company']}")
        print(f"📧 Emails  : {len(result['emails'])}")
        print(f"📞 Phones  : {len(result['phones'])}")
        print(f"📍 Address : {len(result['addresses'])}")
        print(f"💻 Tech    : {', '.join(result['technology'])}")

        seo = result["seo"]

        print("\n📊 SEO Audit")
        print(f"Title             : {'✅' if seo['title'] else '❌'}")
        print(f"Meta Description  : {'✅' if seo['meta_description'] else '❌'}")
        print(f"H1                : {'✅' if seo['h1'] else '❌'}")
        print(f"Images without ALT: {seo['images_without_alt']}")

        score = result["score"]

        print("\n⭐ Lead Score")
        print(f"Score : {score['score']}/100")

        if score["opportunities"]:

            print("\nOpportunities:")

            for item in score["opportunities"]:

                print(f"• {item}")