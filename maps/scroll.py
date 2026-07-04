from playwright.sync_api import Page
import time


class MapsScroller:

    @staticmethod
    def scroll(page: Page, rounds=15):

        print("\n🗺 Scrolling Google Maps...")

        panel = page.locator('div[role="main"]')

        panel.wait_for(timeout=10000)

        for i in range(rounds):

            page.mouse.move(250, 500)

            page.mouse.wheel(0, 3000)

            time.sleep(2)

            print(f"Scroll {i+1}/{rounds}")

        print("✅ Scrolling Finished")