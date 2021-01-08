def updateMatrix(self, matrix):
    res = matrix
    if not matrix:
        return matrix
    y_max = len(matrix)
    x_max = len(matrix[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = []

    def find_min(x, y, visited):
        print(x, y, matrix[y][0])
        if (x, y) in visited:
            return res[y][x]
        if 0 <= x < x_max and 0 <= y < y_max:
            if not matrix[y][x]:
                visited.append((x, y))
                return 0
            else:
                neighbours = []
                for direction in directions:
                    n_x, n_y = x + direction[0], y + direction[1]
                    d_v = find_min(n_x, n_y, visited)
                    neighbours.append(find_min(n_x, n_y, visited))
                    if d_v == 0:
                        break

                n_m = min(neighbours)
                c_m = 1 + n_m
                visited.append((x, y))
                res[y][x] = c_m
                return c_m

        return float('inf')

    for y in range(y_max):
        for x in range(x_max):
            print('---', x, y)
            c_xy = find_min(x, y, visited)
            res[y][x] = c_xy
    return res


matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]]

print(updateMatrix(None, matrix))
