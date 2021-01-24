from collections import defaultdict


def minTime(self, n: int, edges, hasApple):
    adjacent = defaultdict(list)
    for edge in edges:
        adjacent[edge[0]].append(edge[1])
    print(adjacent)

    apples_time = []

    def find_apple(start, current_time):
        if hasApple[start]:
            apples_time.append(current_time)

        nodes = adjacent[start]
        if nodes:
            for next_node in nodes:
                find_apple(next_node, current_time + 2)

    find_apple(0, 0)
    print(apples_time)

    return sum(apples_time)


n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]

print(minTime(None, n, edges, hasApple))
