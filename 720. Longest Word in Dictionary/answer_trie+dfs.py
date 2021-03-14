import collections


def longestWord(self, words) -> str:
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    END = 'END'
    for word in words:
        root = trie
        for letter in word:
            root = root[letter]
        root[END] = True
    words.sort()
    print(words)
    words = []
    print(trie.keys())
    print(trie['e'])

    def dfs(node, word):
        if not node or node is True or (node[END] is True and len(node.keys()) == 1):
            return
        for key in node.keys():
            if key is not END and True in node[key].values():
                print(node[key].values())
                words.append(word + key)
                dfs(node[key], word + key)

    dfs(trie, '')
    words.sort()
    print(words)
    return max(words, key=len)

    # return dfs(trie, 0)


# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
words = ["ogz", "eyj", "e", "ey", "hmn", "v", "hm", "ogznkb", "ogzn", "hmnm", "eyjuo", "vuq", "ogznk", "og", "eyjuoi",
         "d"]
# words = ["a", "app", "ap", "b",'bc','dc']
words = ["ogz", "eyj", "e", "ey", 'a', 'ejyob']

print(longestWord(None, words))
