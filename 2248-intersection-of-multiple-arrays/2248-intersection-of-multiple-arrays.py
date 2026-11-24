class Solution(object):
    def intersection(self, nums):
        x = set(nums[-1])
        for i in nums[:-1]:
            x = x.intersection(set(i))
        return sorted(x)