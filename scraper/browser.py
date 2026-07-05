from playwright.sync_api import sync_playwright
import time

from config.settings import Settings


class Browser:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):

        Settings.create_directories()

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=Settings.HEADLESS
        )

        self.context = self.browser.new_context(

            user_agent=Settings.USER_AGENT,

            viewport={
                "width": 1366,
                "height": 768
            }

        )

        self.page = self.context.new_page()

        self.page.set_default_timeout(
            Settings.BROWSER_TIMEOUT
        )

    def open(self, url):

        retries = 3

        for attempt in range(retries):

            try:

                self.page.goto(

                    url,

                    wait_until="domcontentloaded",

                    timeout=Settings.BROWSER_TIMEOUT

                )

                return self.page

            except Exception as e:

                print(
                    f"Retry {attempt + 1}/{retries}: {url}"
                )

                if attempt == retries - 1:
                    raise Exception(
                        f"Failed to open {url}\n{e}"
                    )

                time.sleep(2)

    def stop(self):

        if self.page:
            self.page.close()

        if self.context:
            self.context.close()

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()