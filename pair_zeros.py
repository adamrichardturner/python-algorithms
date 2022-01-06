def pair_zeros(arr):
    """
    For a given list of digits 0 to 9, return a list with the same digits 
    in the same order, but with all 0s paired. Pairing two 0s generates one
    0 at the location of the first one.

    E.G

    input: [0, 1, 7, 0, 2, 2, 0, 0, 1, 0]
    paired: ^--------^        ^--^
        -> [0, 1, 7,    2, 2, 0,    1, 0]
                        kept: ^        ^
    """
    # Indices of all the zeros stored here...
    indices = []
    # For each index and number in the arr...
    for i, n in enumerate(arr):
        # If the number is 0, append its index to indices...
        if n == 0:
            indices.append(i)
    # Store our indices to take away from arr here...
    take_away = []
    # For each index and number in the indices...
    for i, n in enumerate(indices):
        # If the index is odd, append it to the take_away list
        if i % 2 != 0:
            take_away.append(n)
    # Return the numbers in arr if they are not at the indices held in take_away
    return [num for index, num in enumerate(arr) if index not in take_away]

print(pair_zeros([0, 1, 7, 0, 2, 2, 0, 0, 1, 0])) # [0, 1, 7, 2, 2, 0, 1, 0]