def searchRange(self, nums, target: int):
    start = -1
    end = -1
    res = [start, end]

    if target not in nums:
        return res
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if nums[mid] == target:
            start = end = mid
            start_tmp = start
            while start >= low and nums[start] == target:
                start_tmp = start
                start -= 1
            res[0] = start_tmp

            end_tmp = end
            while end <= high and nums[end] == target:
                end_tmp = end
                end += 1
            res[1] = end_tmp
            break

        if nums[mid] >= target:
            high = mid
        else:
            low = mid + 1

    return res


nums = [5, 7, 7, 8, 8, 10]
target = 8

nums = [1, 4]
target = 4
print(searchRange(None, nums, target))
