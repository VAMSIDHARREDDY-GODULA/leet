class Solution(object):
    def isPowerOfFour(self, n):
        while n>3:
            if n%4:
                return 3==2
            n //= 4
        return n==1