class Solution(object):
    def repeatedNTimes(self, nums):
        b = []
        i = 0
        while i<len(nums):
            if nums[i] in b: return nums[i]
            b.append(nums[i])
            i += 1