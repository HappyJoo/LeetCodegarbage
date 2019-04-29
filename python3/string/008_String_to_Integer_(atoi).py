class Solution:
    def myAtoi(self, str: str) -> int:
        # Solution 1 without using re
        str = str.strip()  # Remove all the space in the front and back
        if not str:  # Return 0 if str is empty
            return 0
        num, pos = '', 1  # *num shouble be empty string here. pos = 1 means positive.
        if str[0] == '+':  
            str = str[1:]
        elif str[0] == '-':
            str = str[1:]
            pos = -1
        
        for c in str:
            if '0' <= c <= '9':
                num += c
            else:
                break
        
        if not num:  # *Consider when num is empty
            return 0
        num = int(num) * pos  # *Num should multiply pos
        if num < -2147483648:
            return -2147483648
        elif num >= 2147483648:  # *when num is too big
            return 2147483647
        return num

# Solution 2 using re
        import re
        """ 
        *: zero or more
        ?: zero or one
        +: one or more
        'r' means 'raw string'
        """
        pattern = r"[\s]*[+-]?[\d]+"
        match = re.match(pattern, str)
        if match:
            res = int(match.group(0))
            if res > 2 ** 31 - 1:  # Or 2147483648
                return 2 ** 31 -1  
            if res < - 2 ** 31:
                return - 2 ** 31
        else:
            return 0
        return res 
        