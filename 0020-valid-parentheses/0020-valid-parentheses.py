class Solution(object):
    def isValid(self, s):
        d = {']':'[','}':'{',')':'('}
        x = []
        for i in s:
            if i in '{([':
                x.append(i)
            elif not x or d[i]!=x.pop():
                return False
        return not x