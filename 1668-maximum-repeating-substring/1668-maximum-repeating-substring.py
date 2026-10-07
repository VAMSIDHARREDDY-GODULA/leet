class Solution(object):
    def maxRepeating(self, sequence, word):
        c, s = 0, word
        while word in sequence:
            c += 1
            word += s
        return c