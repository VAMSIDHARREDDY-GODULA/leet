class Solution(object):
    def addToArrayForm(self, num, k):
        x = ''
        for i in num:
            x += str(i)
        x = str(int(x)+k)
        return [int(i) for i in x]