class Solution(object):
    def tribonacci(self, n):
        t1, t2, t3 = 0, 1, 1
        for i in range(n):
            t1, t2, t3 = t2, t3, t2+t3+t1
        return t1