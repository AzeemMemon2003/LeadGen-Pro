from pathlib import Path


class Settings:

    ROOT = Path(__file__).resolve().parent.parent

    # -----------------------------
    # Directories
    # -----------------------------

    DATA_DIR = ROOT / "data"

    OUTPUT_DIR = ROOT / "output"

    CAMPAIGN_DIR = OUTPUT_DIR / "campaigns"

    LOG_DIR = ROOT / "logs"

    # -----------------------------
    # Database
    # -----------------------------

    DATABASE = DATA_DIR / "leadgen.db"

    # -----------------------------
    # Browser
    # -----------------------------

    HEADLESS = True

    BROWSER_TIMEOUT = 30000

    USER_AGENT = (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0.0.0 Safari/537.36"
    )

    # -----------------------------
    # Scanner
    # -----------------------------

    REQUEST_TIMEOUT = 15

    CRAWL_LIMIT = 10

    # -----------------------------
    # Excel
    # -----------------------------

    EXCEL_FILE = OUTPUT_DIR / "leads.xlsx"

    # -----------------------------
    # Helpers
    # -----------------------------

    @classmethod
    def create_directories(cls):

        cls.DATA_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        cls.OUTPUT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        cls.CAMPAIGN_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        cls.LOG_DIR.mkdir(
            parents=True,
            exist_ok=True
        )