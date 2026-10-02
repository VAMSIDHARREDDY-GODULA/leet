class Solution(object):
    def numIdenticalPairs(self, nums):
        if len(nums)==len(set(nums)): return 0
        a = 0
        for i in set(nums):
            x = nums.count(i)
            if x>1: a += (x*(x-1)//2)
        return a