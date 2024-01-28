import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            req = urllib.request.Request(self.site, headers=headers)
            r = urllib.request.urlopen(req)
            html = r.read()
            parser = "html.parser"
            sp = BeautifulSoup(html, parser)
            print(sp.get_text())
        except Exception as e:
            print("Error: ", e)

# Example usage
robots_txt_url = "https://www.wikipedia.org/robots.txt"
Scraper(robots_txt_url).scrape()
