class Solution(object):
    def construct2DArray(self, o, m, n):
        if len(o)!=m*n: return []
        b = []
        i = 0
        while i<len(o):
            b.append(o[i:i+n])
            i += n
        return b