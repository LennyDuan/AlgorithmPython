def kthSmallest(self, matrix, k: int) -> int:
    total_array = []
    for arr in matrix:
        total_array += arr

    print(total_array, k)
    return sorted(total_array)[k-1]


matrix = [
 [1, 5, 9],
 [10, 11, 13],
 [12, 13, 15]
]
k = 8
print(kthSmallest(None, matrix, k))
