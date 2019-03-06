#-*- coding:utf-8 -*-
class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]
