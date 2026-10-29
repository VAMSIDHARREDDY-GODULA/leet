class Solution(object):
    def findComplement(self, num):
        x = bin(num)[2:]
        y1 = x.replace('1','a')
        y2 = y1.replace('0','1')
        y3 = y2.replace('a', '0')
        return int(y3,2)