class Solution(object):
    def removeOuterParentheses(self, s):
        a = 0
        x = []
        for i in s:
            if i=='(':
                if a:
                    x.append(i)
                a += 1
            else:
                a -= 1
                if a:
                    x.append(i)
        return ''.join(x)
