class Solution(object):
    def greatestLetter(self, s):
        d = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
        for i in d:
            x = lower(i)
            if x in s and i in s: return i
        return ''