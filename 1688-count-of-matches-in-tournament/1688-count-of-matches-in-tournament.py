class Solution(object):
    def numberOfMatches(self, n):
        x, y = n, 0
        while x:
            if x%2: y = 1
            x //= 2
        return n-y