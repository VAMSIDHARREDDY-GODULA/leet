class Solution(object):
    def maxSubArray(self, nums):
        s = m = nums[0]
        for i in nums[1:]:
            s = i if s<0 else s+i
            m = m if m>s else s
        return m