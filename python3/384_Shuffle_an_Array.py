import random
class Solution:
    # solution 1 
    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return sorted(self.nums, key=lambda x: random.random())


    # solution 2 a little bit tedious
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.init = list(nums)
        self.nums = nums
        self.length = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = list(self.init)
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in reversed(range(self.length)):
            index = random.randint(0, i)
            self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
        return self.nums