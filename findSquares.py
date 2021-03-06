def findSquares(x,y):
    """
    A rectangle can be split up into a grid of 1x1 squares, the amount of 
    which being equal to the product of the two dimensions of the rectangle. 
    Depending on the size of the rectangle, that grid of 1x1 squares can 
    also be split up into larger squares, for example a 3x2 rectangle has 
    a total of 8 squares, as there are 6 distinct 1x1 squares, and two possible 
    2x2 squares. A 4x3 rectangle contains 20 squares.

    Your task is to write a function `findSquares` that returns the total number 
    of squares for any given rectangle, the dimensions of which being given as 
    two integers with the first always being equal to or greater than the second.
    """
    # Algorithm works as follows: Total number of squares= x*y + (x−1)*(y−1)+(x−2)*(y−2)+…
    totalSquares = x * y
    # Iterate through each number stopping inclusive of the first side length.
    for i in range(1, x + 1):
        # If = to the smaller side length, break the loop.
        if i == y:
            break
        else:
        # Else, totalSquares is x - i * y - i
            totalSquares += (x - i) * (y - i)
    return totalSquares

print(findSquares(3, 2)) # 8
print(findSquares(4, 3)) # 20
print(findSquares(11, 4)) # 100
