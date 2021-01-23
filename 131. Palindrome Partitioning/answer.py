def partition(self, s: str):
    def isPalinrome(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

    def dfs(start, s, cur_res=[], res=[]):
        if start >= len(s):
            res.append(cur_res)
            print('res', res)
        for end in range(start, len(s)):
            if isPalinrome(s, start, end):
                dfs(end + 1, s, cur_res + [s[start:end + 1]], res)

    paths = list()
    dfs(0, s, [], paths)
    return paths


s = "aab"
print(partition(None, s))
