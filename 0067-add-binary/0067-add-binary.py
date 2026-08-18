class Solution(object):
    def addBinary(self, a, b):
        x, y = int(a,2), int(b,2)
        return bin(x+y)[2:]