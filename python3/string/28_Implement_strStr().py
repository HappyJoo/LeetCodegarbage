class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Solution 1 using slice
        for i in range(len(haystack) - len(needle) + 1):
            if needle == haystack[i:i + len(needle)]:
                return i
        return -1
        

        # Solution 2 using string.find()
        return haystack.find(needle)