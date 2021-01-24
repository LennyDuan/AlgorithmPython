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
    roots = [node for node, paths in adjencents.items() if len(paths) != 1]
    print(roots)

    def get_path_height(node, visited=[]):
        if node in visited:
            return 0
        visited.append(node)

        steps = []
        for next_node in adjencents[node]:
            step = get_path_height(next_node, visited) + 1
            steps.append(step)

        return max(steps)

    all_paths = []
    for root in roots:
        root_step = get_path_height(root, [])
        all_paths.append([root, root_step])
    print(all_paths)
    new_paths = sorted(all_paths, key=lambda val: val[1])
    print(new_paths)
    res = [node for node, step in new_paths if step == new_paths[0][1]]

    return res


n = 4
edges = [[1, 0], [1, 2], [1, 3]]

n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
print(findMinHeightTrees(None, n, edges))
