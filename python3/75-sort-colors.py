from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = Counter(nums) #Counter({2: 2, 0: 2, 1: 2})
        for  i in range(len(nums)): #range(0, 6)
            ```
            So count has three key:value.
            The 0 in the count[0] means the first key,
            so 1 should be the second key and 2 the third
            Therefore the count[0] should be 2, the value of the first key 2.
            Since the problem tell us that there is only 0, 1, 2
            we can just set nums to 0, 1, 2
            ```
            if i < count[0]:
            # i start from 0, so the first instruction is 'if 0 < 2:'
                nums[i] = 0   #nums[0] and nums[1] is 0
            elif i < count[0] + count[1]: # count[0] + count[1] is 4
                nums[i] = 1   #nums[2] and nums[3] is 1
            else:
                nums[i] =2    #nums[4] and nums[5] is 0

