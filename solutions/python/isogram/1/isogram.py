import string 
def is_isogram(phrase):
    letters_found = set()
    for char in phrase:
        new_char = char.lower()
        if new_char.isalpha():
            if new_char in letters_found:
                return False
            letters_found.add(new_char)
    return True