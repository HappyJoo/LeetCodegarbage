
# Solution 1 with 1800ms... at leetcode
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Solution 2. Which is faster than Solution 1 with only 140ms
# You can learn all about heap at https://docs.python.org/3.7/library/heapq.html#heapq.heapify
import heapq
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(nums) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
       
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif self.pool[0] < val:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]