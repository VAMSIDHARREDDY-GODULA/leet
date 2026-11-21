class Solution(object):
    def checkString(self, s):
        if 'a' not in s or 'b' not in s: return 1==1
        x, y = (len(s)-s[::-1].index('a')-1), s.index('b')
        return x<y