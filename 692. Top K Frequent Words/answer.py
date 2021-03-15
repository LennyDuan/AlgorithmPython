import collections


def topKFrequent(self, words: [], k: int):
    map = collections.Counter(words)
    print(map)
    sorted_map = sorted(map.items(), key=lambda x: (-x[1], x[0]))
    print(sorted_map)

    return [k for k, v in (sorted_map)][:k]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3

print(topKFrequent(None, words, k))
