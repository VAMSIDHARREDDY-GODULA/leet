class Solution(object):
    def sumZero(self, n):
        x = n//2
        if n%2:
            return list(range(-x,x+1))
        else:
            return list(range(-x,0))+list(range(1,x+1))