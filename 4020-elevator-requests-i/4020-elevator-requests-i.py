class Solution(object):
    def elevatorRequests(self, n, r):
        x = a = 0
        for i in r:
            x += a-i if a>i else i-a
            a = i
        return x