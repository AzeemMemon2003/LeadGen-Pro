import socket
import dns.resolver


class DomainVerifier:

    @staticmethod
    def verify(domain):

        result = {
            "valid": False,
            "ip": "",
            "a_record": False,
            "aaaa_record": False
        }

        try:

            result["ip"] = socket.gethostbyname(domain)
            result["valid"] = True

        except Exception:
            return result

        try:

            dns.resolver.resolve(domain, "A")
            result["a_record"] = True

        except Exception:
            pass

        try:

            dns.resolver.resolve(domain, "AAAA")
            result["aaaa_record"] = True

        except Exception:
            pass

        return result