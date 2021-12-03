def compute_sum(n):
    """
    Find the sum of the digits of all the numbers from 1 to N (both ends included).
    E.G

    # N = 12
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
    """
    # We store our total here...
    total = 0
    # For each number in range from 1 up to and inluding n...
    for num in range(1, n + 1):
        # If the number is greater than 1 digit in length...
        if len(str(num)) > 1:
            # Add to total the sum of each digit in that number...
            total += sum(int(digit) for digit in str(num))
        else:
            # Else just add the singular digit to the total...
            total += num
    # Return total...
    return total
    
print(compute_sum(10)) # 46
print(compute_sum(12)) # 51
