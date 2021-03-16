def subarraySum(self, nums: List[int], k: int) -> int:
    res = 0

    for i, num in enumerate(nums):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == k:
                res += 1

    return res


nums = [1, 1, 1]
k = 2
print(subarraySum(None, nums, k))
