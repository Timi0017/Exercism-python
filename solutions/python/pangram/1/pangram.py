import string
def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    letters_found = set()
    for char in sentence:
        new_char = char.lower()
        if new_char.isalpha():
            letters_found.add(new_char)

    if letters_found == alphabet:
        return True
    return False