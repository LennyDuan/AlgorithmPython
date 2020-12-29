def minPathSum(self, grid):
    if not grid:
        return 0
    y_end = len(grid) - 1
    x_end = len(grid[0]) - 1
    path = {
        (0, 0): grid[0][0]
    }

    def min_before(x, y):
        if x == y == 0:
            return 0
        from_left = path.get((x-1,y)) if x > 0 else float('inf')
        from_top =  path.get((x,y-1)) if y > 0 else float('inf')
        return min(from_left, from_top)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cur_min = grid[y][x] + min_before(x, y)
            path[(x, y)] = cur_min
    return path.get((x_end, y_end))


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

print(minPathSum(None, grid))
