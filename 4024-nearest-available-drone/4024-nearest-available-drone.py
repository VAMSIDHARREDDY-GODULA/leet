class Solution(object):
    def nearestDrone(self, d, t):
        b = -1
        a = float('inf')
        t1, t2 = t
        for j, i in enumerate(d):
            x = abs(i[0]-t1)+abs(i[1]-t2)
            if x<=i[2] and a>x:
                a = x
                b = j
        return b