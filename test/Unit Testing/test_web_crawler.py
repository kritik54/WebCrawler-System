import unittest

class WebCrawler:
    def download_page(self, url):
        return "<html><title>Test</title></html>"

class TestWebCrawler(unittest.TestCase):
    def test_download_page(self):
        crawler = WebCrawler()
        html = crawler.download_page("https://example.com")
        self.assertIn("<html>", html)

if __name__ == '__main__':
    unittest.main()