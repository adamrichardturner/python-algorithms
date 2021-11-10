def count_bits(n):
    """
    Write a function that takes an integer as input, and returns the number of bits that are 
    equal to one in the binary representation of that number. You can guarantee that input 
    is non-negative.

    Example: The binary representation of 1234 is 10011010010, so the function should return 
    5 in this case
    """
    # Store string representation of binary number (in reverse) here.
    binary = ""
    # Algorithm to convert decimal to binary.
    # While n > 0...
    while n > 0:
        # If n has a remainder of 1 after dividing by 2..
        if n % 2 == 1:
            # Floor divide n by 2.
            n //= 2
            # Add the remainder as "1" to binary.
            binary += "1"
        else:
            # If no remainder, add "0" to binary after floor dividing by 2.
            n //= 2
            binary += "0"
    # Return the count of bits in the binary representation. The binary string is in
    # Reverse, but we only need to know the number of bits for this exercise.
    return binary.count('1')

print(count_bits(1234)) # 5
print(count_bits(0)) # 0
print(count_bits(234)) # 5
print(count_bits(256)) # 1