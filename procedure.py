def procedure(i):
    """
    In this exercise, you will create a function that takes an integer, i. With it you must do the following:
    Find all of its multiples up to and including 100,
    Then take the digit sum of each multiple (eg. 45 -> 4 + 5 = 9),
    And finally, get the total sum of each new digit sum.
    Note: If the digit sum of a number is more than 9 (eg. 99 -> 9 + 9 = 18) then you do NOT have to break it down 
    further until it reaches one digit.
    Example (if i is 25):

    Multiples of 25 up to 100 --> [25, 50, 75, 100]

    Digit sum of each multiple --> [7, 5, 12, 1]

    Sum of each new digit sum --> 25
    """
    # We store our sum here...
    sum = 0
    # For each multiple...
    for n in range(i, 101, i):
        # And each digit in that multiple
        for x in str(n):
            # Add the digit to the sum
            sum += int(x)
    # Return the sum
    return sum


print(procedure(25)) # 25
print(procedure(30)) # 18
print(procedure(12)) # 72