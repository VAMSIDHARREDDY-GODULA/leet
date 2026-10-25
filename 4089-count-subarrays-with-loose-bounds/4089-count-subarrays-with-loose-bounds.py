class Solution(object):
    def countSubarrays(self, nums, mink, maxk):
        b = x = 0
        for i in nums:
            if mink<=i<=maxk:
                b += 1+x
                x += 1
            else: x = 0
        return b