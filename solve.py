import math

def solve(a,b):
    """
    In this Kata, you will be given two numbers, a and b, and your task is to determine if the first number a is divisible 
    by all the prime factors of the second number b. For example: solve(15,12) = False because 15 is not divisible by all 
    the prime factors of 12 (which include 2).

    See test cases for more examples.
    """
    def prime_factors(num):
        primes = []
        for i in range(2, num + 1):
            if num % i == 0:
                count = 1
                for j in range(2, (i//2 + 1)):
                    if(i % j == 0):
                        count = 0
                        break
                if count == 1:
                    primes.append(i)
        return primes

    def divide_primes():
        primes = prime_factors(b)
        count = 0
        for num in primes:
            if a % num == 0:
                count += 1
        if count != len(primes):
            return False
        else:
            return True
    
    return divide_primes()

print(solve(15, 12))
print(solve(2,256))
print(solve(2,253))
print(solve(9,243))
print(solve(1000013,7187761))
print(solve(1000013,7187762))