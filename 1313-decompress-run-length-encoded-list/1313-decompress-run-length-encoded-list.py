class Solution(object):
    def decompressRLElist(self, nums):
        i = 0
        b = []
        while i<len(nums):
            b.extend([nums[i+1]]*nums[i])
            i += 2
        return b