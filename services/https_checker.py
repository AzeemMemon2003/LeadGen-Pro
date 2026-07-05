from urllib.parse import urlparse

import requests


class HTTPSChecker:
    @staticmethod
    def check(url: str) -> dict:
        result = {
            "https": False,
            "redirect": False,
            "status_code": None,
            "error": None,
        }

        try:
            response = requests.get(
                url,
                timeout=10,
                allow_redirects=True,
                headers={
                    "User-Agent": "Mozilla/5.0"
                },
            )

            result["status_code"] = response.status_code
            result["https"] = response.url.startswith("https://")

            original = urlparse(url)
            final = urlparse(response.url)

            if original.scheme == "http" and final.scheme == "https":
                result["redirect"] = True

        except Exception as e:
            result["error"] = str(e)

        return result


# 👇 YE BILKUL FILE KE END MEIN ADD KARO
if __name__ == "__main__":
    print(HTTPSChecker.check("http://github.com"))