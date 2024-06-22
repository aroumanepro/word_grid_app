import unittest
from word_grid_app.utils.word_finding import find_possible_words

class TestWordFinding(unittest.TestCase):
    def setUp(self):
        self.valid_words = {"hello", "world", "test"}

    def test_find_possible_words(self):
        letters = "helloworld"
        possible_words = find_possible_words(letters, self.valid_words, 9)
        self.assertIn("hello", possible_words)
        self.assertIn("world", possible_words)

if __name__ == '__main__':
    unittest.main()
