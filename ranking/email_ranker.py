class EmailRanker:

    HIGH_PRIORITY = [
        "owner",
        "founder",
        "ceo",
        "director",
        "marketing",
        "sales",
        "hello",
        "contact",
        "business"
    ]

    MEDIUM_PRIORITY = [
        "info",
        "support",
        "help"
    ]

    LOW_PRIORITY = [
        "admin",
        "office",
        "team"
    ]

    IGNORE = [
        "privacy",
        "legal",
        "abuse",
        "security",
        "noreply",
        "no-reply",
        "webmaster",
        "hostmaster",
        "postmaster",
        "mailer-daemon"
    ]

    @classmethod
    def rank(cls, emails):

        if not emails:

            return {
                "primary": "",
                "backup": [],
                "ignored": []
            }

        primary = ""
        backups = []
        ignored = []

        ranked = []

        for email in emails:

            email = email.lower().strip()

            username = email.split("@")[0]

            if any(word in username for word in cls.IGNORE):

                ignored.append(email)

                continue

            score = 0

            if any(word in username for word in cls.HIGH_PRIORITY):
                score += 100

            elif any(word in username for word in cls.MEDIUM_PRIORITY):
                score += 70

            elif any(word in username for word in cls.LOW_PRIORITY):
                score += 40

            else:
                score += 90

            ranked.append((score, email))

        ranked.sort(reverse=True)

        if ranked:

            primary = ranked[0][1]

            backups = [email for _, email in ranked[1:]]

        return {

            "primary": primary,

            "backup": backups,

            "ignored": ignored
        }