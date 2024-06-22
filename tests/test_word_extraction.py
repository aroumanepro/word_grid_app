import unittest
from word_grid_app.utils.word_extraction import extract_words_from_grid

class TestWordExtraction(unittest.TestCase):
    def setUp(self):
        self.valid_words = {"hello", "world", "test"}

    def test_extract_words_from_grid(self):
        grid = [
            ["H", "E", "L", "L", "O"],
            ["W", "O", "R", "L", "D"],
            ["T", "E", "S", "T", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]
        horizontal_words, vertical_words = extract_words_from_grid(grid, self.valid_words)
        self.assertIn("hello", horizontal_words)
        self.assertIn("world", horizontal_words)
        self.assertIn("test", horizontal_words)

if __name__ == '__main__':
    unittest.main()
