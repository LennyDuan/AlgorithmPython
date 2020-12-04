def maximum_operating(maxTravelDist, forwardRouteList, returnRouteList):
    res = []
    len_f = len(forwardRouteList)
    len_r = len(returnRouteList)
    index_f = 0
    index_r = len_r - 1
    max_paired = 0
    while index_f < len_f and index_r >= 0:
        print(index_f, index_r)
        if forwardRouteList[index_f][1] + returnRouteList[index_r][1] > maxTravelDist:
            index_r -= 1
            continue
        else:
            current_paired = forwardRouteList[index_f][1] + returnRouteList[index_r][1]
            print(current_paired)
            if current_paired > max_paired:
                res = [[forwardRouteList[index_f][0], returnRouteList[index_r][0]]]

            if current_paired == max_paired or not res:
                res.append([forwardRouteList[index_f][0], returnRouteList[index_r][0]])

            max_paired = max(max_paired, current_paired)
            index_f += 1

    return res


maxTravelDist = 10000
forwardRouteList = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
returnRouteList = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
res = [[2, 4], [3, 2]]

maxTravelDist = 7000
forwardRouteList = [[1, 2000], [2,4000], [3, 6000]]
returnRouteList = [[1, 2000]]
res = [[2, 1]]

print(maximum_operating(maxTravelDist, forwardRouteList, returnRouteList))
