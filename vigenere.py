import string

def vigenere(text, key):
    """
    Decrypts text using a keyword. We repeat the keyword the length of the text.
    Then we shift the characters in text by the place value of the key word.
    """
    alphabet = string.ascii_lowercase
    punctuation = '!.? '
    phrase = ''
    pointer = 0
    decoded = ''
    for char in range(0, len(text)):
        if text[char] in punctuation:
            phrase += text[char]
        else:
            phrase += key[pointer]
            pointer = (pointer + 1) % len(key)
    for i in range(0, len(text)):
        if not text[i] in punctuation:
            ln = alphabet.find(text[i]) - alphabet.find(phrase[i])
            decoded += alphabet[ln % 26]
        else:
            decoded += text[i]
    return decoded 

print(vigenere('dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!', 'friends'))
# you were able to decode this? nice work! you are becoming quite the expert at crytography!