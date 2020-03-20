from random import random


class Solution:

    def __init__(self, nums: list()):
        self.origin = nums,

    def reset(self) -> list():
        """
        Resets the array to its original configuration and return it.
        """
        print(self.origin)
        return self.origin

    def shuffle(self) -> list():
        """
        Returns a random shuffling of the array.
        """
        shuffled = random.shuffle(self.nums)
        print(shuffled)
        return shuffled

# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3])
param_1 = obj.reset()
param_2 = obj.shuffle()