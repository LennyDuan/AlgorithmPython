from collections import defaultdict


def minTime(self, n: int, edges, hasApple):
    adjacent = defaultdict(list)
    for edge in edges:
        adjacent[edge[0]].append(edge[1])
        adjacent[edge[1]].append(edge[0])

    print(adjacent)

    def dfs(node, res, visited):
        if node in visited:
            return
        found = False
        visited.append(node)
        for next_node in adjacent[node]:
            if dfs(next_node, res, visited):
                found = True
                res[0] += 2

        return found or hasApple[node]

    res = [0]
    dfs(0, res, [])
    return res[0]


n = 7
edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
hasApple = [False, False, True, False, True, True, False]

print(minTime(None, n, edges, hasApple))


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        paths = defaultdict(set)
        for frm, to in edges:
            paths[frm].add(to)
            paths[to].add(frm)

        self.cost = 0
        seen = set()
        def dfs(current):
            found = False
            if current in seen:
                return
            seen.add(current)
            for nxt in paths[current]:
                if dfs(nxt):
                    found = True
                    self.cost += 2

            return found or hasApple[current]

        dfs(0)
        return self.cost