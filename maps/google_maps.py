from urllib.parse import quote_plus

from scraper.browser import Browser
from maps.scroll import MapsScroller
from maps.parser import MapsParser


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

        page.wait_for_timeout(5000)

        MapsScroller.scroll(page)

        businesses = MapsParser.get_businesses(page)

        print("\nBusinesses Found:\n")

        for i, business in enumerate(businesses, start=1):

            print(f"{i}. {business}")

        input("\nPress ENTER to close browser...")

        self.browser.stop()