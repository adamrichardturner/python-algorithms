def digital_root(n):
    """
    Digital root is the recursive sum of all the digits in a number.

    Given n, take the sum of the digits of n. If that value has more than one digit, 
    continue reducing in this way until a single-digit number is produced. The input 
    will be a non-negative integer.

    Examples
    16  -->  1 + 6 = 7
    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
    132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
    493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
    """
    # We will store our string representation of n here...
    total = list(str(n))
    # We will store our final sum here...
    sum = 0
    # For each number character in total (list) 
    for num in total:
        # Add to sum this char as an integer...
        sum += int(num)
    # If the length of number is > 1
    if len(str(sum)) > 1:
        # Recursively calculate the sum until it is 1...
        return digital_root(sum)
    else:
        # Else return the sum if it is a single digit number...
        return sum

print(digital_root(16)) # 7
print(digital_root(942)) # 6
print(digital_root(132189)) # 6
print(digital_root(493193)) # 2