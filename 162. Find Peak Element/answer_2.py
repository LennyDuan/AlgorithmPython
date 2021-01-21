def findPeakElement(self, nums) -> int:
    for index, num in enumerate(nums[:-1]):
        if num > nums[index + 1]:
            return index
    return len(nums) - 1


nums = [1, 2, 3, 1]
print(findPeakElement(None, nums))
