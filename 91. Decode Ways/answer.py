def numDecodings(self, s: str) -> int:
    dp = [0] * (len(s) + 1)
    valid_26_num = [str(i) for i in range(1, 27)]
    valid_9_num = [str(i) for i in range(1, 10)]

    dp[0] = 1
    dp[1] = 1 if s[0] in valid_9_num else 0
    for i in range(2, len(s) + 1):
        if s[i-1:i] in valid_9_num:
            dp[i] += dp[i - 1]
        if s[i - 2:i] in valid_26_num:
            dp[i] += dp[i - 2]
    print(dp)
    return dp[-1]


s = "226"
# s = '0'
# s = "2101"
print(numDecodings(None, s))
