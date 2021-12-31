def every_other_letter(word):
    """
    We are going to create a function that extract every other letter 
    from a string and returns the resulting string. There are a few different
    ways you can solve this problem.
    """
    return ''.join([letter for index, letter in enumerate(word) if index % 2 == 0])
# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd