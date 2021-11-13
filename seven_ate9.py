def seven_ate9(str_):
    """
    Write a function that removes every lone 9 that is inbetween 7s.

    "79712312" --> "7712312"
    "79797"    --> "777"
    """
    # We will store our index of 9 when located here...
    i = 0
    # Converting str_ into a list representation...
    chars = list(str_)
    # For each character in chars...
    for char in chars:
        # If the char is 9...
        if char == "9":
            # Store the index of that 9 in i...
            i = chars.index(char)
            # If the number is 7 immediately before and after that instance 
            # of 9, remove the 9...
            if chars[i - 1] and chars[i + 1] == "7":
                chars.remove(char)
    # Return a joined string representation of the chars list...
    return ''.join(chars)

print(seven_ate9('165561786121789797')) # 1655617861217877
print(seven_ate9('797')) # 77
print(seven_ate9('7979797')) # 7777

    