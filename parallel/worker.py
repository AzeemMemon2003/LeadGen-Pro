from services.scan_service import ScanService


class Worker:

    @staticmethod
    def run(browser, website):

        try:

            return ScanService.scan(
                browser,
                website
            )

        except Exception as e:

            print(f"❌ {website}")

            print(e)

            return None