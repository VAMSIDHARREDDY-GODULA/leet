class Solution(object):
    def mostWordsFound(self, s):
        return max(len(i.split()) for i in s)