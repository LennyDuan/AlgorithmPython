def pacificAtlantic(self, matrix):
    if not matrix:
        return []
    p_available = set()
    a_available = set()
    rows, cols = len(matrix), len(matrix[0])
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def traverse(i, j, available):
        if (i, j) in available:
            return
        available.add((i, j))
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                if matrix[next_i][next_j] >= matrix[i][j]:
                    traverse(next_i, next_j, available)

    for row in range(rows):
        traverse(row, 0, p_available)
        traverse(row, cols - 1, a_available)

    for col in range(cols):
        traverse(0, col, p_available)
        traverse(rows - 1, col, a_available)

    print(p_available)
    print(a_available)
    return list(p_available & a_available)


matrix = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]

print(pacificAtlantic(None, matrix))
