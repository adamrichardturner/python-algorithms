import math

def closest_power(n):
    """
    Perfect powers are numbers that can be written m^k, where m and k are both integers greater than 1.
    Your task is to write a function that returns the perfect power nearest any number.

    Notes: When the input itself is a perfect power, return this number. Since 4 is the smallest perfect 
    power, for inputs < 4 (including 0, 1, and negatives) return 4. The input can be either a floating-point 
    number or an integer. If there are two perfect powers equidistant from the input, return the smaller one

    E.G 

    0  -->   4
    11  -->   9    #  9 = 3^2
    34  -->  32    # 32 = 2^5 and 36 = 6^2 --> same distance, pick the smaller
    """
    # Store our list of powers here...
    perfect = []
    # If n <= 0 or == 1 return 4...
    if n <= 0 or n == 1:
        return 4
    # In any other case, for m in the range (start 2, end m inclusive) iterate each number up to and including m.
    for m in range(2, math.ceil(n), 1):
    # Within each iteration above, complete iteration of the same range..
        for k in range(2, math.ceil(n), 1):
        # Append to perfect m^k. This will check all combinations of powers upto and inclusive of the range m.
            perfect.append(m ** k)
    # Return the minimum possible perfect power from the list. I.E the perfect power closest to our input (n).
    print(perfect)
    return min(perfect, key=lambda x:abs(x-round(n)))
    

print(closest_power(56.5))
