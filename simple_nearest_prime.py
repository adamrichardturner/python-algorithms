import math

def solve(n):
    print(n)
    """
    In this Kata, you will be given a number and your task will be to return the nearest prime number.

    solve(4) = 3. The nearest primes are 3 and 5. If difference is equal, pick the lower one. 
    solve(125) = 127
    We'll be testing for numbers up to 1E10. 500 tests.
    """
    primes = []
    for num in range(n - 100, n + 101):
        if num > 1:
            for i in range(2, int(math.sqrt(num))):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return min(primes, key=lambda x:abs(x-n))

print(solve(125))