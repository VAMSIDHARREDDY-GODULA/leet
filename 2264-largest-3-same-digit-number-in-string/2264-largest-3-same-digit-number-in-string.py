class Solution(object):
    def largestGoodInteger(self, num):
        for i in range(9,-1,-1):
            x = str(i)*3
            if x in num: return x
        return ''