def longestOnes(self, A, K: int) -> int:
    l = 0
    r = 0
    nums = 0
    max_len = 0
    while r < len(A):
        if A[r] == 0:
            nums += 1
        while nums > K:
            if A[l] == 0:
                nums -= 1
            l += 1

        r += 1
        max_len = max(max_len, r - l)


    return max_len


A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
K = 3

A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2

print(longestOnes(None, A, K))
