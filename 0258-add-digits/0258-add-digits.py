class Solution(object):
    def addDigits(self, num):
     while num>9:
        x = 0
        for i in str(num):
            x += int(i)
        num = x
     return num