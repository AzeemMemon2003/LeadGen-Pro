from datetime import datetime


class JSONBuilder:

    @staticmethod
    def build(results):

        return {

            "generated_at": datetime.now().isoformat(),

            "generator": "LeadGen Pro",

            "version": "4.0",

            "total_leads": len(results),

            "leads": [

                {

                    "company": lead.get("company", ""),

                    "website": lead.get("website", ""),

                    "title": lead.get("title", ""),

                    "contact": {

                        "primary_email":
                            lead.get("contact", {}).get("primary_email", ""),

                        "backup_emails":
                            lead.get("contact", {}).get("backup_emails", []),

                        "primary_phone":
                            lead.get("contact", {}).get("primary_phone", ""),

                        "backup_phones":
                            lead.get("contact", {}).get("backup_phones", []),

                        "head_office":
                            lead.get("contact", {}).get("head_office", ""),

                        "linkedin":
                            lead.get("contact", {}).get("linkedin", ""),

                        "confidence":
                            lead.get("contact", {}).get("confidence", 0)

                    },

                    "qualification":
                        lead.get("qualification", {}),

                    "seo":
                        lead.get("seo", {}),

                    "technology":
                        lead.get("technology", []),

                    "opportunity":
                        lead.get("opportunity", {})

                }

                for lead in results

            ]

        }