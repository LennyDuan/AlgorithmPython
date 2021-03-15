def arrayRankTransform(self, arr):
    rank_dict = {k: i + 1 for i, k in enumerate(sorted(set(arr)))}
    return [rank_dict.get(key) for key in arr]


# arr = [40, 10, 20, 30]
arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
print(arrayRankTransform(None, arr))
