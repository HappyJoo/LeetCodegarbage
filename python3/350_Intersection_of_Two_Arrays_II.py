""" Given two arrays, write a function to compute their intersection."""
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        x1, x2 = 0, 0
        nums1.sort()
        nums2.sort()
        while x1 < len(nums1) and x2 < len(nums2):
            if nums1[x1] == nums2[x2]:
                res.append(nums1[x1])
                x1 += 1
                x2 += 1
            elif nums1[x1] > nums2[x2]:
                x2 += 1
            else:
                x1 += 1
        return res

    
        # Solution 2
        import collections
        res = []
        x = collections.Counter(nums2) # or nums1, whatever.
        for n in nums1:
            if n in x and x[n] > 0: # it's True even if it's 0
                res.append(n)
                x[n] -= 1
        return res
