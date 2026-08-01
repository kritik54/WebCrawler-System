import unittest
import hashlib

class DuplicateDetector:
    def generate_hash(self, content):
        return hashlib.sha256(content.encode()).hexdigest()

class TestDuplicateDetector(unittest.TestCase):
    def test_generate_hash(self):
        detector = DuplicateDetector()
        h1 = detector.generate_hash("sample content")
        h2 = detector.generate_hash("sample content")
        self.assertEqual(h1, h2)

if __name__ == '__main__':
    unittest.main()