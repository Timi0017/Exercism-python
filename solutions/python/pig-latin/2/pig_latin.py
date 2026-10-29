"""Translate English text into Pig Latin."""
def translate_word(text):
    """Translate a single word into Pig Latin."""
    if text.startswith(('xr', 'yt', 'a', 'e', 'i', 'o', 'u')):
        return text + 'ay'

    vowel = 'aeiou'
    for index, letter in enumerate(text):
        if letter.lower() == 'u' and index > 0 and text[index - 1].lower() == 'q':
            return text[index + 1:] + text[:index + 1] + 'ay'

        if letter.lower() in vowel or (letter.lower() == 'y' and index > 0):
            return text[index:] + text[:index] + 'ay'
    return text

def translate(text):
    """Translate phrases into Pig Latin using the translate_word function."""
    translated_words = []
    for word in text.split():
        translated_words.append(translate_word(word))
    return ' '.join(translated_words)