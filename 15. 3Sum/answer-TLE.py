from collections import defaultdict


def threeSum(self, nums):
    res = set()
    two_sum_dict = defaultdict(list)

    for i_one, num_one in enumerate(nums):
        for i_two in range(i_one + 1, len(nums)):
            two_sum = num_one + nums[i_two]
            two_sum_dict[two_sum].append([i_one, i_two])

    print(two_sum_dict)

    for i, num in enumerate(nums):
        sum_to_zero_key = -num
        two_sum_arr = two_sum_dict.get(sum_to_zero_key)
        if two_sum_arr and len(two_sum_arr) > 0:
            for arr in two_sum_arr:
                if arr and i not in arr:
                    cur_res_i = arr + [i]
                    cur_res_nums = tuple(sorted([nums[i] for i in cur_res_i]))
                    res.add(cur_res_nums)

    return list(res)


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(None, nums))
