def sortColors(self, nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums_two = []
    print(nums)
    import bisect
    for num in nums:
        bisect.insort_left(nums_two, num)

    print(nums_two)
    nums[:] = nums_two[:]
    return nums


nums = [2, 0, 2, 1, 1, 0]
sortColors(None, nums)
