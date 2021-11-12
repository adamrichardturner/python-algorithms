from math import sqrt

def is_prime(num):
    """
    Define a function that takes one integer argument and returns logical value 
    true or false depending on if the integer is a prime.

    Requirements

    You can assume you will be given an integer input.
    You can not assume that the integer will be only positive. 
    You may be given negative numbers as well (or 0).
    """
    # This is our prime flag, if it is not 0 we have a composite
    prime = 0
    # Numbers less than including 1 are not prime...
    if num <= 1:
        return False
    else:
        # For each item in range 2 to the sqrt(num) as integer + 1
        for i in range(2, int(sqrt(num)) + 1):
            # If the num is divisible by item...
            if num % i == 0:
                # We have a composite...
                prime = 1
                break
        # Final check, if prime is 0 we have a prime number...
        if prime == 0:
            return True
        else:
        # Otherwise, we don't...
            return False

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(7))
print(is_prime(5099))