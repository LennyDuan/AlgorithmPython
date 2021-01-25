class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        on_board = [0, 0]
        directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

        def is_on_board(x, y):
            return 0 <= x < N and 0 <= y < N

        def move(x, y, k):
            if k == 0 and is_on_board(x, y):
                on_board[0] += 1
                return
            elif not is_on_board(x, y):
                on_board[1] += (8 * (k)) or 1
                return

            elif k and is_on_board(x, y):
                for direction in directions:
                    next_x, next_y = x + direction[0], y + direction[1]
                    move(next_x, next_y, k - 1)

        move(r, c, K)
        print(on_board)

        return on_board[0] / sum(on_board) if on_board[1] else 0


# 0.01562
print(Solution.knightProbability(None, 3, 3, 0, 0))

# 0.25
print(Solution.knightProbability(None, 3, 1, 0, 0))
# 0.625
print(Solution.knightProbability(None, 3, 2, 0, 0))
