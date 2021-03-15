def arrayRankTransform(self, arr):
    arr_set = list(set(arr))
    sorted_arr = (sorted(arr_set))
    print(sorted_arr)

    res = [sorted_arr.index(ele) + 1 for ele in arr]

    return res


# arr = [40, 10, 20, 30]
arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
print(arrayRankTransform(None, arr))
