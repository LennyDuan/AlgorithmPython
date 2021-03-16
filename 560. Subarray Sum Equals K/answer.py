def subarraySum(self, nums: [int], k: int) -> int:
    res = s = 0
    D = {0: 1}
    for num in nums:
        print(D)
        s += num
        key = s - k
        if key in D:
            res += D[key]
        D[s] = (D.get(s) or 0) + 1
        print(D)
        print('---')

    return res


nums = [1, 2, 3]
k = 3
print(subarraySum(None, nums, k))
