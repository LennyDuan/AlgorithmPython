def longestPalindrome(self, s: str) -> str:
    res = ''
    s_l = len(s)

    def helper(l, r, s):
        while l >= 0 and r < s_l and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l:r-1]

    for i in range(s_l):
        res = max(helper(i, i, s), helper(i, i + 1, s), res, key=len)

    return res


# s = "babad"
# # s = "cbbd"
s = "ac"

print(longestPalindrome(None, s))
