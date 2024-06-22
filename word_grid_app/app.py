import os
import tkinter as tk
from word_grid_app.ui.main_window import WordGridApp


def main():
    data_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'mots.txt')
    with open(data_file, 'r', encoding='utf-8') as file:
        valid_words = set(file.read().splitlines())

    root = tk.Tk()
    app = WordGridApp(root, valid_words)
    root.mainloop()


if __name__ == '__main__':
    main()
