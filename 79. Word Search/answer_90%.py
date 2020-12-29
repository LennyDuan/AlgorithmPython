from collections import defaultdict


def exist(self, board, word):
    res = False
    if not board:
        return False

    x_min = y_min = 0
    y_max = len(board) - 1
    x_max = len(board[0]) - 1
    found = []

    def isValid(x, y, word, visited):

        if visited[(x, y)]:
            return

        current_char = board[y][x]
        first_char_in_word = word[0]
        print(current_char, first_char_in_word, word)

        if current_char == first_char_in_word:
            visited[(x, y)] = True

            if len(word) is 1:
                found.append(True)
                return

            if x + 1 <= x_max:
                isValid(x + 1, y, word[1:], visited)
            if y + 1 <= y_max:
                isValid(x, y + 1, word[1:], visited)
            if x - 1 >= x_min:
                isValid(x - 1, y, word[1:], visited)
            if y - 1 >= y_min:
                isValid(x, y - 1, word[1:], visited)
        else:
            visited[(x, y)] = False

    for y_c in range(len(board)):
        for x_c in range(len(board[0])):
            word_list = [char for char in word]
            isValid(x_c, y_c, word_list, defaultdict(bool))
            if found:
                return True
            print('---')

    return res


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
