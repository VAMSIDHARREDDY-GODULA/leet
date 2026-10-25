class Solution(object):
    def peakValleyDifference(self, nums):
        x, y = 0, 0
        i = 1
        while i<len(nums)-1:
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                x += nums[i]
            elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                y += nums[i]
            i += 1
        return x-y