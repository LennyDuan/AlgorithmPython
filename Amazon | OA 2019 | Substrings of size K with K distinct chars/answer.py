def size_k(s, k):
    res = []
    len_s = len(s)
    for i in range(len_s):
        sub = s[i:i+k]
        if i + k > len_s:
            break
        if sub not in res and len(set(sub)) is k:
            res.append(sub)
    return res


s = "abcabc"
k = 3

s = "abacab"
k = 3

s = "awaglknagawunagwkwagl"
k = 4

print(size_k(s, k))
