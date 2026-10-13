class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2: return 0
        a = 0
        n = sorted(set(nums))
        for i in range(1,len(n)):
            x = n[i]-n[i-1]
            if x>a: a=x
        return a