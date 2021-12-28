def incrementer(nums):
    """
    Given an input of an array of digits, return the array with each digit incremented 
    by its position in the array: the first digit will be incremented by 1, the second 
    digit by 2, etc. Make sure to start counting your positions from 1 (and not 0).

    Your result can only contain single digit numbers, so if adding a digit with it's 
    position gives you a multiple-digit number, only the last digit of the number 
    should be returned.

    Notes:
    - return an empty array if your array is empty
    - arrays will only contain numbers so don't worry about checking that

    E.G
    [1, 2, 3]  -->  [2, 4, 6]   #  [1+1, 2+2, 3+3]
    """
    # Sums holds our nums values incremented by their indices (1 is the first index...)
    sums = [num + i for i, num in enumerate(nums, start=1)]
    # We return the num from sums if len(str(num)) is 1 else we simply return the integer
    # representation of the last digit in num if it is greater than 1 digit long...
    return [num if len(str(num)) == 1 else int(str(num)[-1]) for num in sums]

print(incrementer([1, 2, 3])) # [2, 4, 6]
print(incrementer([4, 6, 7, 1, 3])) # [5, 8, 0, 5, 8]
print(incrementer([3, 6, 9, 8, 9])) # [4, 8, 2, 2, 4]