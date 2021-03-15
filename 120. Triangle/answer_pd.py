def minimumTotal(self, triangle) -> int:
    h = high = len(triangle)
    print(high)
    res = []
    points = {
        (0, 0): triangle[0][0]
    }

    for high in range(1, len(triangle)):
        for index in range(len(triangle[high])):
            before_left = (high - 1, index - 1)
            before_right = (high - 1, index)
            print(triangle[high][index])
            c_v = triangle[high][index] + min(
                points.get(before_left) if points.get(before_left) is not None else float('inf'),
                points.get(before_right) if points.get(before_right) is not None else float('inf')
            )
            points[(high, index)] = c_v
    print(points)
    for index in range(high + 1):
        val = points.get((h - 1, index))
        if val is not None:
            res.append(val)
    print(res)
    return min(res)


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
triangle = [[-10]]
triangle = [[-1],[2,3],[1,-1,-1]]
triangle = [[1],[-5,-2],[3,6,1],[-1,2,4,-3]]
print(minimumTotal(None, triangle))
