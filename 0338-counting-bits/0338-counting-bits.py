class Solution(object):
    def countBits(self, n):
        b = [0]*(n+1)
        for i in range(1,n+1):
            b[i] = b[i>>1]+(i&1)
        return b