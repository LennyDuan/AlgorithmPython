class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['#'] = {}

    def search(self, word: str) -> bool:
        return self.dfs(self.trie, word)

    def dfs(self, trie, word):
        if not word and '#' in trie:
            return True
        elif not word or not trie:
            return False

        f_c = word[0]

        if f_c == '.':
            return any(self.dfs(trie[c], word[1:]) for c in trie.keys())
        else:
            if f_c in trie:
                trie = trie[f_c]
                return self.dfs(trie, word[1:])
            else:
                return False

