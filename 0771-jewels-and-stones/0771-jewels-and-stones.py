class Solution(object):
    def numJewelsInStones(self, j, s):
        b = 0
        for i in j:
            b += s.count(i)
        return b