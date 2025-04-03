from stats import count_words, char_dict_from, dict_to_sorted_list
from sys import argv, exit

def get_book_text(filepath):
    with open(filepath) as book:
        return book.read()
    
def print_report(word_count, letter_count_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in letter_count_list:
        char = dict["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {dict["count"]}")
    print("============= END ===============")
    
def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_text = get_book_text(argv[1])
    word_count = count_words(book_text)
    letter_count_sorted = dict_to_sorted_list(char_dict_from(book_text))
    print(str(word_count) + " words found in the document")
    print_report(word_count, letter_count_sorted)

main()