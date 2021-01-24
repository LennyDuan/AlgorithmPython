def sortColors(self, nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums_dict = {
        0: 0,
        1: 0,
        2: 0
    }
    for num in nums:
        nums_dict[num] += 1
    print(nums_dict)
    nums = []
    for k, v in nums_dict.items():
        for i in range(v):
            nums.append(k)
    print(nums)
    nums[:] = nums[:]

    return nums


nums = [2, 0, 2, 1, 1, 0]
sortColors(None, nums)
