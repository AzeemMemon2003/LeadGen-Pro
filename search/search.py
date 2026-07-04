from ddgs import DDGS


class SearchEngine:

    def search(self, keyword, max_results=20):

        websites = []

        with DDGS() as ddgs:

            results = ddgs.text(
                keyword,
                max_results=max_results
            )

            for result in results:

                url = result.get("href") or result.get("url")

                if not url:
                    continue

                if url not in websites:
                    websites.append(url)

        return websites