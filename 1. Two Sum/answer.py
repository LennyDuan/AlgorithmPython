def twoSum(self, nums, target):
    s_dict = {}
    for index, num in enumerate(nums):
        paired_key = target - num
        if s_dict.get(paired_key) is not None:
            return [s_dict.get(paired_key), index]
        else:
            s_dict[num] = index
            s_dict[paired_key] = index
    print(s_dict)


nums = [2, 7, 11, 15]
target = 9
print(twoSum(None, nums, target))
