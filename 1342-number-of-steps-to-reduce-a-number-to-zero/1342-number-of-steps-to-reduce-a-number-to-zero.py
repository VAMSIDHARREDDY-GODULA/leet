class Solution(object):
    def numberOfSteps(self, num):
        a = 0
        while num:
            if num%2:
                num -= 1
            else:
                num //= 2
            a += 1
        return a