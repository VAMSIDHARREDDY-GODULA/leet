class Solution(object):
    def sortColors(self, nums):
        j, k = 0, len(nums)-1
        x = y = 0
        for i in nums:
            if not i:
                nums[j] = i
                j += 1
            elif i==1: x += 1
            else: y += 1
        while x or y:
            if x:
                nums[j] = 1
                x -= 1
                j += 1
            if y:
                nums[k] = 2
                y -= 1
                k -= 1
        return nums