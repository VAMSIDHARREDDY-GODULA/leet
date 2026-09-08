class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        j = 0
        while k:
            i = nums[j]
            if not i: return sum(nums)
            if i>0:
                y = k%2
                if y and i<nums[j-1]: nums[j] = -i
                elif y: nums[j-1] = -nums[j-1]
                return sum(nums)
            nums[j] = -i
            k -= 1
            j = j+1 if j<len(nums)-1 else 0
        return sum(nums)