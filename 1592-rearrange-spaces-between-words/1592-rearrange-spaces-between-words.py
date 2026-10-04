class Solution(object):
    def reorderSpaces(self, text):
        c = text.count(' ')
        s = text.split()
        n = len(s)
        if n==1: return s[0]+(' '*c) 
        x, y  = c//(n-1), c%(n-1)
        b = ''
        for i in s[:-1]:
            b += i+(' '*x)
        return b+s[-1]+(' '*y)