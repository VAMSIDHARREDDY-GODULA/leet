class Solution(object):
    def countPrefixes(self, w, s):
        a = 0
        for i in w:
            if s.startswith(i): a+=1
        return a