"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""

""" 
Every element in the list is 0-9, which is non-negative integer.
So the list represent an interger, and we are here to make it plus one.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # a=''
        # for i in digits:
        #     a += str(i)
        # a = str(int(a)+1)
        # res = []
        # for i in a:
        #     res.append(int(i))
        # return res
        a = [str(x) for x in digits]
        d = "".join(a)
        d = int(d) + 1
        return [int(x) for x in str(d)]
