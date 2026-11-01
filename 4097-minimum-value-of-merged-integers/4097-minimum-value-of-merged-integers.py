class Solution(object):
    def minMergedInteger(self, nums):
        a = int(str(nums[0])+str(nums[1]))
        for i in range(2,len(nums),2):
            print(a)
            x = int(str(nums[i])+str(nums[i+1]))
            a = min(a,x)
        return a