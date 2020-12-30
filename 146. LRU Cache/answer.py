class LRUCache:
    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.cache = OrderedDict(int)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not self.cache.get(key):
            return -1

        value = self.cache.pop(key)
        self.cache[key] = value

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)

        elif len(self.cache.keys()) == self.capacity:
            del self.cache[self.cache.pop(0)]

        self.cache[key] = value



