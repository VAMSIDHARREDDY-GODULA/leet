class Solution(object):
    def minAddToMakeValid(self, s):
        x = []
        for i in s:
            if i==")" and x and x[-1]=='(': x.pop()
            else: x.append(i)
        return len(x)