def maxNonOverlapping(self, nums, target: int) -> int:
    seen = set([0])
    ans = curr = 0

    for i, num in enumerate(nums):
        curr += num
        prev = curr - target

        if prev in seen:
            ans += 1
            seen = set([0])
        seen.add(curr)

    return ans


nums = [-1, 3, 5, 1, 4, 2, -9]
target = 6
print(maxNonOverlapping(None, nums, target))
