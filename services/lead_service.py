from scanner import Scanner


class LeadService:

    @staticmethod
    def scan_websites(websites):

        return Scanner.run_websites(websites)

    @staticmethod
    def scan_website(browser, website):

        return Scanner.scan(browser, website)