def findPeakElement(self, nums) -> int:
    res = 0
    if len(nums) < 2:
        return 0

    # Compare first 2 nums
    if len(nums) == 2:
        return 1 if nums[1] > nums[0] else 0

    # Compare last 2 nums
    if nums[-1] > nums[-2]:
        return len(nums) - 1

    for index, num in enumerate(nums):
        before = index - 1
        after = index + 1
        left = right = False
        if before >= 0 and nums[left] < num:
            left = True
        if after < len(nums) and nums[after] < num:
            right = True

        if left and right:
            return index

    return res


nums = [1, 2, 3, 1]
print(findPeakElement(None, nums))
