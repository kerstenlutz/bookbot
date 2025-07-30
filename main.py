import sys

from stats import get_book_text
from stats import word_count
from stats import letter_counter
from stats import sort_on
from stats import sort_dict

def main():
    sys.argv
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    user_book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {user_book_path}")
    print("----------- Word Count ----------")
    text = get_book_text(user_book_path)
    num_words = word_count(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = letter_counter(text)
    dict_chars = sort_dict(num_chars)
    for dict_char in dict_chars:
        print(f"{dict_char["char"]}: {dict_char["num"]}" )
    print("============= END ===============")

main()


