def subsets(nums: list()) -> list():
    results = []
    n = len(nums)

    def backtracking(index=0, curr=[]):
        if len(curr) == k:
            results.append(curr[:])

        for i in range(index, n):
            curr.append(nums[i])
            backtracking(i + 1, curr)
            curr.pop()

    for k in range(n + 1):
        backtracking()

    print(results)
    return results


subsets([1, 2, 3])
