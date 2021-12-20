def double_every_other(lst):
    """
    Write a function that doubles every second integer in a list starting from the left.
    """
    doubled = []
    for index, num in enumerate(lst[1:]):
        if index % 2 == 0:
            doubled.append(num * 2)
        else:
            doubled.append(num)
    doubled.insert(0, lst[0])
    return doubled
print(double_every_other([1,2,3,4])) # -> [1, 4, 3, 8]