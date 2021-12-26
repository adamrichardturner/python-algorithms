import re

def max_sum_between_two_negatives(arr):
    """
    You have a list of integers. The task is to return the maximum sum of the elements located between two negative elements, or if there is no such sum: -1 for Python, JavaScript and COBOL, Nothing for Haskell.

    No negative element should be present in this sum.

    Example:

    [4, -1, 6, -2, 3, 5, -7, 7] -> 8
    """
    indices = ''
    for i, n in enumerate(arr):
        if n > 0:
            indices += str(n)
        else:
            indices += 'x'
    groups = indices.split('x')
    sums = []
    for num in groups:
        if len(num) > 1:
            numSum = 0
            for i in num:
                numSum += int(i)
            sums.append(numSum)
        elif num == '':
            continue
        else:
            sums.append(int(num))
    return max(sums)
            
print(max_sum_between_two_negatives([-1,6,-2,3,5,-7])) #8