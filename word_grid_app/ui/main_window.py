import tkinter as tk
from tkinter import messagebox
from word_grid_app.utils.word_extraction import extract_words_from_grid
from word_grid_app.utils.word_finding import find_possible_words, display_words_with_points


class WordGridApp:
    def __init__(self, root, valid_words):
        self.root = root
        self.valid_words = valid_words
        self.grid_entries = []
        self.letter_vars = []
        self.letter_entries = []

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Extraction de mots de la grille")

        config_frame = tk.Frame(self.root)
        config_frame.pack(pady=10)

        tk.Label(config_frame, text="Nombre de lignes:").grid(row=0, column=0, padx=5)
        self.rows_entry = tk.Entry(config_frame, width=5)
        self.rows_entry.grid(row=0, column=1, padx=5)

        tk.Label(config_frame, text="Nombre de colonnes:").grid(row=0, column=2, padx=5)
        self.cols_entry = tk.Entry(config_frame, width=5)
        self.cols_entry.grid(row=0, column=3, padx=5)

        create_button = tk.Button(config_frame, text="Créer la grille", command=self.create_grid)
        create_button.grid(row=0, column=4, padx=5)

        letters_config_frame = tk.Frame(self.root)
        letters_config_frame.pack(pady=10)

        tk.Label(letters_config_frame, text="Nombre de lettres:").grid(row=0, column=0, padx=5)
        self.num_letters_entry = tk.Entry(letters_config_frame, width=5)
        self.num_letters_entry.grid(row=0, column=1, padx=5)

        create_letters_button = tk.Button(letters_config_frame, text="Créer les inputs de lettres", command=self.create_letter_inputs)
        create_letters_button.grid(row=0, column=2, padx=5)

        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=10)

        self.grid_frame = tk.Frame(main_frame)
        self.grid_frame.grid(row=0, column=0, padx=10)

        extract_button = tk.Button(main_frame, text="Extraire les mots", command=self.on_extract_words)
        extract_button.grid(row=1, column=0, pady=10)

        self.result_listbox = tk.Listbox(main_frame, width=30, height=15)
        self.result_listbox.grid(row=0, column=1, rowspan=2, padx=10)

        self.letters_frame = tk.Frame(main_frame)  # Make letters_frame an instance attribute
        self.letters_frame.grid(row=2, column=0, pady=10)

        find_words_button = tk.Button(main_frame, text="Trouver les mots possibles", command=self.on_find_possible_words)
        find_words_button.grid(row=3, column=0, pady=10)

        self.possible_words_listbox = tk.Listbox(main_frame, width=30, height=10)
        self.possible_words_listbox.grid(row=2, column=1, rowspan=2, padx=10)

        find_completions_button = tk.Button(main_frame, text="Trouver les mots en complétant", command=self.find_completions)
        find_completions_button.grid(row=4, column=0, pady=10)

        self.completions_listbox = tk.Listbox(main_frame, width=30, height=10)
        self.completions_listbox.grid(row=4, column=1, padx=10)

        clean_all_button = tk.Button(main_frame, text="Tout nettoyer", command=self.clean_all)
        clean_all_button.grid(row=5, column=0, pady=10)

        clean_grid_button = tk.Button(main_frame, text="Nettoyer la grille", command=self.clean_grid)
        clean_grid_button.grid(row=5, column=1, pady=10)

        clean_letters_button = tk.Button(main_frame, text="Nettoyer les lettres", command=self.clean_letters)
        clean_letters_button.grid(row=5, column=2, pady=10)

    def create_grid(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        rows = int(self.rows_entry.get())
        cols = int(self.cols_entry.get())
        self.grid_entries = []
        for row in range(rows):
            row_entries = []
            for col in range(cols):
                var = tk.StringVar()
                entry = tk.Entry(self.grid_frame, width=2, justify='center', textvariable=var)
                entry.grid(row=row, column=col, padx=1, pady=1)
                entry.bind("<KeyRelease>", lambda e, var=var, row=row, col=col: self.on_key_release(var, row, col))
                row_entries.append(entry)
            self.grid_entries.append(row_entries)

    def on_key_release(self, var, row, col):
        value = var.get().upper()
        if value and not value.isalpha():
            var.set('')
        else:
            var.set(value)
            if len(value) == 1:
                next_row, next_col = row, col + 1
                if next_col >= len(self.grid_entries[0]):
                    next_row += 1
                    next_col = 0
                if next_row < len(self.grid_entries):
                    self.grid_entries[next_row][next_col].focus()

    def on_extract_words(self):
        grid = []
        for row_entries in self.grid_entries:
            row = []
            for entry in row_entries:
                row.append(entry.get().upper() if entry.get().isalpha() else ' ')
            grid.append(row)
        horizontal_words, vertical_words = extract_words_from_grid(grid, self.valid_words)
        self.result_listbox.delete(0, tk.END)
        self.result_listbox.insert(tk.END, "Mots horizontaux:")
        for word in horizontal_words:
            self.result_listbox.insert(tk.END, word)
        self.result_listbox.insert(tk.END, "Mots verticaux:")
        for word in vertical_words:
            self.result_listbox.insert(tk.END, word)

    def create_letter_inputs(self):
        for widget in self.letters_frame.winfo_children():
            widget.destroy()
        num_letters = int(self.num_letters_entry.get())
        self.letter_vars = [tk.StringVar() for _ in range(num_letters)]
        self.letter_entries = [tk.Entry(self.letters_frame, width=2, justify='center', textvariable=var) for var in self.letter_vars]
        for i, entry in enumerate(self.letter_entries):
            entry.grid(row=0, column=i, padx=5)
            entry.bind("<KeyRelease>", lambda e, var=self.letter_vars[i], idx=i: self.on_letter_key_release(var, idx))

    def on_letter_key_release(self, var, index):
        value = var.get().upper()
        if value and not value.isalpha():
            var.set('')
        else:
            var.set(value)
            if len(value) == 1 and index < len(self.letter_entries) - 1:
                self.letter_entries[index + 1].focus()

    def on_find_possible_words(self):
        letters = ''.join([var.get().lower() for var in self.letter_vars])
        if not letters.isalpha() or len(letters) < 1:
            messagebox.showerror("Erreur", "Veuillez entrer au moins une lettre.")
            return

        grid = []
        for row_entries in self.grid_entries:
            row = []
            for entry in row_entries:
                row.append(entry.get().upper() if entry.get().isalpha() else ' ')
            grid.append(row)

        horizontal_words, vertical_words = extract_words_from_grid(grid, self.valid_words)
        existing_words = set(horizontal_words + vertical_words)

        possible_words = find_possible_words(letters, self.valid_words, 9)

        possible_words = [word for word in possible_words if word not in existing_words]

        words_with_points = [(word, len(word)) for word in possible_words]

        display_words_with_points(self.possible_words_listbox, words_with_points)

    def find_completions(self):
        letters = ''.join([var.get().lower() for var in self.letter_vars])
        if not letters.isalpha() or len(letters) < 1:
            messagebox.showerror("Erreur", "Veuillez entrer au moins une lettre.")
            return

        grid = []
        for row_entries in self.grid_entries:
            row = []
            for entry in row_entries:
                row.append(entry.get().upper() if entry.get().isalpha() else ' ')
            grid.append(row)

        horizontal_words, vertical_words = extract_words_from_grid(grid, self.valid_words)
        possible_completions = []

        for word in horizontal_words:
            if len(word) > 2:
                for candidate in find_possible_words(word + letters, self.valid_words, 9):
                    if candidate.startswith(word) and len(candidate) > len(word):
                        possible_completions.append(candidate)
                for candidate in find_possible_words(letters + word, self.valid_words, 9):
                    if candidate.endswith(word) and len(candidate) > len(word):
                        possible_completions.append(candidate)

        for word in vertical_words:
            if len(word) > 2:
                for candidate in find_possible_words(word + letters, self.valid_words, 9):
                    if candidate.startswith(word) and len(candidate) > len(word):
                        possible_completions.append(candidate)
                for candidate in find_possible_words(letters + word, self.valid_words, 9):
                    if candidate.endswith(word) and len(candidate) > len(word):
                        possible_completions.append(candidate)

        completions_with_points = [(word, len(word)) for word in possible_completions]

        display_words_with_points(self.completions_listbox, completions_with_points)

    def clean_all(self):
        self.clean_grid()
        self.clean_letters()
        self.result_listbox.delete(0, tk.END)
        self.possible_words_listbox.delete(0, tk.END)
        self.completions_listbox.delete(0, tk.END)

    def clean_grid(self):
        for row_entries in self.grid_entries:
            for entry in row_entries:
                entry.delete(0, tk.END)

    def clean_letters(self):
        for var in self.letter_vars:
            var.set('')
