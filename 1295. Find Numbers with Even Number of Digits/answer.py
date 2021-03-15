def findNumbers(self, nums) -> int:
    res = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            res += 1
    return res


nums = [12, 345, 2, 6, 7896]
print(findNumbers(None, nums))
