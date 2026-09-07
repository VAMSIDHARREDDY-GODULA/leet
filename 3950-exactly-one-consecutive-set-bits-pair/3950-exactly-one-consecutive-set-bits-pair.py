class Solution(object):
    def consecutiveSetBits(self, n):
        x = bin(n)[2:]
        c1, c2 = x.count('11'), '111' not in x
        return c1==1 and c2