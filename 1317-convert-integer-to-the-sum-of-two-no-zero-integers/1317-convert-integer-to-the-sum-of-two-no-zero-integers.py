class Solution(object):
    def getNoZeroIntegers(self, n):
        b = [1,n-1]
        while '0' in str(b[0])+str(b[1]):
            b = [b[0]+1, b[1]-1]
        return b