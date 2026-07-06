import re

from verification.domain import DomainVerifier
from verification.mx import MXVerifier
from verification.disposable import DisposableVerifier


class EmailVerifier:

    EMAIL_REGEX = re.compile(

        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    )

    ROLE_ACCOUNTS = {

        "info",
        "contact",
        "sales",
        "support",
        "hello",
        "office",
        "admin",
        "marketing"

    }

    @classmethod
    def verify(cls, email):

        result = {

            "email": email,
            "verified": False,
            "confidence": 0,

            "syntax_valid": False,
            "domain_valid": False,
            "mx_valid": False,

            "provider": "",
            "role_account": False,
            "disposable": False,

            "reasons": []

        }

        if not email:

            result["reasons"].append(
                "Email is empty"
            )

            return result

        email = email.strip().lower()

        # -----------------------------
        # Syntax
        # -----------------------------

        if not cls.EMAIL_REGEX.match(email):

            result["reasons"].append(
                "Invalid email syntax"
            )

            return result

        result["syntax_valid"] = True
        result["confidence"] += 25

        local, domain = email.split("@")

        # -----------------------------
        # Role account
        # -----------------------------

        if local in cls.ROLE_ACCOUNTS:

            result["role_account"] = True

            result["confidence"] += 5

        # -----------------------------
        # Disposable
        # -----------------------------

        disposable = DisposableVerifier.verify(
            email
        )

        result["disposable"] = disposable["disposable"]

        if result["disposable"]:

            result["reasons"].append(
                "Disposable email"
            )

            result["confidence"] -= 30

        # -----------------------------
        # Domain
        # -----------------------------

        domain_result = DomainVerifier.verify(
            domain
        )

        result["domain_valid"] = domain_result["valid"]

        if result["domain_valid"]:

            result["confidence"] += 25

        else:

            result["reasons"].append(
                "Domain not found"
            )

        # -----------------------------
        # MX
        # -----------------------------

        mx = MXVerifier.verify(
            domain
        )

        result["mx_valid"] = mx["valid"]
        result["provider"] = mx["provider"]

        if mx["valid"]:

            result["confidence"] += 45

        else:

            result["reasons"].append(
                "No MX records"
            )

        # -----------------------------
        # Final
        # -----------------------------

        result["confidence"] = max(
            0,
            min(
                100,
                result["confidence"]
            )
        )

        result["verified"] = (

            result["syntax_valid"]
            and result["domain_valid"]
            and result["mx_valid"]
            and not result["disposable"]

        )

        return result