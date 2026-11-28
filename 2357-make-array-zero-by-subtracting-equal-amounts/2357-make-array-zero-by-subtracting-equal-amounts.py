class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        n = sorted(nums)
        a = x = 0
        for i in n:
            i -= x
            x += i
            if i: a+=1
        return a