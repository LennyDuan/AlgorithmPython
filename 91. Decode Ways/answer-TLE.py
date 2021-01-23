def numDecodings(self, s: str) -> int:
    res = [0]
    valid_num = [str(i) for i in range(1, 27)]

    def is_valid(s):
        return s in valid_num

    def dfs(s, start, c_path):
        if start > len(s):
            print(c_path)
            res[0] += 1
            return
        for end in range(start, len(s) + 1):
            if is_valid(s[start:end + 1]):
                dfs(s, end + 1, c_path + [s[start:end + 1]])
            else:
                break

    dfs(s, 0, [])
    return res[0]


s = "226"
s = '0'
s = "2101"
print(numDecodings(None, s))
