from collections import Counter
class Solution:
    # Solution 1
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
    # Time: O(n) Space: O(n)
"""
nums = [3,2,3]
Counter(nums).most_common(1)       ==> [[3, 2]]
Counter(nums).most_common(1)[0]    ==> [3,2]
Counter(nums).most_common(1)[0][0] ==> 3

Getting it?
The most_common function return a list with the n most common numbers
In this case, return 1 most common number in a list.
So use [0][0] to get the number in that list.
Always remember to read the description.
It tells us that we may assume that the array is non-empty and the majority element always exist in the array.
"""

    # Solution 2
    # This one is cumbersome. 
    # If the list is toooooo long, it might takes quite a few moments...
    # Try setting this be nums and you will know. https://leetcode-cn.com/submissions/detail/15520270/testcase/
    majority_count = len(nums) // 2
    for num in nums:
        count = sum(1 for elem in nums if elem == num)
        if count > majority_count:
            return num
    # Time: O(n*n) Space(1)

    # Solution 3
    # Because the majority element is always more than n/2
    # So we r pretty sure the element is the n//2 th element if the list is sorted.
    # Some kind of math trick i guess?
    nums.sort()
    return nums[(len(nums)-1) // 2]
    # Time: O(nlgn) Space: O(1) or O(n)

    



