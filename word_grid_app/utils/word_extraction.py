def extract_words_from_grid(grid, valid_words):
    def extract_horizontal_words(grid):
        horizontal_words = []
        for row in grid:
            current_word = ""
            for char in row:
                if char != ' ':
                    current_word += char
                else:
                    if current_word:
                        horizontal_words.append(current_word.lower())
                        current_word = ""
            if current_word:
                horizontal_words.append(current_word.lower())
        return horizontal_words

    def extract_vertical_words(grid):
        vertical_words = []
        num_cols = len(grid[0])
        num_rows = len(grid)
        for col_idx in range(num_cols):
            current_word = ""
            for row_idx in range(num_rows):
                char = grid[row_idx][col_idx]
                if char != ' ':
                    current_word += char
                else:
                    if current_word:
                        vertical_words.append(current_word.lower())
                        current_word = ""
            if current_word:
                vertical_words.append(current_word.lower())
        return vertical_words

    horizontal_words = extract_horizontal_words(grid)
    vertical_words = extract_vertical_words(grid)

    valid_horizontal_words = [word for word in horizontal_words if word in valid_words]
    valid_vertical_words = [word for word in vertical_words if word in valid_words]

    return valid_horizontal_words, valid_vertical_words
