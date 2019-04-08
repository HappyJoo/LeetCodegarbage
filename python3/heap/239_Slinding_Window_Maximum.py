class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        win_index, res = [], [] # win_index is an index, and window is the sliding window.
        for i, x in enumerate(nums):
            """ 
            i - k is the index of the number before the window whose size should be k.
            pop out the first number of win_index if the size of sliding window is bigger than k.
            """
            if i >= k and win_index[0] <= i - k: 
                win_index.pop(0)

            # before appending x, if the number in the sliding window is <= x, pop it out.
            # make sure that the first number of the sliding window is always the biggest.
            while win_index and nums[win_index[-1]] <= x: 
                win_index.pop()
            win_index.append(i) # adding index i
            if i >= k - 1:
                res.append(nums[win_index[0]]) # win_index(0) in nums should always be the biggest number in the window.
        return res

# nums = [1,2,3,4,5,6,7,8,9]
# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# a = Solution()
# print(a.maxSlidingWindow(nums, k))
