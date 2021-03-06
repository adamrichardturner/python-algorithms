import string

def ceaser_cipher(text, shift):
    """
    Shifts letters of the alphabet dependant in the string to decode or encode
    a message.
    """
    alphabet = string.ascii_lowercase
    return ''.join([alphabet[(alphabet.index(char.lower()) + shift) % 26] if char.lower() in alphabet else char.lower() for char in text])

plaintext = "Adam was here"
ciphered = "knkw gkc robo"
print(ceaser_cipher(plaintext, 10)) # knkw gkc robo
print(ceaser_cipher(ciphered, -10)) # adam was here