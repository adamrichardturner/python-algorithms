# Given the triangle of consecutive odd numbers
#   1
#  3 5
# 7 9 11
# ...
# Calculate the sum of the numbers in the nth row of this triangle
# starting at index 1. e.g (1), (3 + 5), (7 + 9 + 11)

def row_sum_odd_numbers(n):
    # n is the number of the row, n^3 is the total of the odd
    # numbers in that row. 
    return n ** 3