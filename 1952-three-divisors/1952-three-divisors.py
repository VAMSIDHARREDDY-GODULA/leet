class Solution(object):
    def isThree(self, n):
        a = 2
        for i in range(2,int(n**0.5)+1):
            if not n%i: 
                if i!=n//i: a+=1
                a += 1
        return a==3