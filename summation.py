def summation(num):
    """Write a program that finds the summation of every number 
    from 1 to num. The number will always be a positive integer
    greater than 0.
    E.G
    summation(2) -> 3
    1 + 2
    summation(8) -> 36
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
    """
    # We keep our sum total here.
    sum = 0
    # We reverse the range of num + 1 to find all the digits descending
    # from num.
    nums = reversed(range(num + 1))
    # Iterate through each of the digits in nums generated above, adding
    # them to the total.
    for num in nums:
        sum += num
    return sum

print(summation(8))