def canJump(self, nums) -> bool:
    if len(nums) < 2:
        return True
    dp = [0] * len(nums)
    dp[0] = nums[0]
    print(dp)
    for i in range(1, len(nums)):
        if dp[i - 1] < i:
            print(dp)
            print(i)
            return False
        dp[i] = max(dp[i - 1], i + nums[i])
    return dp[-1] >= len(nums) - 1


nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
nums2 = [3, 2, 1, 1, 0]

print(canJump(None, nums1))
print(canJump(None, nums2))
