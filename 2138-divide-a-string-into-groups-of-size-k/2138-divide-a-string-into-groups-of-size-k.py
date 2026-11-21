class Solution(object):
    def divideString(self, s, k, fill):
        x = len(s)%k
        if x: s+=fill*(k-x)
        return [s[i:i+k] for i in range(0,len(s),k)]