def count_inversions(array):
    """
    Array inversion indicates how far the array is from being sorted.

    Inversions are pairs of elements in array that are out of order.

    Examples
    [1, 2, 3, 4]  =>  0 inversions
    [1, 3, 2, 4]  =>  1 inversion: 2 and 3
    [4, 1, 2, 3]  =>  3 inversions: 4 and 1, 4 and 2, 4 and 3
    [4, 3, 2, 1]  =>  6 inversions: 4 and 3, 4 and 2, 4 and 1, 3 and 2, 3 and 1, 2 and 1
    """
    inversions = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                inversions += 1
    return inversions
    

print(count_inversions([6,5,4,3,3,3,3,2,1])) # Returns 24, should return 30
