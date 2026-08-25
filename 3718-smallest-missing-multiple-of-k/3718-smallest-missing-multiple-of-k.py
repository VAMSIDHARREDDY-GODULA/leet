class Solution(object):
    def missingMultiple(self, nums, k):
        for i in range(k, max(nums)+k+1, k):
            if i not in nums:
                return i