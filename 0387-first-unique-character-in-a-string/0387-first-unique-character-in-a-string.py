class Solution(object):
    def firstUniqChar(self, s):
        b = []
        for i in set(s):
            if s.count(i)==1:
                b.append(s.index(i))
        return min(b) if b else -1