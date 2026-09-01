class Solution(object):
    def productExceptSelf(self, nums):
        if nums.count(0)>1:
            return [0]*len(nums)
        b, c = [], 1
        for i in nums:
            if i:
                c *= i
        if 0 not in nums:
            for j in nums:
                b.append(c//j)
        else :
            for i in nums:
                if not i: b.append(c)
                else: b.append(0)
        return b
        