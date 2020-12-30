class LRUCache:
    def __init__(self, capacity: int):
        from collections import defaultdict
        self.cache = {}
        self.capacity = capacity
        self.queue = []

    def get(self, key: int) -> int:
        if not self.cache.get(key):
            return -1

        self.queue.remove(key)
        self.queue.append(key)

        return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.queue.remove(key)

        elif len(self.cache.keys()) == self.capacity:
            del self.cache[self.queue.pop(0)]

        self.cache[key] = value
        self.queue.append(key)



