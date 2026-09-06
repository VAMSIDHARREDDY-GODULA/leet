class Solution(object):
    def elevatorRequests(self, n, r):
        x = a = 0
        for i in r:
            x += abs(a-i)
            a = i
        return x