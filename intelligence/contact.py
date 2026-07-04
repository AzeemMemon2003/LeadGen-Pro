from ranking.email_ranker import EmailRanker


class ContactIntelligence:

    @staticmethod
    def build(result):

        email_rank = EmailRanker.rank(result["emails"])

        phones = sorted(set(result["phones"]))

        addresses = sorted(set(result["addresses"]))

        contact = {

            "primary_email": email_rank["primary"],

            "backup_emails": email_rank["backup"],

            "ignored_emails": email_rank["ignored"],

            "primary_phone": phones[0] if phones else "",

            "backup_phones": phones[1:] if len(phones) > 1 else [],

            "head_office": addresses[0] if addresses else "",

            "other_addresses": addresses[1:] if len(addresses) > 1 else [],

            "contact_page": "",

            "linkedin": result["social"].get("linkedin", ""),

            "facebook": result["social"].get("facebook", ""),

            "instagram": result["social"].get("instagram", ""),

            "twitter": result["social"].get("twitter", ""),

            "whatsapp": "",

            "confidence": 0

        }

        confidence = 0

        if contact["primary_email"]:
            confidence += 35

        if contact["primary_phone"]:
            confidence += 25

        if contact["head_office"]:
            confidence += 20

        if contact["linkedin"]:
            confidence += 10

        if result["crawl_pages"]:
            confidence += 10

        contact["confidence"] = min(confidence, 100)

        return contact