import collections


def longestWord(self, words) -> str:

    words.sort()
    print(words)
    valids = ['']
    for word in words:
        if word[0:-1] in valids:
            valids.append(word)
    print(valids)
    return max(valids, key=len)

    # return dfs(trie, 0)


# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
words = ["ogz", "eyj", "e", "ey", "hmn", "v", "hm", "ogznkb", "ogzn", "hmnm", "eyjuo", "vuq", "ogznk", "og", "eyjuoi",
         "d"]
# words = ["a", "app", "ap", "b",'bc','dc']
words = ["ogz", "eyj", "e", "ey", 'a', 'ejyob']

print(longestWord(None, words))
