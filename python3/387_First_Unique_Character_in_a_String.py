class Solution:
    def firstUniqChar(self, s: str) -> int:
        # s.find(l) find the first from left, s.rfind from the right
        letters = 'qwertyuiopasdfghjklzxcvbnm'
        index = [s.index(l) for l in letters if s.find(l) != -1 and s.find(l) == s.rfind(l)]
        return min(index) if index else -1
