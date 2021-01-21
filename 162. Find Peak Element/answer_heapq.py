def findPeakElement(self, nums) -> int:
    res = nums.copy()
    import heapq
    heapq._heapify_max(nums)
    top = heapq.heappop(nums)

    return res.index(top)

nums = [1, 2, 3, 1]
print(findPeakElement(None, nums))
