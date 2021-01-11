def allPathsSourceTarget(self, graph):
    res = []
    start = 0
    target = len(graph) - 1
    path = [start]

    def find_all_routes(currNode, path):
        if currNode == target:
            res.append(list(path))
            return
            # explore the neighbor nodes one after another.
        for nextNode in graph[currNode]:
            path.append(nextNode)
            find_all_routes(nextNode, path)
            path.pop()

    find_all_routes(0, path)

    return res


# graph = [[1, 2], [3], [3], []]
# Output: [[0,1,3],[0,2,3]]

graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

# graph = [[4, 3, 1], [3, 2, 4], [], [4], []]
# [[0,4],[0,3,4],[0,1,3,4],[0,1,4]]

print(allPathsSourceTarget(None, graph))
