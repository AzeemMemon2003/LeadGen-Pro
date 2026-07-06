class EmailRanker:

    PRIORITY = {

        "info": 100,
        "contact": 95,
        "sales": 90,
        "hello": 85,
        "support": 80,
        "office": 75,
        "marketing": 70,

        "owner": 60,
        "founder": 60,
        "ceo": 60,

        "admin": 40,

        "hr": 20,
        "careers": 20,
        "jobs": 20,
        "recruitment": 20

    }

    @classmethod
    def _score(cls, email):

        local = email.split("@")[0].lower()

        return cls.PRIORITY.get(local, 50)

    @classmethod
    def sort(cls, emails):

        if not emails:
            return []

        return sorted(
            set(emails),
            key=cls._score,
            reverse=True
        )

    @classmethod
    def best(cls, emails):

        ranked = cls.sort(emails)

        if ranked:
            return ranked[0]

        return ""

    @classmethod
    def rank(cls, emails):

        ranked = cls.sort(emails)

        if not ranked:

            return {
                "primary": "",
                "backup": [],
                "ignored": []
            }

        return {

            "primary": ranked[0],

            "backup": ranked[1:],

            "ignored": []

        }