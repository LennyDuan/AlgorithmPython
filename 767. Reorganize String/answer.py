# TRUE or False
# from collections import defaultdict
#
# c_dict = defaultdict(int)
# for c in S:
#     c_dict[c] += 1
#
# max_c = max(c_dict, key=c_dict.get)
# max_n = c_dict[max_c]
# remain_n = len(S) - max_n
# return max_n - remain_n <= 1


def reorganizeString(self, S: str) -> str:
    a = sorted(sorted(S), key=S.count)
    h = len(a) // 2

    a[1::2], a[::2] = a[:h], a[h:]

    return ''.join(a) * (a[-1:] != a[-2:-1])


S = "aabacda"
print(reorganizeString(None, S))
