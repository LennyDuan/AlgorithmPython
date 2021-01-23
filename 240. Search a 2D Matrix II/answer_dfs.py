def searchMatrix(self, matrix, target: int) -> bool:
    if not matrix:
        return False
    y_max = len(matrix)
    x_max = len(matrix[0])

    res = [False]

    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def search(x, y, visited=[]):
        if matrix[y][x] == target:
            res[0] = True
            return
        if (x, y) in visited:
            return
        visited.append((x, y))

        for direction in directions:
            next_x, next_y = x + direction[0], y + direction[1]
            if 0 <= next_x < x_max and 0 <= next_y < y_max:
                search(next_x, next_y, visited)

    search(0, 0, [])
    return res[0]


matrix = [[1, 4, 7, 11, 15], [2, 3, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 2]]
target = 5
print(searchMatrix(None, matrix, target))
