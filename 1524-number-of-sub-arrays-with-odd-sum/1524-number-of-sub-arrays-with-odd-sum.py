class Solution(object):
    def numOfSubarrays(self, arr):
        m = 10**9+7
        t = o = 0
        for i in arr:
            t += i
            o += t%2
        o += (len(arr)-o)*o
        return o%m