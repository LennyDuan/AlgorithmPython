from functools import cmp_to_key


class Player:
    name = str()
    score = int()

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return self.name + ' ' + self.score

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            return 1 if a.name > b.name else -1


n = int(input())