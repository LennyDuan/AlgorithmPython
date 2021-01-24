def solve(self, board):
    if not board:
        return board
    x_max = len(board[0])
    y_max = len(board)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def is_board(x, y):
        if x == 0 or x == x_max - 1 or y == 0 or y == y_max - 1:
            return True

    def update_board(x, y, visited_O):
        if is_board(x, y):
            return
        if (x, y) in visited_O:
            return
        visited_O.append((x, y))
        completed = []
        for direction in directions:
            next_x, next_y = x + direction[0], y + direction[1]
            if (next_x, next_y) in visited_O or board[next_y][next_x] == 'X':
                completed.append(True)
        print(completed)
        if len(completed) == 4:
            for visited in visited_O:
                x_o, y_o = visited[0], visited[1]
                board[y_o][x_o] = 'X'
            return

        for direction in directions:
            next_x, next_y = x + direction[0], y + direction[1]
            if 0 <= next_x < x_max and y <= next_y < y_max:
                if board[next_y][next_x] == 'O':
                    update_board(next_x, next_y, visited_O)

    for y in range(y_max):
        for x in range(x_max):
            if board[y][x] == 'O':
                print(x, y)
                update_board(x, y, [])
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
# board = [
#     ["O", "O", "O", "O", "X", "X"],
#     ["O", "O", "O", "O", "O", "O"],
#     ["O", "X", "O", "X", "O", "O"],
#     ["O", "X", "O", "O", "X", "O"],
#     ["O", "X", "O", "X", "O", "O"],
#     ["O", "X", "O", "O", "O", "O"]
# ]
solve(None, board)
