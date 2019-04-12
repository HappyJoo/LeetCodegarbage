
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1
        if len(nums) == 0 or len(nums) == 1:
            return False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


        # Solution 2
        return len(set(nums)) != len(nums)
        # if len(set(nums))<len(nums):
        #     return True
        # return False


        # Solution 3
        d={}
        for i in nums:
            if i in d:
                return True
            d[i] = ''
        return False