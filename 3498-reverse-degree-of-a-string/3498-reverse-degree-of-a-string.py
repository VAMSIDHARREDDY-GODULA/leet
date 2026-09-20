class Solution(object):
    def reverseDegree(self, s):
        a = 0
        for j,i in enumerate(s):
            a += (123-ord(i))*(j+1)
        return a