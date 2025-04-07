import sys

from stats import get_num_words
from stats import get_char_count
from stats import get_sort_dicts
from stats import sort_on_count

def get_book_text (path_to_file):
    file_contents = None
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main ():
    if len(sys.argv) != 2:
        print("Incorrect number of parameters passed!")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    char_count_list = get_sort_dicts(char_count)
    char_count_list.sort(reverse=True, key=sort_on_count)

    print( "============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print( "----------- Word Count ----------")
    print(f"Found {book_word_count} total words")
    print( "--------- Character Count -------")
    for char_count in char_count_list:
        if char_count["char"].isalpha():
            print(f"{char_count["char"]}: {char_count["num"]}")

    print( "============= END ===============")

main()
