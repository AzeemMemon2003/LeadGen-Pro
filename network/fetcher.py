import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from utils.logger import Logger


class Fetcher:

    _session = None

    @classmethod
    def session(cls):

        if cls._session is None:

            session = requests.Session()

            retry = Retry(
                total=2,
                connect=2,
                read=2,
                backoff_factor=0.5,
                status_forcelist=[
                    429,
                    500,
                    502,
                    503,
                    504
                ],
                allowed_methods=["GET"]
            )

            adapter = HTTPAdapter(
                max_retries=retry,
                pool_connections=20,
                pool_maxsize=20
            )

            session.mount("http://", adapter)
            session.mount("https://", adapter)

            session.headers.update({

                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/137.0.0.0 Safari/537.36"
                ),

                "Accept": (
                    "text/html,"
                    "application/xhtml+xml,"
                    "application/xml;q=0.9,*/*;q=0.8"
                ),

                "Accept-Language": "en-US,en;q=0.9",

                "Connection": "keep-alive"

            })

            cls._session = session

        return cls._session

    @classmethod
    def get(cls, url, timeout=10):

        logger = Logger.get_logger()

        try:

            response = cls.session().get(
                url,
                timeout=timeout,
                allow_redirects=True
            )

            if response.ok:

                return response.text

            logger.warning(
                f"HTTP {response.status_code}: {url}"
            )

        except requests.exceptions.Timeout:

            logger.warning(
                f"Timeout: {url}"
            )

        except requests.exceptions.RequestException as e:

            logger.warning(
                f"Request failed: {url} | {e}"
            )

        return ""