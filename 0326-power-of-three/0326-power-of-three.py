class Solution(object):
    def isPowerOfThree(self, n):
        while n>2:
            if n%3:
                return 2==3
            n //= 3
        return n==1