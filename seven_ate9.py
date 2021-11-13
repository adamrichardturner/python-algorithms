def seven_ate9(str_):
    """
    Write a function that removes every lone 9 that is inbetween 7s.

    "79712312" --> "7712312"
    "79797"    --> "777"
    """
    # Converting str_ into a list representation...
    chars = list(str_)
    # For each character in chars, enumerate with indices...
    for index, char in enumerate(chars):
        # If char is == 9 and the last char in chars is not 9...
        if char == "9" and chars[-1] != "9":
            # If immediately before and after that 9 char is 7...
            if chars[index - 1] == "7" and chars[index + 1] == "7":
                # Pop char (9) in this instance...
                chars.pop(index)
    # Return a joined string representation of the chars list...
    return ''.join(chars)

print(seven_ate9('165561786121789797')) # 16556178612178977
print(seven_ate9('797')) # 77
print(seven_ate9('7979797')) # 7777
print(seven_ate9('1779')) # 1779