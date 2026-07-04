from playwright.sync_api import sync_playwright
import config


class Browser:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=config.HEADLESS
        )

        self.context = self.browser.new_context()

        self.page = self.context.new_page()

    def open(self, url):

        self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=config.TIMEOUT
        )

        return self.page

    def stop(self):

        self.browser.close()

        self.playwright.stop()