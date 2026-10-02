class Solution(object):
    def numWaterBottles(self, n, e):
        x = n
        while x>=e:
            n += x//e
            x = x%e+x//e
        return n