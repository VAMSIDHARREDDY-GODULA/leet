class Solution(object):
    def checkDivisibility(self, n):
        p, s = 1, 0
        x = n
        while x:
            z = x%10
            p *= z
            s += z
            x //= 10
        return n%(p+s)==0