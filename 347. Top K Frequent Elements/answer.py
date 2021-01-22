from collections import Counter


def topKFrequent(self, nums, k: int):
    counter_dict = Counter(nums)
    print(counter_dict)
    res = [k for k,_ in counter_dict.most_common(k)]
    return res


nums = [1, 1, 1, 2, 2, 3]
nums = [1, 1, 1, 2, 2, 3, 3, 3, 3]

k = 2
print(topKFrequent(None, nums, k))
