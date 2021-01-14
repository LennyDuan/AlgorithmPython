def maxSubArray(self, nums) -> int:
    dp = nums
    for i in range(len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
    print(dp)
    return max(dp)
            # for i in range(1, len(nums)):
    #     if nums[i - 1] > 0:
    #         nums[i] += nums[i-1]
    #
    # return max(nums)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(None, nums))
