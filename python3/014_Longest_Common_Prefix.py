# Solution 1 compare every character vertically in **two row**
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = [len(set(c)) == 1 for c in zip(*str)] + [0]
        return str[0][:r.index(0)] if strs else ''


# Solution 2 compare every character vertically
class Solution:
    def longestCommonPrefix(self, strs):
        res = ''
        for i in zip(*str):
            tmp_set = set(i)
            if len(tmp_set) == 1:
                res += i[0]
            else:
                break
        return res

# Solution 3 compare one by one
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res

# Solution 4 compare the first and last one after sorting.
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        s.sort()
        a = s[0]
        b = s[-1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res