from collections import defaultdict


def threeSum(self, nums):
    res = []
    nums.sort()

    for i in range(0, len(nums) - 2):
        if nums[i] > 0 or i > 0 and nums[i] == nums[i - 1]:
            continue
        num_one = nums[i]
        l = i + 1
        r = len(nums) - 1
        print(i, l, r)
        while l < r:
            num_two = nums[l]
            num_three = nums[r]
            c_sum = num_one + num_two + num_three
            if c_sum > 0:
                r -= 1
            elif c_sum < 0:
                l += 1
            else:
                c_res = [num_one, num_two, num_three]
                res.append(c_res)
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res


nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0]
print(threeSum(None, nums))
