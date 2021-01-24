def wiggleSort(self, nums) -> None:
    nums.sort()
    half = len(nums[::2])
    # print(half)
    # print(nums)
    # print('---')
    # print(nums[0:half+1][::-1])
    # print(nums[half+1:][::-1])
    # print('---')
    # print(nums[half::-1])
    # print(nums[:half:-1])

    nums[::2], nums[1::2] = nums[0:half][::-1], nums[half:][::-1]
    return nums


nums = [1, 5, 1, 1, 6, 4]
print(wiggleSort(None, nums))
