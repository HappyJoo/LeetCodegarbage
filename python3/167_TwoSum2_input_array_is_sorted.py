#-*- coding:utf-8 -*-
class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
                #remember to take a break otherwise it'll loop
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

#Above is enough for LeetCode
#You can delete the octothorpe if you like to run it in linux.
#a = Solution()
#print(a.twoSum([2, 7, 11, 15], 9))
