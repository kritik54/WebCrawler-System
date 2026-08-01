import unittest

class URLFrontier:
    def __init__(self):
        self.queue = []

    def enqueue(self, url):
        self.queue.append(url)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

class TestURLFrontier(unittest.TestCase):
    def test_enqueue(self):
        frontier = URLFrontier()
        frontier.enqueue("https://example.com")
        self.assertEqual(len(frontier.queue), 1)

    def test_dequeue(self):
        frontier = URLFrontier()
        frontier.enqueue("https://example.com")
        self.assertEqual(frontier.dequeue(), "https://example.com")

if __name__ == '__main__':
    unittest.main()