def alternate_case(s):
    """
    Write function alternateCase which switch every letter in string 
    from upper to lower and from lower to upper. 
    E.g: Hello World -> hELLO wORLD
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in s])

print(alternate_case("Hello World")) # hELLO wORLD