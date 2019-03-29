class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapdict = {')':'(', ']':'[','}':'{'}
        for c in s:
            if c not in mapdict:
                stack.append(c)
            elif not stack or mapdict[c] != stack.pop():
                return False
        return not stack