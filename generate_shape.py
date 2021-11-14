def generate_shape(n):
    """
    I will give you an integer. Give me back a shape that is as long and wide as the integer. 
    The integer will be a whole number between 1 and 50.

    Example
    n = 3, so I expect a 3x3 square back.
    """
    # We store our final string representations of the square in this list...
    square = []
    # For each item in range 1 --> n+1...
    for i in range(1, n + 1):
        # If i == n we are at the last row of our square, we don't include line break at the end.
        if i == n:
            square.append("+" * n)
        # Else we are not at the end, each row has a line break at the end. 
        else:
            square.append("+" * n + "\n")
    # Return the square list joined as a string...
    return ''.join(square)

print(generate_shape(5))
# +++++
# +++++
# +++++
# +++++
# +++++