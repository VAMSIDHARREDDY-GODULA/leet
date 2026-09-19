class Solution(object):
    def subtractProductAndSum(self, n):
        a, c = 1, 0
        while n:
            x = n%10
            a *= x
            c += x
            n //= 10
        return a-c