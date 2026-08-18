class Solution(object):
    def isHappy(self, n):
        x = []
        while n!=1 and n not in x:
            x.append(n)
            z = 0
            while n:
                y = n%10
                z += y*y
                n //= 10
            n = z
        return n==1