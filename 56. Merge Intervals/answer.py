## Possible but too much if else

def merge(self, intervals):
    out = list()
    for i in sorted(intervals, key=lambda i: i[0]):

        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out.append(i)
    return out


intervals = [[2, 6], [1, 3], [8, 10], [15, 18]]
# [[1, 4], [0, 5]]
# [[1,4],[0,2]]
# [[1,4],[0,1]]
# [[1,4],[4,5]]
# [[1,4],[1,5]]
# [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[2, 6], [1, 3], [8, 10], [15, 18]]

# [[1,6],[8,10],[15,18]]
print(merge(None, intervals))
