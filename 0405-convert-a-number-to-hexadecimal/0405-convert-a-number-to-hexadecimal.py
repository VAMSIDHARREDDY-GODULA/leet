class Solution(object):
    def toHex(self, num):
        d = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        r = ''
        if num<0: num += (2**32)
        while num>0:
            x = num%16
            if x in d: r = d[x]+r
            else: r = str(x)+r
            num //= 16
        return r if r else '0'