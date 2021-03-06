class MyHashMap:
    my_map = None
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_map = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.my_map[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return -1 if self.my_map.get(key) == None else self.my_map.get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if self.my_map.get(key):
            self.my_map.pop(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)