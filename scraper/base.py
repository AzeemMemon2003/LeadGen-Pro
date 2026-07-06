class BaseExtractor:

    name = ""

    @staticmethod
    def extract(page, html):
        raise NotImplementedError