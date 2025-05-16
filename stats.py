
def get_num_words(text):
    return len(text.split())


def get_num_letters(text):
    letters = {}

    for letter in text:
        letter = letter.lower()

        if letter in letters:
              letters[letter] += 1
        else:
            letters[letter] = 1

    return letters


def get_sorted_letters(letters):
    result = []

    for letter in letters:
        if letter.isalpha():
            result.append({ "char": letter, "num": letters[letter] })

    result.sort(reverse=True, key=lambda x: x["num"])

    return result
