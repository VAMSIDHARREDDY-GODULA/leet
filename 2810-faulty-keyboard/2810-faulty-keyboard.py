class Solution(object):
    def finalString(self, s):
        x = []
        for i in s:
            if i=='i': x.reverse()
            else: x.append(i)
        return ''.join(x)