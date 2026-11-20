class Solution(object):
    def smallestEqual(self, nums):
        for i, j in enumerate(nums):
            if j==i%10: return i
        return -1