# Given an array of integers, find the one that appears
# an odd number of times. There will always be only one
# integer that appears an odd number of times.

from collections import Counter

def find_it(seq):
    count = Counter(seq)
    for x in count:
        if count[x] % 2 != 0:
            return x

print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))