import sys
from stats import calculate_words, calculate_characters, sort_dictionary

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = calculate_words(text)
    print(f"Found {num_words} total words")
    num_characters = calculate_characters(text)
    sorted = sort_dictionary(num_characters)
    for dict in sorted:
        print(dict["char"] + ": " + str(dict["num"]))

if __name__ == "__main__":
    main()
