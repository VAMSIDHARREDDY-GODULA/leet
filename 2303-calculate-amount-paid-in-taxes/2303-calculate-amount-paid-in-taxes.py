class Solution(object):
    def calculateTax(self, b, n):
        l, t = 0, 0
        for i, j in b:
            x = min(i-l,n)
            t += x*j
            l = i
            n -= x
            if not n: return t/100.0