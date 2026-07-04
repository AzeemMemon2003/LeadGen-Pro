from search.search import SearchEngine


class SearchManager:

    def __init__(self):

        self.engine = SearchEngine()

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

        print(f"✅ Found {len(websites)} websites\n")

        return websites

    def from_csv(self):

        import pandas as pd

        df = pd.read_csv("input/websites.csv")

        return df["website"].dropna().tolist()