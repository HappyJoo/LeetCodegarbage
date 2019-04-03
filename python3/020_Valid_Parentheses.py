# Solution 1
# Time: O(n), Space: O(n)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] # create a stack
        mapdict = {')':'(', ']':'[','}':'{'} # create a maplist
        for c in s:
            if c not in mapdict: # if c == '{', '[', '(' append it to stack
                stack.append(c)
            elif not stack or mapdict[c] != stack.pop(): # if not, check it
                return False
        return not stack

# Solution 2 
# Solution 1 is better in time complexity
# If there is any {} [] () in s then change it to ''.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '{}' in s or '[]' in s or '()' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''