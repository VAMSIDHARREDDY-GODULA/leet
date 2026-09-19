class Solution(object):
    def balancedStringSplit(self, s):
        x = []
        a = 0
        for i in s:
            if x and i!=x[-1]:
                x.pop()
                if not x: a += 1
            else:
                x.append(i)
        return a