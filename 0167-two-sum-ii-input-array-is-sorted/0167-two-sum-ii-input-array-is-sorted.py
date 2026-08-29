class Solution(object):
    def twoSum(self, n, t):
        i = 0
        j = len(n)-1
        while i<j:
            x = n[i]+n[j]-t
            if not x:
                return [i+1,j+1]
            elif x>0:
                j -= 1
            else:
                i += 1
        return [-1,-1]