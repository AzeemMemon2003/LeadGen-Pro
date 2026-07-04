from playwright.sync_api import Page


class BusinessDetails:

    @staticmethod
    def extract(page: Page):

        data = {
            "name": "",
            "website": "",
            "phone": "",
            "address": "",
            "rating": "",
            "reviews": ""
        }

        # -------------------------
        # Business Name
        # -------------------------
        try:

            title = page.locator("h1")

            if title.count() > 0:
                data["name"] = title.first.inner_text().strip()

        except:
            pass

        # -------------------------
        # Website
        # -------------------------
        try:

            website = page.locator('a[data-item-id="authority"]')

            if website.count() > 0:

                href = website.first.get_attribute("href")

                if href:
                    data["website"] = href

        except:
            pass

        # -------------------------
        # Phone
        # -------------------------
        try:

            phone = page.locator('button[data-item-id^="phone"]')

            if phone.count() > 0:

                data["phone"] = phone.first.inner_text().strip()

        except:
            pass

        # -------------------------
        # Address
        # -------------------------
        try:

            address = page.locator('button[data-item-id="address"]')

            if address.count() > 0:

                data["address"] = address.first.inner_text().strip()

        except:
            pass

        # -------------------------
        # Rating
        # -------------------------
        try:

            rating = page.locator('div[role="main"] span[aria-hidden="true"]')

            if rating.count() > 0:

                value = rating.first.inner_text().strip()

                if value.replace(".", "").isdigit():
                    data["rating"] = value

        except:
            pass

        # -------------------------
        # Reviews
        # -------------------------
        try:

            reviews = page.locator(
                'button[jsaction*="pane.reviewChart.moreReviews"]'
            )

            if reviews.count() > 0:

                data["reviews"] = reviews.first.inner_text().strip()

        except:
            pass

        return data