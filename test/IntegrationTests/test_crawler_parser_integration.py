import unittest
from bs4 import BeautifulSoup

class WebCrawler:
    def download_page(self, url):
        return "<html><title>Job Listing</title></html>"

class HTMLParser:
    def extract_title(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return soup.title.string

class TestCrawlerParserIntegration(unittest.TestCase):
    def test_crawler_parser_flow(self):
        crawler = WebCrawler()
        parser = HTMLParser()
        html = crawler.download_page("https://example.com")
        title = parser.extract_title(html)
        self.assertEqual(title, "Job Listing")

if __name__ == '__main__':
    unittest.main()