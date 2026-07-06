import dns.resolver


class MXVerifier:

    @staticmethod
    def verify(domain):

        result = {
            "valid": False,
            "provider": "",
            "records": []
        }

        try:

            answers = dns.resolver.resolve(
                domain,
                "MX"
            )

            records = []

            for record in answers:

                host = str(record.exchange).rstrip(".")

                records.append(host)

            provider = MXVerifier.detect_provider(
                records
            )

            result["valid"] = len(records) > 0
            result["provider"] = provider
            result["records"] = records

        except Exception:

            pass

        return result

    @staticmethod
    def detect_provider(records):

        joined = " ".join(records).lower()

        providers = {

            "Google Workspace": [
                "google.com",
                "googlemail.com",
                "aspmx"
            ],

            "Microsoft 365": [
                "outlook.com",
                "protection.outlook"
            ],

            "Zoho Mail": [
                "zoho"
            ],

            "Amazon SES": [
                "amazonses"
            ],

            "Proofpoint": [
                "proofpoint"
            ],

            "Mimecast": [
                "mimecast"
            ],

            "Cloudflare Email": [
                "cloudflare"
            ]

        }

        for provider, keywords in providers.items():

            if any(
                keyword in joined
                for keyword in keywords
            ):
                return provider

        return "Unknown"