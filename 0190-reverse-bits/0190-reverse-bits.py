class Solution(object):
    def reverseBits(self, n):
        s = bin(n)[2:][::-1]
        c = len(s)
        return int(s+'0'*(32-c),2)
