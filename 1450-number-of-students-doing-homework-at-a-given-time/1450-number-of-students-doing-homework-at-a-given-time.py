class Solution(object):
    def busyStudent(self, s, e, q):
        a = 0
        for i,j in zip(s,e):
            if i<=q<=j: a+=1
        return a