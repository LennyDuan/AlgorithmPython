
def canFinish(self, numCourses: int, prerequisites) -> bool:
    def buildAdjacencyList(n, prerequisites):
        adjList = [[] for _ in range(n)]
        for start, end in prerequisites:
            adjList[end].append(start)
        return adjList

    adjList = buildAdjacencyList(numCourses, prerequisites)
    visited = [0] * numCourses

    print(adjList)
    print(visited)

    def hasCycle(i):
        if visited[i] == -1:
            return True
        if visited[i] == 1:
            return False

        for pre in adjList[i]:
            if hasCycle(pre):
                return True

        visited[i] = 1
        return False

    for i in range(numCourses):
        if hasCycle(i):
            return False

    return True


numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(None, numCourses, prerequisites))
