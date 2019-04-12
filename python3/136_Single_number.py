class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Remember there is only one single number in list.
        # All of the others appear twice.
        # First solution:
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        '''
        # The thing up there (60ms) is two time faster than below (112ms),
        # don't know why yet..
        for i in nums:
            result ^= i
        '''
        return result
''' 
    So the point is, every element appears twice except the one we're finding. 
    Note here, TWICE!! Only ONE single number!
    Anything ^ anything twice will get the 'Anything'.
    Like, if a ^ b = c, c ^ b will get a again~
    That is a ^ b ^ b == a
    a ^ b ^ c ^ b ^ d ^ d ^ c == a

    So we use the element in the list and ^ every element in it.
    Except the single one, we will ^ any different element exactly twice.
    And then only the single one is left~
'''

        # Second solution(iterator):
        res = {} # Get an empty dict
        for i in nums: # Iterate the list
            if i in res:
                res[i] = 1 # Every two number will be 1
            else:
                res[i] = 0 # The one single number will be 0
        for key in res.keys():
            if res[key] == 0:
                return key # According to the question, there will be one only answer.


        nums.sort()
        for i in range(0,len(nums)-2,2):
            x = i+1
            if nums[i] != nums[x]:
                return nums[i]
        return nums[-1]

