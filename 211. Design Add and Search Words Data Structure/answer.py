class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = ''

    def addWord(self, word: str) -> None:
        self.dic += word

    def search(self, word: str) -> bool:
        s_w = word.replace(',', '')
        return s_w in self.dic