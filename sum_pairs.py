def sum_pairs(ints, s):
    """
    Given a list of integers and a single sum value, return the 
    first two values (parse from the left please) in order of appearance
    that add up to form the sum.
    E.G
    sum_pairs([10, 5, 2, 3, 7, 5],         10)
    #              ^-----------^   5 + 5 = 10, indices: 1, 5
    #                    ^--^      3 + 7 = 10, indices: 3, 4 *
    #  * entire pair is earlier, and therefore is the correct answer
    == [3, 7]
    """
    def get_pairs(ints, s):
        nums = ints.copy()
        res = []
        while nums:
            num = nums.pop()
            diff = s - num
            if diff in nums:
                res.append([diff, num])
        return res
    pairs = get_pairs(ints, s)
    if len(pairs) == 1:
        return pairs
    else:
        nums = ints.copy()
        indices = []
        while pairs:
            i = pairs.pop()
            x = 0
            for n in i:
                if n in nums:
                    indices.append(nums.index(n))
                    nums[nums.index(n)] = 0
            
        print("Indices", indices)
print(sum_pairs([10, 5, 2, 3, 7, 5],         10))
print(sum_pairs([11, 3, 7, 5],         10))