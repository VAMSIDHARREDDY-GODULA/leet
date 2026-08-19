class Solution(object):
    def isPowerOfTwo(self, n):
        while n>1:
            if n%2:
                return 1==2
            n //= 2
        return n==1