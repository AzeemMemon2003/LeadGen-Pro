import pandas as pd
from urllib.parse import urlparse

from search.search import SearchEngine
from maps.google_maps import GoogleMaps
from helpers.url_helper import URLHelper


class SearchManager:

    BLOCKED_DOMAINS = {

        "facebook.com",
        "m.facebook.com",
        "linkedin.com",
        "instagram.com",
        "twitter.com",
        "x.com",
        "youtube.com",
        "youtu.be",
        "reddit.com",
        "wikipedia.org",
        "medium.com",
        "quora.com",
        "pinterest.com",
        "tiktok.com",
        "amazon.com",
        "ebay.com"

    }

    BLOCKED_KEYWORDS = [

        "/blog",
        "/blogs",
        "/news",
        "/article",
        "/articles",
        "/category",
        "/tag",
        "/search",
        "/privacy",
        "/terms",
        "/careers",
        "/jobs"

    ]

    def __init__(self):

        self.engine = SearchEngine()
        self.maps = GoogleMaps()

    def menu(self):

        print("\nSelect Input Mode")
        print("1. CSV File")
        print("2. Keyword Search")
        print("3. Google Maps")

        choice = input("\nChoice (1/2/3): ").strip()

        if choice == "1":
            websites = self.from_csv()

        elif choice == "2":
            websites = self.by_keyword()

        elif choice == "3":
            websites = self.by_maps()

        else:
            print("Invalid Choice.")
            return []

        websites = self.clean_websites(websites)

        print(f"\n✅ Unique Business Websites: {len(websites)}")

        return websites

    def from_csv(self):

        df = pd.read_csv("input/websites.csv")

        return df["website"].dropna().tolist()

    def by_keyword(self):

        keyword = input("\nKeyword: ").strip()

        if not keyword:
            print("Keyword cannot be empty.")
            return []

        print("\n🔍 Searching Google...")

        return self.engine.search(
            keyword,
            max_results=20
        )

    def by_maps(self):

        keyword = input("\nBusiness Type: ").strip()

        city = input("City: ").strip()

        limit = input("Results (default 10): ").strip()

        limit = int(limit) if limit else 10

        businesses = self.maps.search(
            keyword=keyword,
            city=city,
            limit=limit
        )

        websites = []

        for business in businesses:

            website = business.get("website", "").strip()

            if website:
                websites.append(website)

        return websites

    def clean_websites(self, websites):

        cleaned = []

        for website in websites:

            if not website:
                continue

            website = website.strip()

            try:

                parsed = urlparse(website)

                domain = parsed.netloc.lower().replace("www.", "")

                path = parsed.path.lower()

            except Exception:
                continue

            if any(blocked in domain for blocked in self.BLOCKED_DOMAINS):
                continue

            if any(keyword in path for keyword in self.BLOCKED_KEYWORDS):
                continue

            cleaned.append(website)

        return URLHelper.remove_duplicates(cleaned)