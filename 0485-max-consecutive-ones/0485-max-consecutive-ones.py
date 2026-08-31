class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if 0 not in nums:
            return len(nums)
        c = 0
        b = 0
        for i in nums:
            if i==1:
                b += 1
            else :
                if c<b:
                    c = b
                b = 0
        if c<b:
            c = b
        return c