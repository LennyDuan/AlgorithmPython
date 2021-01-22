def maxProduct(self, nums) -> int:
    res = nums[0]
    dp = [None] * len(nums)
    dp[0] = (nums[0], nums[0])
    for i in range(1, len(nums)):
        pre_dp = dp[i-1]
        pre_max, pre_min = pre_dp[0], pre_dp[1]

        i_max = max(max(nums[i], nums[i] * pre_max), pre_min * nums[i])
        i_min = min(min(nums[i], nums[i] * pre_min), pre_max * nums[i])
        dp[i] = (i_max, i_min)

        res = max(i_max, res)

    print(dp)
    return res


nums = [2, 3, -2, 4]
print(maxProduct(None, nums))
