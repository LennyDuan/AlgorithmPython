def solve(self, board):
    if not board:
        return board
    x_max = len(board[0])
    y_max = len(board)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(x, y, board):
        if board[y][x] != 'O':
            return

        board[y][x] = '.'
        for direction in directions:
            next_x, next_y = x + direction[0], y + direction[1]
            if 0 <= next_x < x_max and 0 <= next_y < y_max and board[next_y][next_x] == 'O':
                dfs(next_x, next_y, board)

    for i in range(x_max):
        dfs(i, 0, board)
        dfs(i, y_max - 1, board)

    for j in range(y_max):
        dfs(0, j, board)
        dfs(x_max - 1, j, board)

    for y in range(y_max):
        for x in range(x_max):
            board[y][x] = 'O' if board[y][x] == '.' else 'X'

    print(board)
    return board


board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']
]

board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'X', 'X']
]

#
# board = [
#     ["X", "O"],
#     ["O", "X"]
# ]
#
# board = [
#     ["O", "X", "X", "O", "X"],
#     ["X", "O", "O", "X", "O"],
#     ["X", "O", "X", "O", "X"],
#     ["O", "X", "O", "O", "O"],
#     ["X", "X", "O", "X", "O"]
# ]
#
board = [
    ["O", "O", "O", "O", "X", "X"],
    ["O", "O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O", "O"],
    ["O", "X", "O", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "O"],
    ["O", "X", "O", "O", "O", "O"]
]

board = [
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"],
    ["X", "O", "X", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "X"]
]

solve(None, board)
