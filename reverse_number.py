def reverse_number(n):
    """
    Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

    Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

    E.G
     123 ->  321
    -456 -> -654
    1000 ->    1
    """
    # We store a reversed version of the integer as a string here...
    reversed = str(n)[::-1]
    # If the first char of the string representation of the integer is -
    if str(n)[0] == "-":
        # Reversed is now everything bar the minus at the end (it was previously reversed)
        reversed = reversed[0:-1]
        # Return the integer representation of the number * -1 as we know it is a negative number.
        return int(reversed) * -1
    else:
        # Else return the integer representation of the number reversed.
        return int(reversed)

print(reverse_number(123)) # 321
print(reverse_number(-123)) # -321
print(reverse_number(1000)) # 1