from urllib.parse import quote_plus

from scraper.browser import Browser
from maps.scroll import MapsScroller
from maps.parser import MapsParser
from maps.business import BusinessOpener
from maps.details import BusinessDetails


class GoogleMaps:

    def __init__(self):

        self.browser = Browser()

    def search(self, keyword, city, limit=10):

        self.browser.start()

        query = quote_plus(f"{keyword} {city}")

        url = f"https://www.google.com/maps/search/{query}"

        page = self.browser.open(url)

        print("\n🚀 Google Maps Started")

        page.wait_for_timeout(5000)

        MapsScroller.scroll(page)

        businesses = MapsParser.get_businesses(page)

        if not businesses:

            print("No businesses found.")

            self.browser.stop()

            return []

        print(f"\nFound {len(businesses)} businesses")

        results = []

        for business in businesses[:limit]:

            print("\n" + "=" * 60)
            print(f"Opening: {business}")
            print("=" * 60)

            opened = BusinessOpener.open(
                page,
                business
            )

            if not opened:

                print("Unable to open business.")

                continue

            page.wait_for_timeout(2000)

            details = BusinessDetails.extract(page)

            results.append(details)

            print(f"Business : {details['name']}")
            print(f"Website  : {details['website']}")
            print(f"Phone    : {details['phone']}")
            print(f"Address  : {details['address']}")
            print(f"Rating   : {details['rating']}")
            print(f"Reviews  : {details['reviews']}")

            # Go back to results list
            page.go_back()

            page.wait_for_timeout(3000)

        input("\nPress ENTER to close browser...")

        self.browser.stop()

        return results