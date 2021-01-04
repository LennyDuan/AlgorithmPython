def pacificAtlantic(self, matrix):
    if not matrix:
        return []
    res = []
    x_min = y_min = 0
    y_max = len(matrix)  # 1
    x_max = len(matrix[0])  # 5
    matric_visited = [[[False, False] for _ in range(x_max)] for _ in range(y_max)]

    def water_flow_P(x, y, pre_v, c_res=dict, visited=[]):
        if x < x_min or x >= x_max or y < y_min or y > y_max - 1 or visited[x][y]:
            return
        visited[x][y] = True

        if matric_visited[y][x][0]:
            c_res['P'] = True
            return

        if pre_v >= matrix[y][x]:
            if x == x_min or y == y_min:
                c_res['P'] = True
                matric_visited[y][x][0] = True
                return
            water_flow_P(x - 1, y, matrix[y][x], c_res, visited)
            water_flow_P(x + 1, y, matrix[y][x], c_res, visited)
            water_flow_P(x, y + 1, matrix[y][x], c_res, visited)
            water_flow_P(x, y - 1, matrix[y][x], c_res, visited)
        else:
            return

    def water_flow_A(x, y, pre_v, c_res=dict, visited=[]):

        if x < x_min or x > x_max - 1 or y < y_min or y > y_max - 1 or visited[x][y]:
            return
        visited[x][y] = True

        if matric_visited[y][x][1]:
            c_res['A'] = True
            return
        if pre_v >= matrix[y][x]:
            if x == x_max - 1 or y == y_max - 1:
                c_res['A'] = True
                matric_visited[y][x][1] = True
                return
            water_flow_A(x, y + 1, matrix[y][x], c_res, visited)
            water_flow_A(x + 1, y, matrix[y][x], c_res, visited)
            water_flow_A(x - 1, y, matrix[y][x], c_res, visited)
            water_flow_A(x, y - 1, matrix[y][x], c_res, visited)
        else:
            return

    for y in range(y_max):  # 0 ~
        for x in range(x_max):  # 0 ~ 4
            print('-----')
            c_res = {
                'P': False,
                'A': False,
            }
            visited = [[False for _ in range(y_max)] for _ in range(x_max)]
            water_flow_P(x, y, matrix[y][x], c_res, visited)
            visited = [[False for _ in range(y_max)] for _ in range(x_max)]
            water_flow_A(x, y, matrix[y][x], c_res, visited)

            if c_res['P'] and c_res['A']:
                available_point = [y, x]
                res.append(available_point)
            print(y, x, matrix[y][x], c_res)

    return res


matrix = [
    # [8, 13, 11, 18, 14, 16, 16, 4, 4, 8, 10, 11, 1, 19, 7],
    #       [2, 9, 15, 16, 14, 5, 8, 15, 9, 5, 14, 6, 10, 15, 5],
    #       [15, 16, 17, 10, 3, 6, 3, 4, 2, 17, 0, 12, 4, 1, 3],
    #       [13, 6, 13, 15, 15, 16, 4, 10, 7, 4, 19, 19, 4, 9, 13],
    #       [7, 1, 9, 14, 9, 11, 5, 4, 15, 19, 6, 0, 0, 13, 5],
    #       [9, 9, 15, 12, 15, 5, 1, 1, 18, 1, 2, 16, 15, 18, 9],
    #       [13, 0, 4, 18, 12, 0, 11, 0, 1, 15, 1, 15, 4, 2, 0],
    #       [11, 13, 12, 16, 9, 18, 6, 8, 18, 1, 5, 12, 17, 13, 5],
    #       [7, 17, 2, 5, 0, 17, 9, 18, 4, 13, 6, 13, 7, 2, 1],
    #       [2, 3, 9, 0, 19, 6, 6, 15, 14, 4, 8, 1, 19, 5, 9],
    #       [3, 10, 5, 11, 7, 14, 1, 5, 3, 19, 12, 5, 2, 13, 16],
    #       [0, 8, 10, 18, 17, 5, 5, 8, 2, 11, 5, 16, 4, 9, 14],
    #       [15, 9, 16, 18, 9, 5, 2, 5, 13, 3, 10, 19, 9, 14, 3],
    #       [12, 11, 16, 1, 10, 12, 6, 18, 6, 6, 18, 10, 9, 5, 2],
    #       [17, 9, 6, 6, 14, 9, 2, 2, 13, 13, 15, 17, 15, 3, 14],
    #       [18, 14, 12, 6, 18, 16, 4, 10, 19, 5, 6, 8, 9, 1, 6]]
    [12, 7, 7, 14, 6, 17, 12, 17, 8, 18, 9, 5],
    [6, 8, 12, 5, 3, 6, 2, 14, 19, 6, 18, 13],
    [0, 6, 3, 8, 8, 10, 8, 17, 13, 13, 13, 12],
    [5, 6, 8, 8, 15, 16, 19, 14, 7, 11, 2, 3],
    [7, 18, 2, 7, 10, 10, 3, 14, 13, 15, 15, 7],
    [18, 6, 19, 4, 12, 3, 3, 2, 6, 6, 19, 6],
    [3, 18, 5, 16, 19, 6, 3, 12, 6, 0, 14, 11],
    [9, 10, 17, 12, 10, 11, 11, 9, 0, 0, 12, 0],
    [4, 13, 3, 0, 4, 12, 9, 5, 6, 17, 10, 11],
    [18, 3, 5, 0, 8, 19, 18, 4, 8, 19, 1, 3],
    [16, 2, 14, 6, 4, 14, 7, 2, 9, 7, 13, 18],
    [0, 16, 19, 16, 16, 4, 15, 19, 7, 0, 3, 16],
    [13, 8, 12, 8, 2, 3, 5, 18, 6, 15, 18, 6],
    [4, 10, 8, 1, 16, 0, 6, 0, 14, 10, 11, 8],
    [7, 1, 3, 4, 11, 12, 9, 0, 6, 2, 17, 5],
    [1, 16, 6, 1, 0, 19, 11, 1, 5, 7, 8, 2],
    [4, 1, 14, 13, 14, 7, 3, 7, 1, 9, 15, 18],
    [14, 11, 6, 14, 14, 14, 4, 0, 11, 17, 1, 9],
    [3, 14, 2, 10, 3, 1, 9, 16, 1, 13, 0, 15],
    [8, 9, 13, 5, 5, 7, 10, 1, 4, 5, 0, 9],
    [13, 16, 15, 5, 17, 6, 16, 13, 5, 7, 3, 15],
    [5, 1, 12, 19, 3, 13, 0, 0, 3, 10, 6, 13],
    [12, 17, 9, 16, 16, 6, 2, 6, 12, 15, 14, 16],
    [7, 7, 0, 6, 4, 15, 1, 7, 17, 5, 2, 12],
    [3, 17, 0, 2, 4, 5, 11, 7, 16, 16, 16, 13], [3, 7, 16, 11, 2, 16, 14, 9, 16, 17, 10, 3],
    [12, 18, 17, 17, 5, 15, 1, 2, 12, 12, 5, 7], [11, 10, 10, 0, 11, 7, 17, 14, 5, 15, 2, 16],
    [7, 19, 14, 7, 6, 2, 4, 16, 11, 19, 14, 14], [6, 17, 6, 6, 6, 15, 9, 12, 8, 13, 1, 7],
    [16, 3, 15, 0, 18, 17, 0, 11, 3, 16, 11, 12], [15, 12, 4, 6, 19, 15, 17, 7, 3, 9, 2, 11]]
# #     [
#     # [1, 2, 2, 3, 5],
#     # [3, 2, 3, 4, 4],
#     # [2, 4, 5, 3, 1],
#     # [6, 7, 1, 4, 5],
#     # [5, 1, 1, 2, 4]
# ]

print(pacificAtlantic(None, matrix))
