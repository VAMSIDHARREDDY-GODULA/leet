class Solution(object):
    def isPalindrome(self, s):
        x = re.sub(r'[^a-z0-9]','',s.lower())
        return x==x[::-1]