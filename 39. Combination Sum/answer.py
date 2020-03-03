def combinationSum(candidates: list, target: int) -> list:
    results = []

    def recursive(current_list, nums, index, target):
        if target == 0:
            results.append(current_list)
            return

        for i in range(index, len(nums)):
            if target < 0:
                break
            recursive(current_list + [nums[i]], nums, i, target - nums[i])

    recursive([], candidates, 0, target)
    print(results)
    return results
    recursive([], candidates, 0, target)

    print(results)
    return results


combinationSum([2, 3, 5], 8)
