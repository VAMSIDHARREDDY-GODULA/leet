class Solution(object):
    def subsets(self, nums):
        b = []
        for i in range(len(nums)+1):
            for i in itertools.combinations(nums,i):
                b.append(list(i))
        return b