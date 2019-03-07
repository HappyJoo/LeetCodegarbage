#Please run it in LeetCode.com

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #nums = [1,1,1,2,2,3], k = 2
        n = len(nums) #n = 6
        cntDict = collections.defaultdict(int)
        for i in nums:
            cntDict[i] += 1 #cntDict = {1:3, 2:2, 3:1}
        freqList = [[] for i in range(n + 1)] # freqList = [[], [], [], [], [], [], []]
        for p in cntDict:
            freqList[cntDict[p]] += p, #freqList = [[], [3], [2], [1], [], [], []]
        ans = []
        for p in range(n, 0, -1):
            ans += freqList[p] #ans = [1, 2, 3]
        return ans[:k]
