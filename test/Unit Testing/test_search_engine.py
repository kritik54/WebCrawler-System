import unittest

class SearchEngine:
    def search(self, keyword, data):
        return [item for item in data if keyword.lower() in item.lower()]

class TestSearchEngine(unittest.TestCase):
    def test_search(self):
        engine = SearchEngine()
        data = ["Software Engineer Nairobi", "Accountant Mombasa"]
        results = engine.search("software", data)
        self.assertEqual(len(results), 1)

if __name__ == '__main__':
    unittest.main()