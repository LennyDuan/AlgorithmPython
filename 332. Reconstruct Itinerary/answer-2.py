def findItinerary(self, tickets):
    from collections import defaultdict

    tickets_dict = defaultdict(list)

    for ticket in tickets:
        from_air, to_air = ticket[0], ticket[1]
        tickets_dict[from_air].append(to_air)

    start = 'JFK'
    res = []
    print(tickets_dict)

    def backtracking(start):
        print('---')
        print(start)
        while tickets_dict[start]:
            next = tickets_dict[start].pop()
            backtracking(next)
        res.append(start)

    backtracking('JFK')
    return res[::-1]


# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(findItinerary(None, tickets))
