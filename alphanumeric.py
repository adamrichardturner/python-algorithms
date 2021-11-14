def alphanumeric(password):
    """
    In this example you have to validate if a user input string is alphanumeric. 
    The given string is not nil/null/NULL/None, so you don't have to check that.

    The string has the following conditions to be alphanumeric:

    At least one character ("" is not valid)
    Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
    No whitespaces / underscore
    """
    # We store our allowed characters in this list for later sanitizing...
    allowed = []
    # For each char in password...
    for char in password:
        # If the char is alphanumeric, append to allowed list...
        if char.isalpha() or char.isnumeric():
            allowed.append(char)
    # Sanitizing allowed. If the length of allowed is same as password, it is valid.
    # Also if the len of password is 0 (empty), we return False.
    if len(allowed) != len(password) or len(password) == 0:
        return False
    else:
        return True

print(alphanumeric("")) # False
print(alphanumeric("hello world_")) # False
print(alphanumeric("PassW0rd")) # True