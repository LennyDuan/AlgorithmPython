def minimumTotal(self, triangle) -> int:
    res = 0
    hight = len(triangle)
    res = []

    def dfs(subsum, level, index):
        if level >= hight:
            return

        current_val = triangle[level][index]
        subsum += current_val
        if level + 1 == hight:
            res.append(subsum)
            return
        dfs(subsum, level+1, index)
        dfs(subsum, level+1, index+1)

    dfs(0, 0, 0)
    print(res)
    return min(res)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(minimumTotal(None, triangle))
