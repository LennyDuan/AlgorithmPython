def findItinerary(self, tickets):
    from collections import defaultdict

    tickets_dict = defaultdict(list)

    for ticket in tickets:
        from_air, to_air = ticket[0], ticket[1]
        tickets_dict[from_air].append(to_air)

    start = 'JFK'
    res = []
    print(tickets_dict)

    def find_next(start, res):
        print('---')
        print(start)
        res.append(start)
        to_airs = tickets_dict[start]
        if to_airs:
            lexical_air = list(sorted(to_airs))
            print(lexical_air)
            next_start = lexical_air.pop(0)
            tickets_dict[start] = lexical_air
            find_next(next_start, res)

    find_next(start, res)
    return res


# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(findItinerary(None, tickets))
