from stats import get_num_words, get_num_letters, get_sorted_letters


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    print("============ BOOKBOT ============")

    PATH = "./books/frankenstein.txt"

    print(f"Analyzing book found at {PATH}")

    text = get_book_text(PATH)

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
