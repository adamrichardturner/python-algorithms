def sum_fibs(n):
    """
    Create a function that takes an argument n and sums even Fibonacci numbers 
    up to n's index in the Fibonacci sequence.
    """
    def fibs(n):
        # Fibonacci is 0 with n=0, and 1 with n=1
        if n == 0: return 0
        elif n == 1: return 1
        else:
            # We store our two items in the sequence to add in x...
            x = [0, 1]
            # For each num in range(n less 1)...
            for i in range(n - 1):
                x.append(x[-1] + x[-2])
        return x

    def sumEvenFibs():
        x = fibs(n)
        sum = 0
        for i in x:
            if i % 2 == 0:
                sum += i
        return sum
    
    return sumEvenFibs()

print(sum_fibs(9))