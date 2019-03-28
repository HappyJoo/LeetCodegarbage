# The length of nums1 is not changable. So no nums1.pop()

# Solution 1
# If there is a 0 in nums1, because nums1 will always have enough space
# replace it with nums2's element. Then sort nums1, won't change its id.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Solution 1
        index_nums2 = 0
        for i in range(len(nums1)):
            if index_nums2 == len(nums2): # index cannot bigger than len(nums2)
                break
            elif nums1[i] == 0:
                nums1[i] = nums2[index_nums2]
                index_nums2 += 1
        nums1.sort()


        """ Solution 2
         Imaging two list, nums1 is the one with a lot of zeroes.
         Nums2 is the second one that you should put into nums1.
         And every time I say last one means the one behind zeroes.
        """
        # The last number exclude zeroes.
        # Which is also the biggest one.
        index_nums1 = m - 1 
        index_nums2 = n - 1 
        index_input = m + n - 1 # The last index of nums1
        while index_nums1 >= 0 and index_nums2 >= 0:
            if nums1[index_nums1] > nums2[index_nums2]:
                """ Imaging u put the last non-zeroes of nums1 into its end"""
                nums1[index_input] = nums1[index_nums1]
                index_input -= 1 # You can actually combine this two
                index_nums1 -= 1 # lines into one line
            else: # The last one of nums2 is bigger than nums1's
                """ Imaging to put the last one of nums2 into nums1's end"""
                nums1[index_input] = nums2[index_nums2]
                index_input -= 1
                index_nums2 -= 1

        """ 
        Remember, m is not len(nums1), but len(nums1) without all zeroes
        So if nums1 run out, nums2 still has some numsbers which are smaller than the smallest number in nums1.
        As a result, just put them into the index they should be.
        """
        while index_nums2 >= 0:
            nums1[index_input] = nums2[index_nums2]
            index_input -= 1
            index_nums2 -= 1

        # The same as Solution 2 but much pretty.
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1 
            else: 
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1


        # Solution3 
        # I think it's maybe prettier than Solution1, but I just don't understand it yet.
        for i in range(n):
            t = m
            for j in range(m-1, -1, -1):
                if nums2[i] < nums1[j]:
                    nums1[j+1] = nums1[j]
                    t = j
                else:
                    break
            m += 1
            nums1[t] = nums2[i]