import unittest
from tkinter import Tk
from word_grid_app.ui.main_window import WordGridApp

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.valid_words = {"hello", "world", "test"}
        self.app = WordGridApp(self.root, self.valid_words)

    def test_create_grid(self):
        self.app.rows_entry.insert(0, "5")
        self.app.cols_entry.insert(0, "5")
        self.app.create_grid()
        self.assertEqual(len(self.app.grid_entries), 5)
        self.assertEqual(len(self.app.grid_entries[0]), 5)

if __name__ == '__main__':
    unittest.main()
