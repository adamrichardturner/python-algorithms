def rot13(message):
    """
    How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
    I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?

    Hint: For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers etc. Test examples:

    rot13("EBG13 rknzcyr.") == "ROT13 example.";
    rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"
    """

    alphaLower = "abcdefghijklmnopqrstuvwxyz"
    alphaUpper = alphaLower.upper()
    rot13 = []
    for i in message:
        if i.isupper():
            rot13.append(alphaUpper[alphaUpper.index(i) - 13])
        elif i.islower():
            rot13.append(alphaLower[alphaLower.index(i) - 13])
        else:
            rot13.append(i)
    return ''.join(rot13)

print(rot13("EBG13 rknzcyr.")) # ROT13 example.
print(rot13("This is my first ROT13 excercise!")) # Guvf vf zl svefg EBG13 rkprepvfr!