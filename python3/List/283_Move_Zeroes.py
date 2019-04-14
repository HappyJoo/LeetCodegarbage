"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Example:  Input: [0,1,0,3,12]  Output: [1,3,12,0,0]
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1
        for i in nums:
            if i == 0:
                nums.remove(i) # Remove the first one that matches
                nums.append(0) # Append in the end
                
        # Solution 2
        k, m = 0, 0
        while k < len(nums) - m:
            if nums[k] == 0:
                del nums[k]
                nums.append(0)
                m += 1
                continue
            k += 1
        
        # Solution 3
        m = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[m] = 0, nums[i]
                m += 1
