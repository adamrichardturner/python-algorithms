import string

def ceaser_cipher(text, shift):
    """
    Shifts letters of the alphabet dependant in the string to decode or encode
    a message.
    """
    alphabet = string.ascii_lowercase
    return ''.join([alphabet[(alphabet.index(char.lower()) + shift) % 26] if char.lower() in alphabet else char.lower() for char in text])

def brute_force_ceaser(text):
    for shift in range(26):
        print(ceaser_cipher(text, shift))

brute_force_ceaser("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")