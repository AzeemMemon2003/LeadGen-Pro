from pathlib import Path


class Settings:

    # Directories
    ROOT = Path(__file__).resolve().parent.parent

    DATA_DIR = ROOT / "data"

    OUTPUT_DIR = ROOT / "output"

    CAMPAIGN_DIR = OUTPUT_DIR / "campaigns"

    LOG_DIR = ROOT / "logs"

    # Database
    DATABASE = DATA_DIR / "leadgen.db"

    # Browser
    USER_AGENT = (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )

    REQUEST_TIMEOUT = 15

    CRAWL_LIMIT = 10

    # Excel
    EXCEL_FILE = OUTPUT_DIR / "leads.xlsx"

    # Reports
    REPORT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def create_directories(cls):

        cls.DATA_DIR.mkdir(exist_ok=True)

        cls.OUTPUT_DIR.mkdir(exist_ok=True)

        cls.CAMPAIGN_DIR.mkdir(exist_ok=True)

        cls.LOG_DIR.mkdir(exist_ok=True)

    # Browser

HEADLESS = True

BROWSER_TIMEOUT = 30000

USER_AGENT = (
    "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/138.0 Safari/537.36"
)