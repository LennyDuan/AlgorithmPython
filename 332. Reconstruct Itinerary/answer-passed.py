from collections import defaultdict


class Solution:

    def findItinerary(self, tickets):
        route = []
        adj_list = defaultdict(list)

        for i, j in tickets:
            adj_list[i].append(j)
        for key in adj_list:
            adj_list[key] = sorted(adj_list[key])
        print(route)
        print(adj_list)

        def visit(airport):
            while adj_list[airport]:
                visit(adj_list[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]


tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
print(Solution().findItinerary(tickets))
