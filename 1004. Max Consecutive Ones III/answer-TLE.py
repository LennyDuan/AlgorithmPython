def longestOnes(self, A, K: int) -> int:
    res = 0
    queue = []
    for a in A:
        queue.append(a)
        if a == 0:
            while queue.count(0) > K:
                queue.pop(0)

        res = max(res, len(queue))
    print(res)
    return res


A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
K = 3

A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2

longestOnes(None, A, K)
