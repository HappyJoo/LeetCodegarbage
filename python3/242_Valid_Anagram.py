class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # solution 1 count every character
        if len(s) != len(t): return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
        
        # Solution 2 sort two list and check if they equal
        return sorted(s) == sorted(t)  # O(NlogN)

        # Solution 3 map. use dictionary to check whether they have same amount of characters
        dict1, dict2 = [0] * 26, [0] * 26
        for i in s:
            dict1[ord(i)-ord('a')] += 1
        for i in t:
            dict2[ord(i)-ord('a')] += 1
        return dict1 == dict2
        
        # Solution 4 hashmap
        dict1, dict2 = {}, {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        for i in t:
            dict2[i] = dict2.get(i, 0) + 1
        return dict1 == dict2