class Solution(object):
    def singleNumber(self, nums):
        x = y = 0
        for i in nums:
            x ^= i &(~y)
            y ^= i &(~x)
        return x