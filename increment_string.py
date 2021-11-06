import re

def increment_string(strng):
    """
    Your job is to write a function which increments a string, to create a new string.
    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.
    """
    strLen = len(strng)
    if len(strng) == 0:
        return '1'
    if strng[-1].isalpha():
        return strng + '1'
    else:
    # Regex to match chars and numbers. 
        stringNums = re.match(r'([a-z]+)([0-9]+)', strng, re.I)
        # If stringNums matches letters + numbers
        if stringNums:
            # Put string into groups of words and numbers.
            i = stringNums.groups()
            elementList = []
            # For each element in the group.
            for el in i:
                # If the element is a digit.
                if el.isdigit():
                    # Return strng minus the chars at the end at length of the digits.
                    # concatenated with string representation of element incremented by 1
                    # with zfill function adding leading 0s to the length of original digit element.
                    return strng[:-len(el)] + str(int(el) + 1).zfill(len(el))
                

print(increment_string("foobar002"))