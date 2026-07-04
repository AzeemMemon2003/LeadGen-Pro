class EmailRanker:

    SCORES = {
        "contact": 100,
        "sales": 95,
        "hello": 90,
        "info": 85,
        "support": 70,
        "marketing": 65,
        "admin": 40,
        "office": 35,
        "careers": 20,
        "jobs": 20,
        "legal": 10,
        "privacy": 5,
        "noreply": 0,
        "no-reply": 0
    }

    @classmethod
    def score(cls, email):

        local = email.split("@")[0].lower()

        for key, value in cls.SCORES.items():

            if key in local:

                return value

        return 50

    @classmethod
    def rank(cls, emails):

        if not emails:

            return {
                "primary": "",
                "backup": [],
                "ignored": []
            }

        ranked = sorted(
            emails,
            key=lambda x: cls.score(x),
            reverse=True
        )

        ignored = []

        cleaned = []

        for email in ranked:

            if cls.score(email) == 0:

                ignored.append(email)

            else:

                cleaned.append(email)

        return {
            "primary": cleaned[0] if cleaned else "",
            "backup": cleaned[1:],
            "ignored": ignored
        }