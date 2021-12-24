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
        return pairs[0]
    else:
        nums = ints.copy()
        indices = []
        while pairs:
            i = pairs.pop()
            for n in i:
                if n in nums:
                    indices.append(nums.index(n))
                    nums[nums.index(n)] = 'x'
        def chunks(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i:i + n]
        index_pairs = list(chunks(indices, 2))
        absolutes = []
        print("index pairs: ", index_pairs)
        if not index_pairs:
            return None
        for pair in index_pairs:
            absolutes.append(pair[1] - pair[0])
        a = index_pairs[absolutes.index(min(absolutes))][0]
        b = index_pairs[absolutes.index(min(absolutes))][1]
        return [ints[a], ints[b]]

print(sum_pairs([1, 2, 3, 4, 1, 0], 2))