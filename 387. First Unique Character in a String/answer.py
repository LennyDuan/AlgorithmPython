import string
from collections import defaultdict


def firstUniqChar(s) -> int:
    w_dict = defaultdict(int)
    uniq = False
    for w in s:
        w_dict[w] += 1

    for k, v in w_dict.items():
        if v is 1:
            uniq = k
            break

    return s.index(uniq) if uniq else -1


def firstUniqChar2(s) -> int:
    letters = string.ascii_lowercase
    count_list = [s.index(l) for l in letters if s.count(l) == 1]
    return min(count_list) if len(count_list) > 0 else -1


def firstUniqChar3(s):
    for i, w in enumerate(s):
        if s.count(w) == 1:
            return i

    return -1


s = "leetcode"
s2 = "loveleetcode"

print(firstUniqChar3(s2))

print(string.ascii_lowercase)

