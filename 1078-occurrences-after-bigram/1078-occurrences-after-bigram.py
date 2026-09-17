class Solution(object):
    def findOcurrences(self, text, first, second):
        x = text.split(' ')
        i = 0
        b = []
        while i<len(x)-2:
            if x[i]==first and x[i+1]==second:
                b.append(x[i+2])
            i += 1
        return b