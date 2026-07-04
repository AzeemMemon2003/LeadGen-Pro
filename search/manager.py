import pandas as pd

from search.search import SearchEngine
from maps.google_maps import GoogleMaps


class SearchManager:

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
            return self.from_csv()

        elif choice == "2":
            return self.by_keyword()

        elif choice == "3":
            return self.by_maps()

        print("Invalid Choice.")

        return []

    def from_csv(self):

        df = pd.read_csv("input/websites.csv")

        return df["website"].dropna().tolist()

    def by_keyword(self):

        keyword = input("\nKeyword: ").strip()

        if not keyword:

            print("Keyword cannot be empty.")

            return []

        print("\n🔍 Searching...")

        websites = self.engine.search(
            keyword,
            max_results=20
        )

        print(f"\n✅ Found {len(websites)} websites")

        return websites

    def by_maps(self):

        keyword = input("\nBusiness Type: ").strip()

        city = input("City: ").strip()

        limit = input("Results (default 10): ").strip()

        if not limit:

            limit = 10

        else:

            limit = int(limit)

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

        print(f"\n🌍 Websites Found: {len(websites)}")

        return websites