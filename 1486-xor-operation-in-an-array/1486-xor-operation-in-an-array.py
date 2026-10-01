class Solution(object):
    def xorOperation(self, n, start):
        r = 0
        for i in range(start,start+(n*2),2):
            r ^= i
        return r