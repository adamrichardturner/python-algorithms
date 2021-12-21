import string

def ceaser_cipher(text, shift):
    """
    Shifts letters of the alphabet dependant in the string to decode or encode
    a message.
    """
    alphabet = string.ascii_lowercase
    return ''.join([alphabet[(alphabet.index(char) + shift) % 26] if char in alphabet else char for char in text])

ciphered = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
# hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!
print(ceaser_cipher(ciphered, 10))