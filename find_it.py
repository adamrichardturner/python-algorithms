# Given an array of integers, find the one that appears
# an odd number of times. There will always be only one
# integer that appears an odd number of times.

from collections import Counter

# Import counter, a tool which provides the number of times
# an item appears in an array.

def find_it(seq):
    count = Counter(seq)
    # For each iteration of count, if the number appears an
    # odd number of items, return that number.
    for x in count:
        if count[x] % 2 != 0:
            return x

print(find_it([1, 1, 2, 2, 3, 3, 4, 4, 7, 7, 7]))