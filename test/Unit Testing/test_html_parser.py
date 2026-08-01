import unittest
from bs4 import BeautifulSoup

class HTMLParser:
    def extract_title(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return soup.title.string

class TestHTMLParser(unittest.TestCase):
    def test_extract_title(self):
        parser = HTMLParser()
        html = "<html><title>Software Engineer</title></html>"
        self.assertEqual(parser.extract_title(html), "Software Engineer")

if __name__ == '__main__':
    unittest.main()