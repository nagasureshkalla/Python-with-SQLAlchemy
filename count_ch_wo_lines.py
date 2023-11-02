"""

HW : 4
Problem : 2
Author : Kalla Naga Suresh

"""


def count_words_lines_characters(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

        # Count the number of words
        word_count = len(content.split())

        # Count the number of lines
        line_count = content.count('\n') + 1

        # Count the number of characters (including whitespace)
        char_count = len(content)

    return word_count, line_count, char_count

if __name__ == "__main__":
    file_path = input("Enter a filename: ")

    try:
        word_count, line_count, char_count = count_words_lines_characters(file_path)
        print(f"{char_count} characters")
        print(f"{word_count} words")
        print(f"{line_count} lines")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
