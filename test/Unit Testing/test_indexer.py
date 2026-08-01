import unittest

class Indexer:
    def create_index(self, job_title):
        return {"title": job_title}

class TestIndexer(unittest.TestCase):
    def test_create_index(self):
        indexer = Indexer()
        result = indexer.create_index("Backend Developer")
        self.assertEqual(result["title"], "Backend Developer")

if __name__ == '__main__':
    unittest.main()