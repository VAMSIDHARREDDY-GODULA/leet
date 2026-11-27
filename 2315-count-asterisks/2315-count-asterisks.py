class Solution(object):
    def countAsterisks(self, s):
        l = s.split('|')
        a = 0
        for i in range(0,len(l),2):
            a += l[i].count('*')
        return a