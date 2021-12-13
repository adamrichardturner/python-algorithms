def binary_array_to_number(arr):
    """
    Given an array of ones and zeroes, convert the equivalent binary value to an integer.
    Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
    Testing: [0, 0, 1, 0] ==> 2
    Testing: [0, 1, 1, 0] ==> 6
    Testing: [1, 1, 1, 1] ==> 15
    Testing: [1, 0, 1, 1] ==> 11
    """
    # Store our decimal value to return at the end here...
    decimal = 0
    # Enumerate values in reverse representation of arr
    for n, p in enumerate(arr[::-1]):
        # Add to decimal p(binary value) multiplied by 2 to the power of n
        decimal += p * 2 ** n
    # Return decimal value
    return decimal

print(binary_array_to_number([0, 0, 1, 0])) # 2
print(binary_array_to_number([0, 1, 1, 0])) # 6
print(binary_array_to_number([1, 1, 1, 1])) # 15
print(binary_array_to_number([1, 0, 1, 1])) # 11