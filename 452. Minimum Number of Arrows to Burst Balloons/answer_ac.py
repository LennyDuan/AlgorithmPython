def findMinArrowShots(self, points: [[int]]) -> int:
    res = 0
    sorted_points = sorted(points, key=lambda x: x[0])
    print(sorted_points)

    def find_min_max(arr):
        c_min = arr[0][0]
        c_max = arr[0][1]
        c_index = 0
        for pair in arr:
            start, end = pair[0], pair[1]
            if start > c_max:
                break
            if start >= c_min:
                c_min = start
            if end <= c_max:
                c_max = end
            c_index += 1
        return c_index

    while sorted_points:
        min_max_index = find_min_max(sorted_points)
        res += 1
        sorted_points = sorted_points[min_max_index:]

    return res


points = [[10, 16], [2, 8], [1, 6], [7, 12]]

points = [[1,2],[3,4],[5,6],[7,8]]

print(findMinArrowShots(None, points))
