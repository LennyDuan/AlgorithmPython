from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        results = list()

        order_equa_dict = defaultdict(str)
        r_order_equa_dict = defaultdict(str)
        equa_dict_with_value = defaultdict(float)

        for i, equa in enumerate(equations):
            order_equa_dict[equa[0]] = equa[1]
            r_order_equa_dict[equa[1]] = equa[0]
            equa_dict_with_value[(equa[0], equa[1])] = values[i]
            equa_dict_with_value[(equa[1], equa[0])] = 1 / values[i]

        def find_equa_route_total(start, end, c_equa, current_equa_dict, r_current_equa_dict, visited):
            print('Look equa {} -> {}'.format(start, end))

            if current_equa_dict.get(start):
                c_end = order_equa_dict.get(start)
                print('look order {}:{}', start, c_end)
                c_equa *= equa_dict_with_value.get((start, c_end))
                if current_equa_dict.get(start) is end:
                    return c_equa

                current_equa_dict[start] = None
                print('next look {}:{}', c_end, end)

                if start in visited:
                    if end not in visited:
                        return -1
                    return c_equa
                visited.add(start)

                return find_equa_route_total(c_end, end, c_equa, current_equa_dict, r_current_equa_dict, visited)

            elif r_current_equa_dict.get(start):
                c_end = r_current_equa_dict.get(start)
                print('look r order {}:{}', start, c_end)
                c_equa *= equa_dict_with_value.get((start, c_end))
                if r_current_equa_dict.get(start) is end:
                    return c_equa

                r_current_equa_dict[start] = None
                print('next look {}:{}', c_end, end)

                if start in visited:
                    if end not in visited:
                        return -1
                    return c_equa
                visited.add(start)

                return find_equa_route_total(c_end, end, c_equa, current_equa_dict, r_current_equa_dict, visited)

            else:
                return -1

        for query in queries:
            print('---\nfind equa: {}'.format(query))
            current_equa_dict = order_equa_dict.copy()
            r_current_equa_dict = r_order_equa_dict.copy()
            result = find_equa_route_total(query[0], query[1], 1, current_equa_dict, r_current_equa_dict, set())
            print('Get equa value: {}'.format(result))
            results.append(result)

        print(order_equa_dict)
        print(r_order_equa_dict)
        print(equa_dict_with_value)
        return results


#
# equations = [["a", "b"], ["b", "c"]]
# values = [2.0, 3.0]
#
# queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]
queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

print(Solution.calcEquation(0, equations, values, queries))
