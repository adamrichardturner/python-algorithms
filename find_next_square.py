# Complete the findNextSquare method that finds the next integral
# perfect square after the one passed as a parameter. Recall that
# an integral perfect square is an integer n such that sqrt(n) is 
# also an integer.
# If the parameter is itself not a perfect square, then -1 should
# be returned. You may assume the parameter is non-negative. 

import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    # if the sqrt of sq is an integer we are dealing with a 
    # square number. 
    if math.sqrt(sq).is_integer() == True:
        # We have a square number, we find the sqrt, increment 
        # by 1 and square the result to find the next consecutive
        # perfect square.
        x = math.sqrt(sq)
        return int((x + 1) ** 2)
    else:
        # Else if sq is not a perfect square (its sqrt is a float)
        # we return -1
        return -1