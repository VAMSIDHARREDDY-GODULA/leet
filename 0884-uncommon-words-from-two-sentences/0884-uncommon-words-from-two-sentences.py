class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        x = collections.Counter(s1.split()+s2.split())
        return [i for i,j in x.items() if j==1]