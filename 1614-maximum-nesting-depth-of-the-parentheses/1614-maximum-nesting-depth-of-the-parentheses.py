class Solution(object):
    def maxDepth(self, s):
        a = m = 0
        for i in s:
            if i=='(':
                a += 1
                if m<a: m=a
            elif i==')': a -= 1
        return m