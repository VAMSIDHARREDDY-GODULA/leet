class Solution(object):
    def percentageLetter(self, s, l):
        x, y = s.count(l), len(s)
        return (x*100)/y