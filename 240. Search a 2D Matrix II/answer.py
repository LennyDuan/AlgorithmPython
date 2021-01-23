def searchMatrix(self, matrix, target: int) -> bool:
    x = -1
    for y in matrix:
        while x + len(y) and y[x] > target:
            x -= 1
        if y[x] == target:
            return True
    return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
print(searchMatrix(None, matrix, target))
