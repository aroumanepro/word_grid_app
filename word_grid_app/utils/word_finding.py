import tkinter as tk
from collections import Counter


def find_possible_words(letters, words, max_word_length):
    letters_counter = Counter(letters)
    possible_words = []

    for word in words:
        if len(word) <= max_word_length:
            word_counter = Counter(word)
            if not word_counter - letters_counter:
                possible_words.append(word)

    possible_words.sort(key=len, reverse=True)
    return possible_words


def display_words_with_points(listbox, words):
    listbox.delete(0, tk.END)
    sorted_words = sorted(words, key=lambda x: x[1], reverse=True)
    for word, points in sorted_words:
        listbox.insert(tk.END, f"{word} - {points} points")
