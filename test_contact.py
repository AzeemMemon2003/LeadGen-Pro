from scraper.browser import Browser
from scraper.contact_form import ContactFormExtractor

browser = Browser()
browser.start()

page = browser.open("https://python.org")

html = page.content()

result = ContactFormExtractor.extract(
    "https://python.org",
    html
)

print(result)

browser.stop()