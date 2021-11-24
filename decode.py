def decode(message):
    """
    You have managed to intercept an important message and you are trying to read it.

    You realise that the message has been encoded and can be decoded by switching each letter with a corresponding letter.

    You also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.

    For example: "a" is encoded with "z", "b" with "y", "c" with "x", etc

    E.G

    "r slkv mlylwb wvxlwvh gsrh nvhhztv" == "i hope nobody decodes this message"
    """
    # We store our alphabet here...
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    # Our decoded message goes here...
    decoded = ''
    # For each character in message...
    for char in message:
        # If the character is alphanumeric...
        if char.isalnum():
            # Add the alphabet character in 25 - index of char in the alphabet 
            decoded += alpha[25 - alpha.index(char)]
        elif char == " ":
            # If a space, add the space...
            decoded += char
    # Return the decoded message...
    return decoded

print(decode("r slkv mlylwb wvxlwvh gsrh nvhhztv")) # i hope nobody decodes this message