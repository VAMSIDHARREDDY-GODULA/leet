class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i,j in enumerate(nums):
            s=0
            while(j>0):
                s+=j%10
                j//=10
            if i==s:
                return i
        return -1