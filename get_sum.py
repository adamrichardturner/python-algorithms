# Given two integers a and b, which can be positive or negative,
# find the sum of all the integers between and including them and
# return it. If the two numbers are equal return a or b.

def get_sum(a,b):
    # Initialise our sum variable
    total = 0
    # If a and b are the same, return one of them
    if a == b:
        return a
    else:
        # Iterate through the range of a, b starting from
        # lowest of the two.
        # Add the each figure to the total and return total.
        for x in range(min(a, b), max(a, b) + 1):
            total += x
        return total