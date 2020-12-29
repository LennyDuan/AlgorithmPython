def exist(self, board, word):
    if not board:
        return False

    y_max = len(board) - 1
    x_max = len(board[0]) - 1

    def isValid(x, y, word, c_board):
        if len(word) is 0:
            return True

        if x < 0 or y < 0 or x > x_max or y > y_max or word[0] != c_board[y][x]:
            return False
        current_char = c_board[y][x]
        c_board[y][x] = '-'

        res = isValid(x - 1, y, word[1:], c_board) or isValid(x + 1, y, word[1:], c_board) \
              or isValid(x, y - 1, word[1:], c_board) or isValid(x, y + 1, word[1:], c_board)
        c_board[y][x] = current_char
        return res

    for y_c in range(len(board)):
        for x_c in range(len(board[0])):
            word_list = [char for char in word]
            if isValid(x_c, y_c, word_list, board):
                return True
    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"

board = [["a", "b"], ["c", "d"]]
word = "acdb"
# #
# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCCED"

# board = [["a", "b"], ["c", "d"]]
# word = "abcd"

board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCEFSADEESE"
print(exist(None, board, word))
