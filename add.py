import itertools

def add(num1, num2):
    """
    For this kata you will have to forget how to add two numbers.

    It can be best explained using the following meme:

    In simple terms, our method does not like the principle of carrying over numbers 
    and just writes down every number it calculates :-) You may assume both integers are 
    positive integers.
    """
    # in to_add we zip string representations of num1, num2 in reverse, padding the smaller
    # string with 0.. This gives us the pairs of numbers to add in tuples...
    to_add = list(itertools.zip_longest(str(num1)[::-1], str(num2)[::-1], fillvalue='0'))
    # in to_sum we iterate each tuple from above, summing the paired values...
    to_sum = [sum(list(map(int, x))) for x in to_add[::-1]]
    # Here we return the integer representation of sums concatenated together...
    return int(''.join([str(x) for x in to_sum]))

print(add(16, 18)) # 214
print(add(26, 39)) # 515
print(add(122, 81)) # 1103