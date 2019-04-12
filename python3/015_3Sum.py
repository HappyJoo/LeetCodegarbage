class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Solution 1 Time: O(N2) Space: O(N)
        # if len(nums) < 3: # without this it works too
        #     return []
        nums.sort()
        res = set()
        for index, num in enumerate(nums[:-2]):
            if index >= 1 and num == nums[index-1]:
                continue
            d = {}
            for x in nums[index+1:]:
                if x not in d:
                    d[-x-num] = 1
                else:
                    res.add((num, -num-x, x))
        return map(list, res)


        # Solution 2 Time: O(N2) Space: 0
        nums.sort()
        res = set()
        