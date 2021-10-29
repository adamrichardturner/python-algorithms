def iq_test(numbers):
    """
    Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one 
    of the given numbers differs from the others. Bob observed that one number usually differs from 
    the others in evenness. Help Bob — to check his answers, he needs a program that among the given 
    numbers finds one that is different in evenness, and return a position of this number.
    
    Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements 
    start from 1 (not 0)
    """
    # First we split the string into a list of number chars split with a space
    nums = numbers.split(' ')
    # We will keep our list of integers here
    intList = []
    # Initial counters for evenness
    even = 0
    odd = 0
    for i in nums:
        # If the integer is even append to the intList and increment even counter
        if int(i) % 2 == 0:
            intList.append(int(i))
            even += 1
        else:
        # Else if the integer is odd, append to the intList and increment odd counter
            intList.append(int(i))
            odd += 1
    # The final check - if even greater than odd, return index of the odd number.
    if even > odd:
        for i in intList:
            if i % 2 != 0:
                # Because we are counting from 1 and not 0 indexed, we add 1 to the index
                return intList.index(i) + 1
    else:
    # If odd greater than even, return index of the even number. 
        for i in intList:
            if i % 2 == 0:
                # Because we are counting from 1 and not 0 indexed, we add 1 to the index
                return intList.index(i) + 1