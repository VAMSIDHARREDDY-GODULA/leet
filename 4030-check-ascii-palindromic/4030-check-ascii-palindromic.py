class Solution(object):
    def isPalindromic(self, s):
        x = ''
        for i in s:
            x += format(ord(i),'08b')
        return x==x[::-1]