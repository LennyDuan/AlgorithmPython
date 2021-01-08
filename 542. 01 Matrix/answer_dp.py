def updateMatrix(self, matrix):
    if not matrix:
        return matrix
    y_max = len(matrix)
    x_max = len(matrix[0])
    res = matrix[:]

    for y in range(y_max):
        for x in range(x_max):
            if matrix[y][x] == 0:
                res[y][x] = 0
            else:
                if x > 0:
                    res[y][x] = 1 + min(res[y][x], res[y][x - 1])
                if y > 0:
                    res[y][x] = 1 + min(res[y][x], res[y - 1][x])

    for y in range(y_max - 1, -1, -1):
        for x in range(x_max - 1, -1, -1):
            if x < x_max -1:
                res[y][x] = min(res[y][x], 1 + res[y][x + 1])
            if y < y_max - 1:
                res[y][x] = min(res[y][x], 1 + res[y + 1][x])
    return res


matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]]

print(updateMatrix(None, matrix))
