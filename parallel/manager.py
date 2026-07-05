from concurrent.futures import ThreadPoolExecutor, as_completed

from parallel.worker import Worker


class ParallelManager:

    def __init__(self, max_workers=5):

        self.max_workers = max_workers

    def run(self, browser_factory, websites):

        results = []

        with ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:

            futures = {

                executor.submit(
                    Worker.run,
                    browser_factory(),
                    website
                ): website

                for website in websites

            }

            for future in as_completed(futures):

                result = future.result()

                if result:

                    results.append(result)

        return results