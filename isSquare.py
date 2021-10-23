import math

# Check if a number is a square number or not. Return true if the number is square
# else return false.

def is_square(n):
    # Square numbers cannot be negative, first we check if n is less than 0
    if n < 0:
        return False
    # If n is above 0 we check the square root is an integer, then we know
    # we have a square number.
    elif n > 0:
        if math.sqrt(n).is_integer() == True:
            return True
        else:
            return False
    # 0 is a square number
    elif n == 0:
        return True
    else:
        return False