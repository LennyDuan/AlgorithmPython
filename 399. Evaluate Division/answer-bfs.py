import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(list)
        results = []
        for equa, value in zip(equations, values):
            b, e = equa
            graph[b].append((e, value))
            graph[e].append((b, 1 / value))

        def find_value(query):
            b, e = query
            if b not in graph or e not in graph:
                return -1
            visited = set()
            q = [(b, 1)]

            while q:
                c_node = q.pop(0)
                c_b, total = c_node
                visited.add(c_b)
                if c_b is e:
                    return total

                for c_e, value in graph.get(c_b):
                    if c_e not in visited:
                        q.append((c_e, total * value))
            return -1

        for query in queries:
            value = find_value(query)
            results.append(value)

        return results


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
# queries = [["a", "b"]]

queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
#
# equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
# values = [1.5, 2.5, 5.0]
# queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

print(Solution.calcEquation(0, equations, values, queries))
