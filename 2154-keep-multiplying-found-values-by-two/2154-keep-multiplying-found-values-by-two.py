class Solution(object):
    def findFinalValue(self, nums, o):
        if o not in nums: return o
        while o in nums:
            o += o
        return o