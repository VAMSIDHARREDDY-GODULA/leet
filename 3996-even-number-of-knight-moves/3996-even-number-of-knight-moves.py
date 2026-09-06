class Solution(object):
    def canReach(self, s, t):
        return (s[0]+t[0])%2==(s[1]+t[1])%2