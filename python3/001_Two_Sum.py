class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1 violent
        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
        # Solution 2 
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        
        # Solution 3
        hashmap = {}
        for index in range(len(nums)):
            if nums[index] in hashmap:
                return [hashmap[nums[index]], index]
            hashmap[target - nums[index]] = index