import requests


class Fetcher:

    @staticmethod
    def get(url, timeout=10):

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/137.0.0.0 Safari/537.36"
            )
        }

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=timeout,
                allow_redirects=True
            )

            if response.status_code == 200:

                return response.text

        except Exception:

            pass

        return ""