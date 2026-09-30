class Solution(object):
    def kLengthApart(self, nums, k):
        if nums.count(1)<2: return 1==1
        b = nums.index(1)
        for i in range(b+1,len(nums)):
            if nums[i]:
                if i-b<=k: return 1==2
                else: b=i
        return 1==1