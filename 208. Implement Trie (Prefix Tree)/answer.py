class Trie:

    def __init__(self):
        self.trie = {}
        """
        Initialize your data structure here.
        """

    def insert(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['#'] = '#'

        """
        Inserts a word into the trie.
        """

    def search(self, word: str) -> bool:
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        if '#' in trie:
            return True
        return False
        """
        Returns if the word is in the trie.
        """

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        trie = self.trie
        for c in prefix:
            if c not in trie:
                return False
            trie = trie[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)