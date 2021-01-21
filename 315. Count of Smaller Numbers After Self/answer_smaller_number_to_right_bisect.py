import bisect


def countSmaller(self, nums):
    res = []
    sorted_nums = []
    for num in nums[::-1]:
        position = bisect.bisect_left(sorted_nums, num)
        res.append(position)
        bisect.insort_left(sorted_nums, num)

    return res[::-1]


nums = [5, 2, 6, 1]
print(countSmaller(None, nums))
