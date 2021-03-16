def removeDuplicates(self, s: str, t_k: int) -> str:
    dups = []
    for c in set(s):
        dups.append(k * c)
    print(dups)

    while True:
        tmp = s
        for dup in dups:
            if dup in s:
                s = s.replace(dup, "")

        if tmp == s:
            return s


s = "deeedbbcccbdaa"
k = 3
print(removeDuplicates(None, s, k))
