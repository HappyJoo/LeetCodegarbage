"""
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # the shortest code and don't understand yet. Using DP
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        return max(nums)


        # using the divide and conquer approach
        # but it's too slow and i don't know why yet.
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[0:n // 2])
            max_right = self.maxSubArray(nums[n // 2:n])

        # left
        max_l = nums[n // 2 - 1]
        tmp = 0
        for i in range(n // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        # right
        max_r = nums[n // 2]
        tmp = 0
        for i in range(n // 2, n):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        return max(max_left, max_right, max_l + max_r)