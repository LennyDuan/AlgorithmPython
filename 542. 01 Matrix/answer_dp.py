def updateMatrix(self, matrix):
    if not matrix:
        return matrix
    y_max = len(matrix)
    x_max = len(matrix[0])

    for y in range(y_max):
        for x in range(x_max):
            if matrix[y][x] :
                top = matrix[y - 1][x] if y else float('inf')
                left = matrix[y][x - 1] if x else float('inf')
                matrix[y][x] = min(top, left) + 1

    for y in range(y_max - 1, -1, -1):
        for x in range(x_max - 1, -1, -1):
            bottom = matrix[y + 1][x] if y < y_max - 1 else float('inf')
            right = matrix[y][x + 1] if x < x_max - 1 else float('inf')
            matrix[y][x] = min(matrix[y][x], bottom + 1, right + 1)
    return matrix


matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]]

print(updateMatrix(None, matrix))
