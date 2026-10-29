##function for single words
def translate_word(text):
    ##rule one, words that begin with certain phrases, the function then adds "ay" at the end
    if text.startswith(('xr', 'yt', 'a', 'e', 'i', 'o', 'u')):
        text += "ay"
        return text
    ##rule 2&3, words that start with zero or more consonants followed by "qu". the function uses a for loop to go through the entire word till it lands on a vowel with an exception of "u" if it is preceeded by "q" via the if statement, the function then slices the consonants out with "qu". the consonants are moved to the end of the sentence and followed by "qu" and then "ay" is added
    vowel = "aeiou"
    for index, letter in enumerate(text):
        if letter.lower() == 'u' and index > 0 and text[index - 1].lower() == 'q':
            return text[index + 1:] + text[:index + 1] + "ay"
    ## rule 4 is for words that start with consonants followed by "y". it is moved to the end and "ay" is added to it
        elif letter.lower() in vowel or (letter.lower() == 'y' and index > 0):
            return text[index:] + text[:index] + "ay"
    return text

##this function is for sentences and phrases for the last test case. the sentences are split into pieces in other to carry out the slice and move function. it is then joined back together 
def translate(text):
    translated_word = []
    for word in text.split():
        translated_word.append(translate_word(word))
    return " ".join(translated_word)

