def updateMatrix(self, matrix):
    if not matrix:
        return matrix
    y_max = len(matrix)
    x_max = len(matrix[0])
    res = [[float('inf') for _ in range(x_max)] for _ in range(y_max)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = []
    for y in range(y_max):
        for x in range(x_max):
            if matrix[y][x] == 0:
                res[y][x] = 0
                queue.append((x, y))

    while queue:
        c_n = queue.pop(0)
        c_x, c_y = c_n[0], c_n[1]
        for direction in directions:
            next_x, next_y = c_x + direction[0], c_y + direction[1]
            if 0 <= next_x < x_max and 0 <= next_y < y_max:
                if res[next_y][next_x] > res[c_y][c_x]:
                    c_v = 1 + res[c_y][c_x]
                    res[next_y][next_x] = c_v
                    queue.append((next_x, next_y))

    return res


matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]]
#
# matrix = [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1],
#     [1, 1, 1]]

print(updateMatrix(None, matrix))
