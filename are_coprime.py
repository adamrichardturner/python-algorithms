def are_coprime(n,m):
    """
    Write a program to determine if the two given numbers are coprime. A pair of numbers are coprime if their greatest shared factor is 1.

    The inputs will always be two positive integers between 2 and 99.

    Examples
    20 and 27:

    Factors of 20: 1, 2, 4, 5, 10, 20
    Factors of 27: 1, 3, 9, 27
    Greatest shared factor: 1
    Result: 20 and 27 are coprime
    """
    # Factors function which returns a list of all the factors of given input.
    def factors(o):
        factor_list = []
        for num in range(1, o + 1):
            if o % num == 0:
                factor_list.append(num)
        return factor_list
    # Our test flag here, if fact is 1 we have a coprime, else it is not.
    fact = 0
    # For each number in factors of n...
    for x in factors(n):
        # If that number is in factors of m..
        if x in factors(m):
            # Add to fact
            fact += x
    # If fact is 1 we have a coprime...
    if fact == 1:
        return True
    # Else, we don't.
    else:
        return False

print(are_coprime(20, 27)) # True
print(are_coprime(12, 39)) # False