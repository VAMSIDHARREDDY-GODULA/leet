class Solution(object):
    def thousandSeparator(self, n):
        s = str(n)[::-1]
        r = ''
        for i in range(0,len(s),3):
            r += s[i:i+3]+'.'
        return r[::-1][1:]