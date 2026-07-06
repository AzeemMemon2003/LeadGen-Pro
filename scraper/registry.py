from scraper.company import CompanyExtractor
from scraper.email import EmailExtractor
from scraper.phone import PhoneExtractor
from scraper.address import AddressExtractor
from scraper.tech import TechExtractor
from scraper.seo import SEOExtractor


EXTRACTORS = [

    CompanyExtractor,

    EmailExtractor,

    PhoneExtractor,

    AddressExtractor,

    TechExtractor,

    SEOExtractor

]