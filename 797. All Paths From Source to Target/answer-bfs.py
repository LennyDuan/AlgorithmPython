def allPathsSourceTarget(self, graph):
    res = []
    start = 0
    end = len(graph) - 1

    path = [start]
    queue = [(graph[0], path)]

    while queue:
        val = queue.pop(0)
        routes, path = val[0], val[1]

        for route in routes:
            new_path = [] + path
            new_path.append(route)

            if route == end:
                res.append(new_path)

            next_routes = graph[route]
            queue.append((next_routes, new_path))

    return res


graph = [[1, 2], [3], [3], []]
# Output: [[0,1,3],[0,2,3]]

graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

graph = [[4, 3, 1], [3, 2, 4], [], [4], []]
# [[0,4],[0,3,4],[0,1,3,4],[0,1,4]]

print(allPathsSourceTarget(None, graph))
