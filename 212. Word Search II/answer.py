def findWords(self, board, words):
    res = []
    if not board:
        return []
    y_max = len(board)
    x_max = len(board[0])
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def find_word(x, y, word, visited):
        if len(word) == 0:
            return True

        if (x, y) in visited:
            return

        if not (0 <= x < x_max and 0 <= y < y_max):
            return

        else:
            if board[y][x] == word[0]:
                visited.append((x, y))
                for direction in directions:
                    next_x, next_y = x + direction[0], y + direction[1]
                    if find_word(next_x, next_y, word[1:], visited):
                        return True
            return

    for word in words:
        find = False
        for y in range(y_max):
            for x in range(x_max):
                visited = []
                if find_word(x, y, word, visited):
                    find = True
        if find:
            res.append(word)
    return res


# Input:
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
# Output: ["eat", "oath"]

board = [["a", "b"], ["c", "d"]]
words = ["abcb"]
# Output: []

board = [
    ["a", "b", "c"],
    ["a", "e", "d"],
    ["a", "f", "g"]
]
words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]
# ["abcdefg","befa","eaabcdgfa","gfedcbaaa"]
print(findWords(None, board, words))
