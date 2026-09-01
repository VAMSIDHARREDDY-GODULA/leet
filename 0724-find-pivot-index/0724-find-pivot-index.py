class Solution(object):
    def pivotIndex(self, nums):
        t = sum(nums)
        l, r = 0, t
        for j,i in enumerate(nums):
            r -= i
            if l==r:
                return j
            l += i
        return -1