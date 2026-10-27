class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        i, j = 0, len(s)-1
        x = 'aeiouAEIOU'
        while i<j:
            if s[i] in x and s[j] in x:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if s[i] not in x: i+=1
            if s[j] not in x: j-=1
        return ''.join(s)