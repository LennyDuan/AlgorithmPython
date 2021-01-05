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
    course_route = {i: [] for i in range(numCourses)}
    print(course_route)

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
        course_route[route_i].append(i)
        return True

    for i in range(numCourses):
        if not can_build_course(i, i):
            return []
        visited = [0] * numCourses

    all_routes = sorted(course_route.values(), key=lambda k: len(k), reverse=True)
    for route in all_routes:
        for i in route:
            if i not in res:
                res.append(i)
    print(res)
    return res[::-1]

numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# prerequisites = [[0, 1], [0, 2], [3, 1], [3, 2]]
# prerequisites = [[1, 3], [2, 3], [0, 1], [0, 2]]

print(canFinish(None, numCourses, prerequisites))
