class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2: return 0
        a = 0
        nums.sort()
        for i in range(1,len(nums)):
            x = nums[i]-nums[i-1]
            if x>a: a=x
        return a