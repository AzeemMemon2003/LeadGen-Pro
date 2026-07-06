class DisposableVerifier:

    DISPOSABLE_DOMAINS = {

        "mailinator.com",
        "guerrillamail.com",
        "10minutemail.com",
        "tempmail.com",
        "temp-mail.org",
        "throwawaymail.com",
        "yopmail.com",
        "sharklasers.com",
        "dispostable.com",
        "maildrop.cc",
        "fakeinbox.com",
        "trashmail.com",
        "emailondeck.com",
        "mintemail.com",
        "getnada.com",
        "moakt.com"

    }

    @staticmethod
    def verify(email):

        if not email or "@" not in email:

            return {
                "disposable": False,
                "domain": ""
            }

        domain = email.split("@")[1].lower()

        return {

            "disposable": domain in DisposableVerifier.DISPOSABLE_DOMAINS,
            "domain": domain

        }