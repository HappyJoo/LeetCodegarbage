class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for i in ops:
            if i == 'C':
                res.pop()
            elif i == 'D':
                res.append(res[-1] * 2)
            elif i == '+':
                res.append(res[-1] + res[-2])
            else:
                """
                In the begining, I thought the should be more numbers than 'CD+',
                So i use i.isdigit() to check if it's number.
                Then when it comes to negative numbers, it's a False
                So we shoulbe check it in the end, 
                because other than "CD+" only numbers left.
                 """
                res.append(int(i))
        return sum(res)


        """ 
        Below is the original tedious and WRONG way. It's not working
        So, use the way above please.
        """
        # res, num = 0, 0
        # stack = []
        # for e in ops:
        #     if e == "+":
        #         num = int(stack[0]) + int(stack[1])
        #         res += num
        #         stack = [num] + stack
        #     elif e == 'D':
        #         num = 2 * int(stack[0])
        #         res += num
        #         stack = [num] + stack
        #     elif e == 'C':
        #         num = int(stack[0])
        #         res -= num
        #         stack.remove(str(num)) 
        #     else:
        #         res += int(e)
        #         stack = [e] + stack
        #     while len(stack) > 3:
        #         stack.pop()
        # return res