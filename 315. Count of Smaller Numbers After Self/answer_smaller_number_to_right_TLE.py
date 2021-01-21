def countSmaller(self, nums):
    res = []
    for index, num in enumerate(nums):
        smaller = 0
        for after_num in nums[index:]:
            if after_num < num:
                smaller += 1
        res.append(smaller)

    return res


nums = [5, 2, 6, 1]
print(countSmaller(None, nums))
