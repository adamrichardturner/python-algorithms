def count_nines(n):
    """
    I want to count from 1 to n. How many times will I use a '9'?
    9, 19, 91.. will contribute one '9' each, 99, 199, 919.. will 
    contribute two '9's each...etc
    
    Note: n will always be a positive integer.
    """
    nineSum = 0

    if n < 9:
        return 0
    else:
        for num in range(9, n+1, 1):
            if "9" in str(num):
                nineSum += str(num).count("9")

    return nineSum

print(count_nines(1))
print(count_nines(9))
print(count_nines(100))
print(count_nines(200))
print(count_nines(278))
print(count_nines(279))
print(count_nines(280))
print(count_nines(908))
print(count_nines(909))