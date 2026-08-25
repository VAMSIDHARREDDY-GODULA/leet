class Solution(object):
    def missingNumber(self, nums):
        x = 0
        for i,j in zip(range(1,len(nums)+1),nums):
            x ^= (i^j)
        return x