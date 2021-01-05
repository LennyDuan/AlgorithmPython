def canFinish(self, numCourses: int, prerequisites) -> bool:
    res = []
    visited = [0] * numCourses

    def buildAdjacencyList(n, prerequisites):
        adjList = [[] for _ in range(n)]
        for start, end in prerequisites:
            adjList[end].append(start)
        return adjList

    adjList = buildAdjacencyList(numCourses, prerequisites)
    print(adjList)

    def can_build_course(i, route_i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1

        for pre in adjList[i]:
            if not can_build_course(pre, route_i):
                return False
        visited[i] = 1
        res.append(i)
        return True

    for i in range(numCourses):
        if visited[i] == 0:
            if not can_build_course(i, i):
                return []

    return res[::-1]

numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# prerequisites = [[0, 1], [0, 2], [3, 1], [3, 2]]
# prerequisites = [[1, 3], [2, 3], [0, 1], [0, 2]]

print(canFinish(None, numCourses, prerequisites))
