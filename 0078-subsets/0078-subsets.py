class Solution(object):
    def subsets(self, nums):
        b = []
        for i in range(len(nums)+1):
            for j in itertools.combinations(nums,i):
                b.append(j)
        return b