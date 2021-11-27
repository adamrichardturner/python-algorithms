def single_digit(n):
    """
    The goal of this Kata is to reduce the passed integer to a single digit 
    (if not already) by converting the number to binary, taking the sum of 
    the binary digits, and if that sum is not a single digit then repeat the 
    process.

    If the passed integer is already a single digit there is no need to reduce
    n will be an integer such that 0 < n < 10^20
    E.G
    111010110111100110100010101 --> (sum of binary digits) 16
    16 --> (binary) 10000
    10000 --> (sum of binary digits) 1
    """
    # Function that converts decimal to binary
    def decimal_to_binary(n):
        binary = ""
        while n > 0:
            if n % 2 == 1:
                n //= 2
                binary += '1'
            else:
                n //= 2
                binary += '0'
        return binary[::-1]
    # Function that sums the binary digits in a string
    def sum_binary_string(n):
        sum = 0
        for char in n:
            sum += int(char)
        return sum
    # If the length of n is 1...
    if len(str(n)) == 1:
        # We return n...
        return n
    else:
    # Else we recursively run the parent function until n is a single
    # digit, where we then return n...
        return single_digit(sum_binary_string(decimal_to_binary(n)))

print(single_digit(999)) # 8
print(single_digit(123456789)) # 1
print(single_digit(123456789)) # 1