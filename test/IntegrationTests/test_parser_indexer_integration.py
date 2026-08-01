import unittest

class HTMLParser:
    def extract_job(self):
        return "Software Engineer"

class Indexer:
    def create_index(self, title):
        return {"title": title}

class TestParserIndexerIntegration(unittest.TestCase):
    def test_parser_to_indexer(self):
        parser = HTMLParser()
        indexer = Indexer()
        title = parser.extract_job()
        indexed = indexer.create_index(title)
        self.assertEqual(indexed["title"], "Software Engineer")

if __name__ == '__main__':
    unittest.main()