class Solution(object):
    def kthDistinct(self, arr, k):
        for i in arr:
            if arr.count(i)==1:
                k -= 1
                if not k: return i
        return ''