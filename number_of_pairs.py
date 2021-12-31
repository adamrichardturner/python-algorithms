from collections import Counter

def number_of_pairs(gloves):
    """
    Winter is coming, you must prepare your ski holidays. The objective of this 
    kata is to determine the number of pair of gloves you can constitute from the 
    gloves you have in your drawer.

    Given an array describing the color of each glove, return the number of pairs 
    you can constitute, assuming that only gloves of the same color can form pairs.
    """
    # We store our pairs in a dictionary here, using Counter the values contain 
    # how many gloves we have per colour...
    pairs = Counter(gloves)
    # Initialise our counter of pairs here...
    countPairs = 0
    # For pair in pairs (values)...
    for pair in pairs.values():
        # We add to countPairs the pair floor divided by 2, returning the number of pairs.
        countPairs += pair // 2
    return countPairs

print(number_of_pairs(["gray","black","purple","purple","gray","black"])) # 3
print(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"])) # 3