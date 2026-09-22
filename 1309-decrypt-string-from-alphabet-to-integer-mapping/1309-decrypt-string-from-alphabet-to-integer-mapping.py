class Solution(object):
    def freqAlphabets(self, s):
        i = 0
        a = ''
        while i<len(s):
            if i+2<len(s) and s[i+2]=='#':
                a += chr(96+int(s[i:i+2]))
                i += 2
            else: a += chr(96+int(s[i]))
            i += 1
        return a