class MyHashSet:
    build_in_set = None
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.build_in_set = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.build_in_set.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.build_in_set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.build_in_set
        """
        Returns true if this set contains the specified element
        """

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)