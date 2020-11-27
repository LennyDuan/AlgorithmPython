import heapq


def count(ropes):
    if not ropes:
        return 0
    if len(ropes) == 1:
        return ropes[0]
    heapq.heapify(ropes)
    result = 0

    while len(ropes) > 1:
        h1 = heapq.heappop(ropes)
        h2 = heapq.heappop(ropes)
        sum = h1 + h2
        result += sum
        heapq.heappush(ropes, sum)

    return result


# ropes = [20, 4, 8, 2]
# ropes = [8, 4, 6, 12]
ropes = [1, 2, 5, 10, 35, 89]

print(count(ropes))
