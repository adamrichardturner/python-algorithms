def reverse_string(word):
    """
    Reverse a string.
    """
    return ''.join([word[i] for i in range(len(word) - 1, -1, -1)])

print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print