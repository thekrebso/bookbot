

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_number_words(text):
    return len(text.split())
    
def main():
    text = get_book_text("./books/frankenstein.txt")
    words_num = get_number_words(text)
    print(f"{words_num} words found in the document")

main()
