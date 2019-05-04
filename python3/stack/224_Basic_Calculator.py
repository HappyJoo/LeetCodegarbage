class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():  # it's c.isdigit(), not c.isdigit! there is paranthesis!!
                num = 10 * num + int(c)
            elif c == '+' or c == '-':  # 'if c in "+-"' is less character
                """
                1.why should res add up in here?
                'num' can only save one number within parenthesis.
                So every time there is a '+' or '-',
                'num' should calculate with 'res'.
                """
                res = res + sign * num  # update res with new num every time
                num = 0  # reset num after adding it with res
                sign = 1 if c == '+' else -1  # update the next sign
            elif c == '(':
                """
                push res and sign into stack to calculate everything within parenthesis first
                we calculate everything within parenthesis first because maybe there is no other way
                """
                stack.append(res)  # push res into stack
                stack.append(sign)  # push sign into stack
                res = 0  # reset res to start new calculation within parenthesis
                sign = 1  # reset sign
            elif c == ')':
                res = res + sign * num  # calculator with the last num before ')' 
                                        # and before calculate with everything before this parenthesis
                num = 0  # reset
                res *= stack.pop()  # there should always be a sign before left parenthesis
                res += stack.pop()  # then add up the res before
        return res + sign * num  # there is no need to add one more line before return