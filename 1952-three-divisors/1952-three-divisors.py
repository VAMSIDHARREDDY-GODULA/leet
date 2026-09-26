class Solution(object):
    def isThree(self, n):
        a = 2
        for i in range(2,n):
            if not n%i: a+=1
        return a==3