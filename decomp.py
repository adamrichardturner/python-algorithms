import math

def decomp(n):
    """
    The aim of the kata is to decompose n! (factorial n) into its prime factors.
    E.G
    n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
    since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.

    n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"

    n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
    """
    def primes(n):
        n += 1
        sieve = [True] * n
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i]:
                sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        return [2] + [i for i in range(3,n,2) if sieve[i]]

    def factorials(x):
        res = []
        for p in primes(n):
            rest = n
            s = 0
            while rest > 0:
                j = rest // p
                s += j
                rest = j
            if s > 1:
                res.append(str(p) + " ^ " + str(s))
            else:
                res.append(str(p))
        return ' * '.join(res)

    return factorials(n)

print(decomp(5)) # 2 ^ 10 * 3 ^ 5 * 5 ^ 2 * 7 * 11
print(decomp(12)) # 2 ^ 10 * 3 ^ 5 * 5 ^ 2 * 7 * 11
#print(decomp(22)) # 2 ^ 19 * 3 ^ 9 * 5 ^ 4 * 7 ^ 3 * 11 ^ 2 * 13 * 17 * 19
#print(decomp(25)) # 2 ^ 22 * 3 ^ 10 * 7 ^ 3 * 11 ^ 2 * 13 * 17 * 19 * 23