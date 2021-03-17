def decompressRLElist(self, nums: [int]) -> [int]:
    res = []
    print(nums)
    count = nums[0::2]
    num = nums[1::2]
    print(count, num)
    for i in range(len(nums)/2):
        res.extend(nums[0::2][i] * [nums[1::2][i]])
    return res


    # res = []
    # for i in range(len(nums)//2):
    #     res.extend(nums[0::2][i] * [nums[1::2][i]])
    # return res


nums = [1, 2, 3, 4]
print(decompressRLElist(None, nums))
