class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, n in enumerate(nums):
            if n in d and i-d[n]<=k:
                return 1==1
            d[n] = i
        return 1==3