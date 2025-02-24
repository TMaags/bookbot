from stats import count_words, count_characters, sorted_characters
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Include filepath: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    num_words = count_words(book)
    num_characters = count_characters(book)
    sorted_chars = sorted_characters(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_chars:
        key = list(dict.keys())[0]
        count = list(dict.values())[0]
        print(f"{key}: {count}")
    print("============= END ===============")
main()