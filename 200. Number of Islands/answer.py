def numIslands(grid) -> int:
    y_strat = 0
    x_start = 0

    y_max = len(grid) - 1
    x_max = len(grid[0]) - 1

    total = 0

    def find_island(x, y, c_visited):
        print('x: {} y: {}'.format(x, y))
        if grid[y][x] is "1":
            c_visited.append((x, y))
            grid[y][x] = "0"

            if x_can_right(x, y):
                find_island(x + 1, y, c_visited)
            if y_can_down(x, y):
                find_island(x, y + 1, c_visited)
            if x_can_left(x, y):
                find_island(x - 1, y, c_visited)
            if y_can_top(x, y):
                find_island(x, y - 1, c_visited)
        return c_visited

    def x_can_right(x, y):
        if x_start <= x + 1 <= x_max and grid[y][x + 1] is "1":
            return True
        return False

    def x_can_left(x, y):
        if x_start <= x - 1 <= x_max and grid[y][x - 1] is "1":
            return True
        return False

    def y_can_top(x, y):
        if y_strat <= y - 1 <= y_max and grid[y - 1][x] is "1":
            return True
        return False

    def y_can_down(x, y):
        if y_strat <= y + 1 <= y_max and grid[y + 1][x] is "1":
            return True
        return False

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            current_visited = find_island(x, y, list())
            if len(current_visited) > 0:
                print('----')
                total += 1

    return total


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

grid3 = [["1", "0", "1", "1", "0", "1", "1"]]

grid4 = [
    ["0", "1", "0"],
    ["1", "0", "1"],
    ["0", "1", "0"]]

grid5 = [
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"]]

print(numIslands(grid))
