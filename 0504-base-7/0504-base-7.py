class Solution(object):
    def convertToBase7(self, num):
        if not num:
            return '0'
        f = '-' if num<0 else ''
        b = ''
        num = abs(num)
        while num:
            b = str(num%7) + b
            num //= 7
        return f+b