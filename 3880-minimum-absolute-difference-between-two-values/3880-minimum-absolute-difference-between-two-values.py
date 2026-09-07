class Solution(object):
    def minAbsoluteDifference(self, nums):
        if 2 not in nums or 1 not in nums : return -1
        c = float('inf')
        i = 0
        while i<len(nums):
            j, y = i+1, []
            if nums[i]:
                z = nums[i]
                while j<len(nums):
                    if nums[j]:
                        if z!=nums[j]:
                            break
                        y.append(j)
                    j += 1
                if c>j-i and j<len(nums): c = j-i
            i = y[0] if y else j
        return c