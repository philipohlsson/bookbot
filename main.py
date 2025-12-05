import sys
from stats import get_num_words, get_each_character, sort_character_counts

    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    characters = get_each_character(text)
    sorted_list = sort_character_counts(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
