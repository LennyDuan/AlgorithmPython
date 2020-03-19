def wordBreak(s: str, words: list()) -> bool:

    ok = [True]
    for i in range(1, len(s) + 1):

        ok += any(ok[j] and s[j:i] in words for j in range(i)),


    print(any(ok))
    return any(ok)


wordBreak("leetcode", ["leet", "code"])
