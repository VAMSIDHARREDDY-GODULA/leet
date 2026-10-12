class Solution(object):
    def sumOfSquares(self, nums):
        s, n = 0, len(nums)
        for i, j in enumerate(nums):
            if not n%(i+1):  s += j*j
        return s