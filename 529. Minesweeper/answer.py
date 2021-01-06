def updateBoard(self, board, click):
    if not board:
        return board
    c_y, c_x = click[0], click[1]
    y_len = len(board)
    x_len = len(board[0])
    if board[c_y][c_x] == 'M':
        board[c_y][c_x] = 'X'
        return board

    m_directions = [
        (1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)
    ]

    visited = {}

    def check_mine(x, y):
        if (x, y) in visited:
            return visited[(x, y)]

        if 0 <= x < x_len and 0 <= y < y_len:
            return board[y][x]
        else:
            return

    def reveal(x, y):
        print('----:', x, y)
        node_val = check_mine(x, y)
        if not node_val:
            return
        if node_val == 'M':
            visited[(x, y)] = board[y][x]
            return
        if node_val == 'B':
            return
        if node_val in '12345678':
            return

        if node_val == 'E':
            # Check 'M' Number
            count = 0
            for direction in m_directions:
                next_x, next_y = x + direction[0], y + direction[1]
                val = check_mine(next_x, next_y)
                if val == 'M':
                    count += 1
            print(count)
            # if is not 'B'
            if count > 0:
                visited[(x, y)] = str(count)
                print(x,y,count)
                board[y][x] = str(count)
                return
            else:
                visited[(x, y)] = 'B'
                board[y][x] = 'B'
                for direction in m_directions:
                    next_x, next_y = x + direction[0], y + direction[1]
                    reveal(next_x, next_y)

    reveal(c_x, c_y)
    return board


# board = [
#     ['E', 'E', 'E', 'E', 'E'],
#     ['E', 'E', 'M', 'E', 'E'],
#     ['E', 'E', 'E', 'E', 'E'],
#     ['E', 'E', 'E', 'E', 'E']
# ]
# click = [3, 0]

board = [
    ["E", "E", "E", "E", "E", "E", "E", "E"],
    ["E", "E", "E", "E", "E", "E", "E", "M"],
    ["E", "E", "M", "E", "E", "E", "E", "E"],
    ["M", "E", "E", "E", "E", "E", "E", "E"],
    ["E", "E", "E", "E", "E", "E", "E", "E"],
    ["E", "E", "E", "E", "E", "E", "E", "E"],
    ["E", "E", "E", "E", "E", "E", "E", "E"],
    ["E", "E", "M", "M", "E", "E", "E", "E"]]
click = [0, 0]

print(updateBoard(None, board, click))
