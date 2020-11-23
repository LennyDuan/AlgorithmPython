import collections


class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(list)
        results = []
        for equa, value in zip(equations, values):
            b, e = equa
            graph[b].append((e, value))
            graph[e].append((b, 1 / value))

        print(graph)

        def find_equa(b, e, equa, visited, graph):
            if not graph.get(b) or not graph.get(e) or b in visited:
                return -1

            if b is e:
                return equa

            visited.add(b)
            c_ends = graph.get(b)
            for c_end in c_ends:
                c_end_node, c_end_value = c_end
                tmp = find_equa(c_end_node, e, equa * c_end_value, visited, graph)
                if tmp != -1:
                    return tmp
            return -1

        for query in queries:
            b, e = query
            result = find_equa(b, e, 1, set(), graph.copy())
            results.append(result)

        return results


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]

queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
#
# equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
# values = [1.5, 2.5, 5.0]
# queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

print(Solution.calcEquation(0, equations, values, queries))
