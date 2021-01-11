def canJump(self, nums) -> bool:
    if not nums:
        return False
    i = 0
    max_index = nums[i]

    while i < len(nums) and i <= max_index:
        new_index = nums[i] + i
        max_index = max(max_index, new_index)
        i += 1

    return i >= len(nums)


nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
print(canJump(None, nums))
