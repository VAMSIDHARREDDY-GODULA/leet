class Solution(object):
    def hasAlternatingBits(self, n):
        x = bin(n)[2:]
        return '11' not in x and '00' not in x