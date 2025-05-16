from stats import get_num_words, get_num_letters, get_sorted_letters
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")

    path = sys.argv[1]

    try:
        text = get_book_text(path)
    except FileNotFoundError as e:
        print("Please pass a path to a existing file")
        sys.exit(1)
    except IsADirectoryError as e:
        print("Please pass a path to a file")
        sys.exit(1)

    print(f"Analyzing book found at {path}")

    print("----------- Word Count ----------")

    words_num = get_num_words(text)
    print(f"Found {words_num} total words")

    letters_num = get_num_letters(text)
    sorted_letters = get_sorted_letters(letters_num)

    print("--------- Character Count -------")

    for letter_info in sorted_letters:
            print(f"{letter_info["char"]}: {letter_info["num"]}") 

    print("============= END ===============")


main()
