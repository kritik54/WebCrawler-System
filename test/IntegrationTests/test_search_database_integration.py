import unittest

class DatabaseManager:
    def query_jobs(self):
        return ["Backend Developer", "System Analyst"]

class SearchEngine:
    def search(self, keyword, jobs):
        return [j for j in jobs if keyword.lower() in j.lower()]

class TestSearchDatabaseIntegration(unittest.TestCase):
    def test_search_database_flow(self):
        db = DatabaseManager()
        search = SearchEngine()
        jobs = db.query_jobs()
        results = search.search("backend", jobs)
        self.assertEqual(results[0], "Backend Developer")

if __name__ == '__main__':
    unittest.main()