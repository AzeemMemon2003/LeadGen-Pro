from playwright.sync_api import Page
import time


class BusinessOpener:

    @staticmethod
    def open(page: Page, business_name):

        cards = page.locator('a[href*="/place/"]')

        count = cards.count()

        for i in range(count):

            try:

                card = cards.nth(i)

                name = card.get_attribute("aria-label")

                if name != business_name:
                    continue

                print(f"\nOpening: {business_name}")

                card.click()

                page.wait_for_timeout(3000)

                return True

            except Exception:
                pass

        return False