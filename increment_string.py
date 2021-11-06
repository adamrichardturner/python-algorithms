import re

def increment_string(strng):
    """
    Your job is to write a function which increments a string, to create a new string.
    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.
    """
    # If the string is empty, return 1.
    if len(strng) == 0:
        return '1'
    # If string is a single digit number, return that digit incremented.
    elif len(strng) == 1 and strng.isdigit():
        return str(int(strng) + 1)
    # If the string is a longer number on its own, increment it with any leading 0s
    elif len(strng) > 1 and strng.isdigit():
        return str(int(strng) + 1).zfill(len(strng))
    # If the final char of the string is a letter, return the strng + 1
    elif strng[-1].isalpha():
        return strng + '1'
    else:
    # Regex to match numbers. 
        stringNums = re.findall('[0-9]+', strng)
        # Counter to determine the position of the final number in the string
        total = 0
        # Iterate stringNums, increment counter (total) 
        for i in stringNums:
            total += 1
        # Store the location of the number at end of string in x.
        x = stringNums[total - 1]
        # Return strng minus final numbers + string representation of the number incremented
        # including any leading 0s.
        return strng[:-len(str(x))] + str(int(x) + 1).zfill(len(x))
                
print(increment_string("asdwd54fegwgerg006")) # asdwd54fegwgerg007
print(increment_string("foo")) # foo1
print(increment_string("foobar001")) # foobar002
print(increment_string("foobar1")) # foobar2
print(increment_string("foobar00")) # foobar01
print(increment_string("foobar99")) # foobar100
print(increment_string("foobar099")) # foobar100
print(increment_string("")) # 1