from playwright.sync_api import sync_playwright


class Browser:

    def __init__(self):
        self.playwright = None
        self.browser = None

    def start(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

    def open(self, url):

        page = self.browser.new_page()

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

        return page

    def stop(self):

        self.browser.close()

        self.playwright.stop()