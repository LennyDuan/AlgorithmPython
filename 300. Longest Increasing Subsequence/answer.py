def lengthOfLIS(self, nums) -> int:
    res = 0
    dp = [1]
    for i in range(1, len(nums)):
        maxval = 0
        for j in range(0, len(nums[0:i])):
            if nums[i] > nums[j]:
                maxval = max(maxval, dp[j])

        dp.append(maxval + 1)
        res = max(res, dp[i])
    return res


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(None, nums))
