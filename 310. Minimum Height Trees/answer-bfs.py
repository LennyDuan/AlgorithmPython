from collections import defaultdict


def findMinHeightTrees(self, n: int, edges):
    if n <= 2:
        return [i for i in range(n)]
    adjencents = defaultdict(list)
    for edge in edges:
        start, end = edge[0], edge[1]
        adjencents[start].append(end)
        adjencents[end].append(start)
    print(adjencents)

    leaves = [node for node, paths in adjencents.items() if len(paths) == 1]
    print(leaves)

    remaining_nodes = n

    while remaining_nodes > 2:
        remaining_nodes -= len(leaves)
        new_leafs = []
        while leaves:
            leaf = leaves.pop()
            neighbor = adjencents[leaf].pop()
            adjencents[neighbor].remove(leaf)
            if len(adjencents[neighbor]) == 1:
                new_leafs.append(neighbor)

        leaves = new_leafs
    return leaves


n = 4
edges = [[1, 0], [1, 2], [1, 3]]

n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
print(findMinHeightTrees(None, n, edges))
