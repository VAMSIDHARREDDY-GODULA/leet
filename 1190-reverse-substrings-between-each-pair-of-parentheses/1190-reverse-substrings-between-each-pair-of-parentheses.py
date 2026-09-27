class Solution(object):
    def reverseParentheses(self, s):
        x = []
        for i in s:
            if i!=')':
                x.append(i)
            else:
                y = []
                while x[-1]!='(':
                    y.append(x.pop()[::-1])
                x.pop()
                x.append(''.join(y))
        return ''.join(x)