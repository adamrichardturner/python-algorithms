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
    powers = []
    # Round n and cast it as an int...
    z = int(round(n))
    # If n <= 0 or == 1 return 4...
    if z <= 0 or z == 1:
        return 4
     # In any other case, for m in the range (start 2, end z inclusive) iterate each number up to and including z.
    for m in range(2, z + 1, 1):
    # Within each iteration above, complete iteration of the same range..
        for k in range(2, z + 1, 1):
            # If z is not in powers...
            if z not in powers:
                # Append m^k tp powers
                powers.append(m ** k)
                if len(powers) >= 100:
                    break
    # Return the minimum value in powers closest to our input number
    return min(powers, key=lambda x:abs(x-z))

print(closest_power(0)) # 4
print(closest_power(11)) # 9
print(closest_power(30)) # 32
print(closest_power(34)) # 32
print(closest_power(56.5)) # 49
#print(closest_power(123321456654)) # CRASH!