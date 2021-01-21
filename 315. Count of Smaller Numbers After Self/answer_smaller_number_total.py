def countSmaller(self, nums):
    from collections import OrderedDict
    res = []
    nums_dict = OrderedDict({num:0 for num in nums})
    print(nums_dict)
    sorted_nums = sorted(nums)
    print(sorted_nums)
    for index, num in enumerate(sorted_nums):
        nums_dict[num] = index
    print(nums_dict)
    res = list(nums_dict.values())
    return res


nums = [5, 2, 6, 1]
print(countSmaller(None, nums))
