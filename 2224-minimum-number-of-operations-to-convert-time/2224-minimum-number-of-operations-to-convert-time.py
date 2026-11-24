class Solution(object):
    def convertTime(self, c1, c2):
        x = ((int(c2[:2])-int(c1[:2]))*60)+(int(c2[3:])-int(c1[3:]))
        t = [60,15,5,1]
        a = 0
        for i in t:
            a += x//i
            x %= i
        return a