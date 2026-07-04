from playwright.sync_api import Page


class MapsParser:

    @staticmethod
    def get_businesses(page: Page):

        businesses = []

        cards = page.locator('a[href*="/place/"]')

        count = cards.count()

        print(f"\nFound {count} business cards")

        for i in range(count):

            try:

                card = cards.nth(i)

                name = card.get_attribute("aria-label")

                if not name:
                    continue

                if name not in businesses:
                    businesses.append(name)

            except Exception:
                pass

        return businesses