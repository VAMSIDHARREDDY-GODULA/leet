class Solution(object):
    def canAliceWin(self, n):
        x = 10
        while x:
            if n>=x:
                n -= x
                x -= 1
                if n<x: return 1==1
                n -= x
                x -= 1
            else: return 1==2
        return 1==2