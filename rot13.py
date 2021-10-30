def rot13(message):
    """
    ROT13 is a simple letter substitution cipher that replaces a letter with the letter 
    13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

    Create a function that takes a string and returns the string ciphered with Rot13. If 
    there are numbers or special characters included in the string, they should be returned 
    as they are. Only letters from the latin/english alphabet should be shifted, like in the 
    original Rot13 "implementation".

    Please note that using encode is considered cheating.
    """
    # We store our alphabet chars in these two strings as lower and uppercase.
    alphaLower = "abcdefghijklmnopqrstuvwxyz"
    alphaUpper = alphaLower.upper()
    # We will append each char to this list and return it is a string.
    rot13 = []
    for char in message:
        # If the char is upper or lower, find it's matching index in the upper or lower alpha string
        if char.isupper():
            index = alphaUpper.index(char)
            # Append the -13 index of the location of the char in the correct string.
            rot13.append(alphaUpper[index - 13])
        elif char.islower():
            # Same process as upper case but for lower.
            index = alphaLower.index(char)
            rot13.append(alphaLower[index - 13])
        else:
            # If neither an uppercase or lowercase letter, append the char.
            rot13.append(char)
    return ''.join(rot13)

print(rot13("Hello World!")) # Uryyb Jbeyq!
print(rot13("Adam Turner is King!")) # Nqnz Gheare vf Xvat!
print(rot13("Attack at Dawn!")) # Nggnpx ng Qnja!