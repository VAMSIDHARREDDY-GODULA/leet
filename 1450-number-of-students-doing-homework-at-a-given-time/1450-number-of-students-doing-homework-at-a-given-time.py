class Solution(object):
    def busyStudent(self, s, e, q):
        a = 0
        for i,j in enumerate(e):
            if s[i]<=q<=j: a+=1
        return a