class Solution(object):
    def countPoints(self, r):
        d = {}
        for i in range(0,len(r),2):
            if r[i+1] in d: d[r[i+1]].append(r[i])
            else: d[r[i+1]]=[r[i]]
        a = 0
        for i in d:
            if len(set(d[i]))==3: a+=1
        return a