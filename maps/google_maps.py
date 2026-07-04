from urllib.parse import quote_plus

from scraper.browser import Browser


class GoogleMaps:

    def __init__(self):

        self.browser = Browser()

    def search(self, keyword, city):

        self.browser.start()

        query = quote_plus(f"{keyword} {city}")

        url = f"https://www.google.com/maps/search/{query}"

        page = self.browser.open(url)

        print("\nGoogle Maps Opened Successfully")

        print(page.title())

        input("\nPress ENTER to close browser...")

        self.browser.stop()