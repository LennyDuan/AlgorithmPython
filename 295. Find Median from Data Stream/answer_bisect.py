import bisect


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort_right(self.nums, num)

    def findMedian(self) -> float:
        length = len(self.nums)
        mid = length // 2
        return self.nums[mid] if length % 2 == 1 else (self.nums[mid] + self.nums[mid - 1]) / 2
