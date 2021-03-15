def countBinarySubstrings(self, s: str) -> int:
    res = 0
    group = [1]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            group.append(1)
        else:
            group[-1] += 1

    print(group)

    for i in range(1, len(group)):
        res += min(group[i], group[i-1])

    return res


s = "00110011"
print(countBinarySubstrings(None, s))
