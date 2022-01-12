def sum_triangular_numbers(n):
    """
    Your task is to return the sum of Triangular Numbers up-to-and-including 
    the nth Triangular Number.

    Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.) 
    obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc."
    [01]
    02 [03]
    04 05 [06]
    07 08 09 [10]
    11 12 13 14 [15]
    16 17 18 19 20 [21]
    """
    if n < 0:
        return 0
    else:
        tri = []
        for num in range(1, n + 1):
            tri.append(num * (num + 1) / 2)
        return int(sum(tri))

print(sum_triangular_numbers(4))