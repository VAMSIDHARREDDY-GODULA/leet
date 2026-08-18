class Solution(object):
    def climbStairs(self, n):
        if n<3:
            return n
        small = 2
        larg = 1
        for _ in range(3,n+1):
            curr_step = small+larg
            larg = small
            small = curr_step
        return small  