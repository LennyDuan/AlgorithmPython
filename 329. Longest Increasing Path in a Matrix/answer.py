def longestIncreasingPath(self, matrix) -> int:
    if not matrix:
        return 0
    res = 0
    visited = set()
    rows, cols = len(matrix), len(matrix[0])
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j, visited):
        if (i, j) in visited:
            return 0
        res = 1
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            direction_count = 0
            if 0 <= next_i < rows and 0 <= next_j < cols:
                if matrix[next_i][next_j] > matrix[i][j]:
                    direction_count = 1 + traverse(next_i, next_j, visited)

            res = max(res, direction_count)
        return res

    for row in range(rows):
        for col in range(cols):
            res = max(traverse(row, col, visited), res)

    return res


nums = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]

print(longestIncreasingPath(None, nums))
