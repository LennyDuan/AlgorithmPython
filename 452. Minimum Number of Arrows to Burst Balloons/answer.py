def findMinArrowShots(self, points: [[int]]) -> int:
    res = 0
    sorted_points = sorted(points, key=lambda x: x[0])[::-1]
    start = float('inf')

    for point in sorted_points:
        if start > point[1]:
            res += 1
            start = point[0]

    return res


points = [[10, 16], [2, 8], [1, 6], [7, 12]]

# points = [[1,2],[3,4],[5,6],[7,8]]

print(findMinArrowShots(None, points))
