from stats import get_num_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

    
def main():
    text = get_book_text("./books/frankenstein.txt")
    words_num = get_num_words(text)
    print(f"{words_num} words found in the document")


main()
