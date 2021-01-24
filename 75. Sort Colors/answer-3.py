def sortColors(self, nums):
    beg, mid, end = 0, 0, len(nums) - 1

    while mid <= end:
        print(nums)
        if nums[mid] == 0:

            nums[beg], nums[mid] = nums[mid], nums[beg]
            mid += 1
            beg += 1

        elif nums[mid] == 2:
            nums[mid], nums[end] = nums[end], nums[mid]
            end -= 1

        elif nums[mid] == 1:
            mid += 1

    print(nums)


nums = [2, 0, 2, 1, 1, 0]
sortColors(None, nums)
