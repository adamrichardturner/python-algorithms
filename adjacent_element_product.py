def adjacent_element_product(array):
    """
    Given an array of integers , Find the maximum product 
    obtained from multiplying 2 adjacent numbers in the array.

    E.G

    adjacentElementsProduct([1, 2, 3]); ==> returns 6
    adjacentElementsProduct([9, 5, 10, 2, 24, -1, -48]); ==> returns 50
    adjacentElementsProduct([-23, 4, -5, 99, -27, 329, -2, 7, -921])  ==>  returns -14
    """
    # Return the maximum value of a list iterated over to produce the multiplication 
    # of adjacent values.
    return max(list(i * j for i, j in zip(array, array[1:])))

print(adjacent_element_product([1, 2, 3])) # 6
print(adjacent_element_product([9, 5, 10, 2, 24, -1, -48])) # 50
print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921])) # -14